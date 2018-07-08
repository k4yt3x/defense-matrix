#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dev: fa11en
Date Created: September 16, 2017
Last Modified: September 18, 2017

Dev: K4YT3X
Last Modified: March 18, 2018

This is the script that is called to install DefenseMatrix.
Customizability (things to input) to this class are:
    install_location = /absolute/path/
    network manager = [WICD, NetworkManager, BOTH], BOTH is default
    network adapter = name (as listed under ifconfig), ALL is default

"""
from __future__ import print_function
import avalon_framework as avalon
import os
import passwd
import settings as st
import shutil
import sys


class Install:
    def __init__(self):
        # copy self to installation directory upon initialization
        os.system('mkdir -p %s' % st.INSTALLPATH)
        os.system('cp -r %s/* %s' % (os.getcwd(), st.INSTALLPATH))
        if os.path.islink("/usr/bin/DefenseMatrix") or os.path.isfile("/usr/bin/DefenseMatrix"):
            os.remove("/usr/bin/DefenseMatrix")
        os.system('ln -s %s/defenseMatrix.py /usr/bin/DefenseMatrix' % st.INSTALLPATH)

    def check_install(self):
        return os.path.exists(st.CONFPATH)

    def sequencePrint(self, msg):
        import time
        for word in str(msg):
            print(word, end="")
            time.sleep(0.0005)
        print()

    def printIcon(self):
        width, height = shutil.get_terminal_size((80, 20))
        spaces = (width - 56) // 2 * " "
        middle = (height - 14) // 2
        for _ in range(middle):
            print()
        self.sequencePrint(spaces + "d8888b. d88888b d88888b d88888b d8b   db .d8888. d88888b")
        self.sequencePrint(spaces + "88  `8D 88'     88'     88'     888o  88 88'  YP 88'")
        self.sequencePrint(spaces + "88   88 88ooooo 88ooo   88ooooo 88V8o 88 `8bo.   88ooooo")
        self.sequencePrint(spaces + "88   88 88~~~~~ 88~~~   88~~~~~ 88 V8o88   `Y8b. 88~~~~~")
        self.sequencePrint(spaces + "88  .8D 88.     88      88.     88  V888 db   8D 88.")
        self.sequencePrint(spaces + "Y8888D' Y88888P YP      Y88888P VP   V8P `8888Y' Y88888P")
        self.sequencePrint(spaces + "\n")
        self.sequencePrint(spaces + ".88b  d88.  .d8b.  d888888b d8888b. d888888b db    db")
        self.sequencePrint(spaces + "88'YbdP`88 d8' `8b `~~88~~' 88  `8D   `88'   `8b  d8'")
        self.sequencePrint(spaces + "88  88  88 88ooo88    88    88oobY'    88     `8bd8'")
        self.sequencePrint(spaces + "88  88  88 88~~~88    88    88`8b      88     .dPYb.")
        self.sequencePrint(spaces + "88  88  88 88   88    88    88 `88.   .88.   .8P  Y8.")
        self.sequencePrint(spaces + "YP  YP  YP YP   YP    YP    88   YD Y888888P YP    YP\n")

    def install(self):
        self.printIcon()
        self._install_passwdcmplx()
        self._install_tigher()
        self._install_arptables()
        self._install_scutum()
        os.system("chmod -R 755 " + st.INSTALLPATH)

        avalon.info("Installation Wizard Completed!")
        avalon.info("Settings will be effective immediately!")
        os.system("systemctl enable DefenseMatrix")
        os.system("systemctl start DefenseMatrix")

    def uninstall(self):
        os.system('iptables -F')  # Flush iptables settings
        os.system('arptables -F')  # Flush arptables settings
        sys.exit(0)
        exit(0)

    def _install_tigher(self):
        if not os.path.isfile("/usr/sbin/tiger"):
            os.system(st.gen_pack_install(st.package_manager, "tiger"))

    def _install_arptables(self):
        if os.system("which arptables"):
            os.system(st.gen_pack_install(st.package_manager, "arptables"))

    def _install_service(self):
        """
        THIS METHOD IS CURRENTLY NOT BEING USED

        There's no need for a service to be running in the background since
        SCUTUM firewall will control iptables and arptables
        """
        shutil.copyfile("DefenseMatrix", "/etc/init.d/DefenseMatrix")
        os.system("chmod 755 /etc/init.d/DefenseMatrix")
        os.system("update-rc.d DefenseMatrix defaults")

    def _install_passwdcmplx(self):
        passwd.replaceOriginalPasswd()

    def _install_scutum(self):
        if not os.system('which curl'):
            os.system("sudo sh -c \"$(curl -fsSL https://raw.githubusercontent.com/K4YT3X/SCUTUM/master/quickinstall.sh)\"")
        elif not os.system('which wget'):
            os.system("sudo sh -c \"$(wget https://raw.githubusercontent.com/K4YT3X/SCUTUM/master/quickinstall.sh -O -)\"")
