#!/usr/bin/python3
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
Date Created: SEP 16, 2017
Last Modified: SEP 16, 2017

Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt

(C) 2016 - 2017 K4YT3X
(C) 2017 fa11en
(C) 2017 Ivens Portugal
(C) 2017 Ahmed

"""
import os
import urllib.request
import argparse
import time

# Import Controller Packages
import iptables
from install import Install


def installPackage(package):
    while True:
        install = input('\033[31m\033[1mAVALON Framework not installed! Install now? [Y/n] \033[0m')
        if len(install) == 0 or install[0].upper() == 'Y':
            try:
                if os.path.isfile('/usr/bin/pip3'):
                    print('Installing using method 1')
                    os.system('pip3 install ' + package)
                elif os.path.isfile('/usr/bin/wget'):
                    print('Installing using method 2')
                    os.system('wget -O - https://bootstrap.pypa.io/get-pip.py | python3')
                    os.system('pip3 install ' + package)
                else:
                    print('Installing using method 3')
                    # import urllib.request
                    content = urllib.request.urlopen('https://bootstrap.pypa.io/get-pip.py')
                    with open('/tmp/get-pip.py', 'w') as getpip:
                        getpip.write(content.read().decode())
                        getpip.close()
                    os.system('python3 /tmp/get-pip.py')
                    os.system('pip3 install ' + package)
                    os.remove('/tmp/get-pip.py')
            except Exception as e:
                print('\033[31mInstallation failed!: ' + str(e))
                print('Please check your Internet connectivity')
                exit(0)
            print('\033[32mInstallation Succeed!\033[0m')
            print('\033[32mPlease restart the program\033[0m')
            exit(0)
        elif install[0].upper() == 'N':
            print('\033[31m\033[1mUnable to run program without dependencies!\033[0m')
            print('\033[33mAborting..\033[0m')
            exit(0)
        else:
            print('\033[31m\033[1mInvalid Input!\033[0m')


try:
    import avalon_framework as avalon
except ImportError:
    installPackage("avalon_framework")

try:
    import securityAudit
    from prettytable import PrettyTable
except ImportError:
    installPackage("prettytable")


VERSION = "0.0.1"


# -------------------------------- Functions --------------------------------

def processArguments():
    """
    This function parses all arguments
    """
    global args
    parser = argparse.ArgumentParser()
    control_group = parser.add_argument_group('Controls')
    control_group.add_argument("--enable", help="Enable DefenseMatrix", action="store_true", default=False)
    control_group.add_argument("--disable", help="Disable DefenseMatrix", action="store_true", default=False)
    control_group.add_argument("--openport", help="Open a TCP port", action="store", default=False)
    control_group.add_argument("--closeport", help="Close a TCP port", action="store", default=False)
    control_group.add_argument("--audit", help="Run system security audit", action="store_true", default=False)
    inst_group = parser.add_argument_group('Installation')
    inst_group.add_argument("--install", help="Install DefenseMatrix Automatically", action="store_true", default=False)
    inst_group.add_argument("--uninstall", help="Uninstall DefenseMatrix Automatically", action="store_true", default=False)
    inst_group.add_argument("--upgrade", help="Check DefenseMatrix & AVALON Framework Updates", action="store_true", default=False)
    args = parser.parse_args()


# -------------------------------- Procedural --------------------------------

processArguments()

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
    else:
        while True:
            iptables.ufw.generateStatistics()
            iptables.ufw.adjustStatus()
            time.sleep(5)
except KeyboardInterrupt:
    avalon.warning("Aborting")
