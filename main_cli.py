# -*- coding: utf-8 -*-
__author__ = 'P. Saint-Amand'
__appname__ = 'BoilerPlate'
# __appname__, _ = os.path.splitext(os.path.basename(__file__))
__version__ = 'V 0.0.1'

# Standard Python Modules
import logging
import os
from pathlib import Path
from typing import Any

# External Python Modules
import typer

# Personal Python Modules
import utils
from constants import *

### Global Variables
all_args={}
output_format="txt"

def callback_outdir(value:Path) -> Path:
    if value and not value.is_dir() and os.path.splitext(value)[1]:
        raise typer.BadParameter(f"outdir must be a DIRECTORY (not a file)")
    return value

def callback_version(value:bool) -> None:
    if value:
        # print(f"{__appname__} {__version__}")
        print(CONSOLE.get_app_banner(selection="random", banner_lst=banner_lst, appversion=__version__, creator="Designed by " + __author__))
        raise typer.Exit()

def get_logger(logger_name:str=None, console_loglevel:int=LOGLEVEL_SUCCESS, file_loglevel:int=LOGLEVEL_DISABLE, logfile:Path=None) -> utils.ColorLogger:
    if not logfile and file_loglevel != LOGLEVEL_DISABLE:
        logfile = os.path.join(LOG_DIR,__appname__+".log")
    if not logger_name:
        logger_name, _ = os.path.splitext(os.path.basename(__file__))

    
    logging.addLevelName(LOGLEVEL_SUCCESS, 'SUCCESS')
    log_options = utils.ColorLoggerOptions(logfile_name=logfile, console_logging_level=console_loglevel, logfile_logging_level=file_loglevel)
    logger = utils.ColorLogger(name=__appname__, options=log_options)
    # save_logger_options(log_options)
    return logger

def init(banner=True):
    """ Clear Screen, display banner & start the logger. """
    CONSOLE.clear_screen()
    if banner:
        print(CONSOLE.get_app_banner(selection="random", banner_lst=banner_lst, appversion=__version__, creator="Designed by " + __author__))
    if all_args["debug"]:
        LOGLEVEL_CONSOLE = LOGLEVEL_SUCCESS
    else:
        LOGLEVEL_CONSOLE = LOGLEVEL_DISABLE
    if all_args["logfile"]:
        LOGLEVEL_FILE = logging.DEBUG
    else:
        LOGLEVEL_FILE = LOGLEVEL_DISABLE
    global logger
    logger = get_logger(logger_name=__appname__, console_loglevel=LOGLEVEL_CONSOLE, file_loglevel=LOGLEVEL_FILE, logfile=all_args["logfile"])
    logger.debug("Debug Mode Activated")

def main(infile:Path = typer.Argument(..., exists=True, readable=True, resolve_path=True, show_default=False, help="The file name (with path) of the file to be analyzed."),
        outdir:Path = typer.Option(None, "--outdir", "-d", exists=False, resolve_path=True, show_default="Same directory as infile", help="Location of the output file", callback=callback_outdir),
        outfile:Path = typer.Option(None, "--outfile", "-o", exists=False, resolve_path=True, show_default="Same directory and filename (with new extension) as infile", help="File Name of the output file"),
        banner:bool = typer.Option(True, help="Display a banner at start of the program", rich_help_panel="Customization and Utils"),
        debug:bool = typer.Option(False, help="Enable debug mode on the console", rich_help_panel="Customization and Utils"),
        logfile:Path = typer.Option(None, "--logfile", "-l", exists=False, resolve_path=True,  help="logfile of detailed activities (debug mode)", rich_help_panel="Customization and Utils"),
        version:bool = typer.Option(False, "--version", "-v", callback=callback_version, is_eager=True, help="Display version of the program", rich_help_panel="Customization and Utils")
        ) -> None:
    # Put all arguments in a dictionnary & perform extra validation or default value assigment
    # Needed in order to be able to compare/use value of other parameters, what was not possible using callback procedure
    all_args["infile"]=infile
    all_args["outdir"]=outdir
    all_args["outfile"]=outfile
    all_args["banner"]=banner
    all_args["debug"]=debug
    all_args["logfile"]=logfile
    all_args["version"]=version
    
    init(banner=all_args["banner"])
    validate_params()

    all_args_str=""
    for k,v in all_args.items():
        all_args_str += f"  - {k}: {v}\n"
    logger.debug(f"Parameters :\n{all_args_str}")

    ### TODO: Add you code here below ###

    # End of program
    if all_args["logfile"]:
        logger.log(LOGLEVEL_SUCCESS, f'logfile available on : {all_args["logfile"]}')
        
def validate_params() -> None:
    # Generate default value for missing outfile and/or outdir parameters
    if all_args["outfile"] and all_args["outdir"]:  # Both parameters have been specified
        all_args["outdir"] = os.path.dirname(os.path.abspath(all_args["outfile"]))
        logger.warning(f"Both outdir and outfile parameters specified. outdir overwrite with path of outfile : {all_args['outdir']}")
    elif all_args["outdir"]:        # only outdir has been specified
        filename, _ = os.path.splitext(os.path.basename(all_args["infile"]))
        filename += "." + output_format
        all_args["outfile"] = os.path.join(all_args["outdir"],filename)
    elif all_args["outfile"]:       # only outfile has been specified
        all_args["outdir"] = os.path.dirname(os.path.abspath(all_args["outfile"]))
    else:                           # No parameter specified regarding output
        all_args["outdir"] = os.path.dirname(os.path.abspath(all_args["infile"]))
        filename, _ = os.path.splitext(os.path.basename(all_args["infile"]))
        filename += "." + output_format
        all_args["outfile"] = os.path.join(all_args["outdir"],filename)

    # create output directory if not exists
    outdir=all_args["outdir"]
    if not os.path.exists(outdir):
        logger.warning(f"Output directory doesn't exists: '{outdir}'")
        try:
            os.makedirs(outdir)                   
        except Exception as e:
            logger.error(f"Unable to create output directory '{outdir}':")
            logger.error(f"{str(e)}")
            raise typer.Abort()
        else:
            logger.log(LOGLEVEL_SUCCESS, f"Output directory successfully created : '{outdir}'")

if __name__ == "__main__":
    CONSOLE.clear_screen()
    typer.run(main)
