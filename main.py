# -*- coding: utf-8 -*-
__author__ = 'P. Saint-Amand'
__appname__ = 'BoilerPlate'
__version__ = 'V 1.0.0'

# Standard Python Modules
import logging
import os
from pathlib import Path
from typing import Any

# External Python Modules
# import pandas

# Personal Python Modules
from params import *
from utils.coloredlog import get_logger
from utils.filename import FileName     #CSVFile, ParameterFile

### Global Variables
### uncomment lines below if you want a dynamic log name instead
# LOGLEVEL_FILE = logging.DEBUG
# LOG_FILE = os.path.join(LOG_DIR,__appname__+".log")
# logfilename_object = FileName(LOG_FILE)
# logfilename_object.add_subname("subname")
# logfilename_object.add_datetime()
# LOG_FILE = logfilename_object.fullpath

### uncomment lines below if you want a dynamic name instead
OUT_FILE = os.path.join(OUT_DIR,__appname__+".csv")
# outfilename_object = FileName(OUT_FILE)
# # outfilename_object.add_subname("subname")
# outfilename_object.add_datetime()
# OUT_FILE = outfilename_object.fullpath

def init():
    """ Clear Screen, display banner & start the logger. """
    CONSOLE.clear_screen()
    if BANNER_DISPLAY:
        print(CONSOLE.get_app_banner(selection="random", banner_lst=BANNERS, appversion=__version__, creator="Designed by " + __author__))
    global logger
    logger = get_logger(logger_name=__appname__, console_loglevel=LOGLEVEL_CONSOLE, file_loglevel=LOGLEVEL_FILE, logfile=LOG_FILE, success_level=LOGLEVEL_SUCCESS)
    logger.info(f"Application Start")
    logger.info(f"Logging levels : Console={LOGLEVEL_CONSOLE}; File={LOGLEVEL_FILE}; Logfile='{LOG_FILE}'")
    logger.debug("Confirm Debug Mode is Activated")
    logger.log(LOGLEVEL_SUCCESS, 'Then success level that is a custom level')

if __name__ == "__main__":
    init()
    #TODO: insert your code here (ideally by calling functions)
