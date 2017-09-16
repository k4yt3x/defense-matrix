"""
Name: K4YT3X
      Fa11en
Date Created: SEP 16, 2017
Last Modified: SEP 16, 2017

Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt

(C) 2016 - 2017 K4YT3X
(C) 2017 fa11en
(C) 2017 Ivens Portugal

"""
import os
import urllib.request
import argparse

# Import Controller Packages
from iptables import ufw
from arptables import arptables
from install import Install


try:
    import avalon_framework as avalon
except ImportError:
    while True:
        install = input('\033[31m\033[1mAVALON Framework not installed! Install now? [Y/n] \033[0m')
        if len(install) == 0 or install[0].upper() == 'Y':
            try:
                if os.path.isfile('/usr/bin/pip3'):
                    print('Installing using method 1')
                    os.system('pip3 install avalon_framework')
                elif os.path.isfile('/usr/bin/wget'):
                    print('Installing using method 2')
                    os.system('wget -O - https://bootstrap.pypa.io/get-pip.py | python3')
                    os.system('pip3 install avalon_framework')
                else:
                    print('Installing using method 3')
                    # import urllib.request
                    content = urllib.request.urlopen('https://bootstrap.pypa.io/get-pip.py')
                    with open('/tmp/get-pip.py', 'w') as getpip:
                        getpip.write(content.read().decode())
                        getpip.close()
                    os.system('python3 /tmp/get-pip.py')
                    os.system('pip3 install avalon_framework')
                    os.remove('/tmp/get-pip.py')
            except Exception as e:
                print('\033[31mInstallation failed!: ' + str(e))
                print('Please check your Internet connectivity')
                exit(0)
            print('\033[32mInstallation Succeed!\033[0m')
            print('\033[32mPlease restart the program\033[0m')
            exit(0)
        elif install[0].upper() == 'N':
            print('\033[31m\033[1mSCUTUMM requires avalon framework to run!\033[0m')
            print('\033[33mAborting..\033[0m')
            exit(0)
        else:
            print('\033[31m\033[1mInvalid Input!\033[0m')


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

if args.install:
    installer = Install()
    installer.install()
elif args.uninstall:
    uninstaller = Install()
    uninstaller.uninstall()
elif args.openport:
    try:
        ports = args.openport.split(',')
        for port in ports:
            ufw.allow(port)
    except TypeError:
        avalon.error("Not a valid port number!")
elif args.closeport:
    try:
        ports = args.closeport.split(',')
        for port in ports:
            ufw.expire(port)
    except TypeError:
        avalon.error("Not a valid port number!")

else:
    pass
