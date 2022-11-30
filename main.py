# -*- coding: utf-8 -*-
__author__ = 'P. Saint-Amand'
__version__ = 'V 0.0.1'

# Standard Python Modules
import logging
from pathlib import Path
from typing import Any

# External Python Modules
# import pandas as pd
# import typer

# Personal Python Modules
import utils
from constants import *

def get_logger(console_loglevel:int=LOGLEVEL_SUCCESS, file_loglevel:int=LOGLEVEL_DISABLE, logfile:Path=None) -> utils.ColorLogger:
    appname, _ = os.path.splitext(os.path.basename(__file__))
    if not logfile and file_loglevel != LOGLEVEL_DISABLE:
        logfile = os.path.join(LOG_DIR,appname+".log")
    
    logging.addLevelName(LOGLEVEL_SUCCESS, 'SUCCESS')
    log_options = utils.ColorLoggerOptions(logfile_name=logfile, console_logging_level=console_loglevel, logfile_logging_level=file_loglevel)
    logger = utils.ColorLogger(name=appname, options=log_options)
    # save_logger_options(log_options)
    return logger

def init():
    """ Clear Screen, display banner & start the logger. """
    CONSOLE.clear_screen()
    if BANNER:
        print(CONSOLE.get_app_banner(selection="random", banner_lst=banner_lst, appversion=__version__, creator="Designed by " + __author__))
    global logger
    logger = get_logger(console_loglevel=LOGLEVEL_CONSOLE, file_loglevel=LOGLEVEL_FILE)
    logger.debug("Debug Mode Activated")

if __name__ == "__main__":
    init()