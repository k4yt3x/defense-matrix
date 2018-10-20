#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Defense Matrix
Dev: K4YT3X
Dev: fa11en
Date Created: September 16, 2017
Last Modified: October 19, 2018

Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt

(C) 2017 - 2018 K4YT3X
(C) 2017 fa11en
(C) 2017 Ivens Portugal
(C) 2017 Ahmed

Description: Defense Matrix is a tool that will help you setup the basic
yet most of the things that you'll ever need to secure a Linux server.
With the number of Internet attacks keeps increasing, securing your Linux
servers might not be a bad idea.

"""
from avalon_framework import Avalon
from install import Install
from security_audit import SecurityAudit
import argparse
import os
import sys
import traceback

VERSION = '1.1.0'


# -------------------------------- Functions --------------------------------

def process_arguments():
    """
    This function parses all arguments
    """
    parser = argparse.ArgumentParser()
    inst_group = parser.add_argument_group('Installation')
    inst_group.add_argument('--install', help='Install defense matrix components', action='store_true', default=False)
    inst_group.add_argument('--uninstall', help='Uninstall defense matrix components', action='store_true', default=False)
    control_group = parser.add_argument_group('Controls')
    control_group.add_argument('--audit', help='Run system security audit', action='store_true', default=False)
    etc = parser.add_argument_group('Extra')
    etc.add_argument('--version', help='Show defense matrix version and exit', action='store_true', default=False)
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    return parser.parse_args()


# -------------------------------- Procedural --------------------------------

args = process_arguments()

if args.version:  # prints program legal / dev / version info
    print('Current Version: ' + VERSION)
    print('Author: K4YT3X')
    print('License: GNU GPL v3')
    print('Github Page: https://github.com/K4YT3X/defense-matrix')
    print('Contact: k4yt3x@k4yt3x.com\n')
    exit(0)

if os.getuid() != 0:
    Avalon.error('This app requires root privilege to run!')
    exit(1)

try:
    if args.install:
        installer = Install()
        installer.install()
    elif args.uninstall:
        uninstaller = Install()
        uninstaller.uninstall()
    elif args.audit:
        audit = SecurityAudit()
        audit.run()
except KeyboardInterrupt:
    Avalon.warning('Aborting')
except Exception:
    Avalon.error('An exception was caught')
    traceback.print_exc()
