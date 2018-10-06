#!/usr/bin/python

# pyham client program

# Command line parameters:
# --help
# --configfile path/file.conf
# --logfile path/file.log

# TODO:
# - Keyboard key (space) as PTT button without character repeating loop while holding down
# - Translate to different languages / Localization
# - Status bar (with log display)
# - Log command line parameters and config variables

programName = "Pyham Client"
programVersion = "0.013"
filename_config = "pyham_client.conf"
filename_log = "pyham_client.log"

import sys
import argparse
from log import log
from client import Client

# Read command line parameters:
parser = argparse.ArgumentParser(description = programName + " " + programVersion)
parser.add_argument('-c', '--configfile', help='use this configuration file')
parser.add_argument('-l', '--logfile', help='log to this file')
parser.add_argument('-n', '--nogui', action='store_true', help='start without wxWidgets GUI')
parser.add_argument('-t', '--terminal', action='store_true', help='start with separate console window (when using GUI)')

args = parser.parse_args()
if args.configfile != None:
	filename_config = args.configfile
if args.logfile != None:
	filename_log = args.logfile

# Start client:
log("Program started.")

if args.nogui:
	client = Client(filename_config)
else:
	from client import ClientWx
	client = ClientWx(filename_config, args.terminal)

client.run()

# Terminate program:
log("Exit program.")
