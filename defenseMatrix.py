#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

d8888b. d88888b d88888b d88888b d8b   db .d8888. d88888b
88  `8D 88'     88'     88'     888o  88 88'  YP 88'
88   88 88ooooo 88ooo   88ooooo 88V8o 88 `8bo.   88ooooo
88   88 88~~~~~ 88~~~   88~~~~~ 88 V8o88   `Y8b. 88~~~~~
88  .8D 88.     88      88.     88  V888 db   8D 88.
Y8888D' Y88888P YP      Y88888P VP   V8P `8888Y' Y88888P


.88b  d88.  .d8b.  d888888b d8888b. d888888b db    db
88'YbdP`88 d8' `8b `~~88~~' 88  `8D   `88'   `8b  d8'
88  88  88 88ooo88    88    88oobY'    88     `8bd8'
88  88  88 88~~~88    88    88`8b      88     .dPYb.
88  88  88 88   88    88    88 `88.   .88.   .8P  Y8.
YP  YP  YP YP   YP    YP    88   YD Y888888P YP    YP



Name: K4YT3X
      Fa11en
Date Created: September 16, 2017
Last Modified: March 15, 2018

Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt

(C) 2017 - 2018 K4YT3X
(C) 2017 fa11en
(C) 2017 Ivens Portugal
(C) 2017 Ahmed

"""
import argparse
import os
import sys

# Import Controller Packages
from install import Install
import avalon_framework as avalon
import securityAudit


VERSION = "1.0 alpha"


# -------------------------------- Functions --------------------------------

def processArguments():
    """
    This function parses all arguments
    """
    parser = argparse.ArgumentParser()
    control_group = parser.add_argument_group('Controls')
    control_group.add_argument("--enable", help="Enable DefenseMatrix", action="store_true", default=False)
    control_group.add_argument("--disable", help="Disable DefenseMatrix", action="store_true", default=False)
    control_group.add_argument("--audit", help="Run system security audit", action="store_true", default=False)
    inst_group = parser.add_argument_group('Installation')
    inst_group.add_argument("--install", help="Install DefenseMatrix Automatically", action="store_true", default=False)
    inst_group.add_argument("--uninstall", help="Uninstall DefenseMatrix Automatically", action="store_true", default=False)
    inst_group.add_argument("--upgrade", help="Check DefenseMatrix & AVALON Framework Updates", action="store_true", default=False)
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    return parser.parse_args()


# -------------------------------- Procedural --------------------------------

args = processArguments()

if os.getuid() != 0:
    avalon.error("This app requires root privilege to run!")
    exit(0)


try:
    if args.install:
        installer = Install()
        installer.install()
    elif args.uninstall:
        uninstaller = Install()
        uninstaller.uninstall()
    elif args.audit:
        securityAudit.audit()
except KeyboardInterrupt:
    avalon.warning("Aborting")
