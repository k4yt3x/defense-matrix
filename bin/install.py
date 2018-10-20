#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dev: fa11en
Date Created: September 16, 2017
Last Modified: September 18, 2017

Dev: K4YT3X
Last Modified: October 19, 2018

This is the script that is called to install defense-matrix.
"""
from avalon_framework import Avalon
from utilities import Utilities
import os
import passwd
import shutil

VERSION = '1.0.0'


class Install:
    """ Install class

    This class will take care of all the installations.
    It will install all the packages, scripts, and deploy
    everything into place.
    """

    def __init__(self):

        self.executable = '/usr/bin/defense-matrix'

        # Get current defense matrix path
        self.current_dir = os.path.dirname(os.path.realpath(__file__)).replace('/bin', '')
        self.install_dir = '/usr/share/defense-matrix'

    def install(self):
        """ Start the installation

        Start the installation and install all packages and
        components.
        """

        self._install_defense_matrix()
        self._install_passwdcmplx()
        self._install_tigher()
        self._install_rkhunter()
        self._install_scutum()

        Avalon.info('Installation Wizard Completed!')
        Avalon.info('Settings will be effective immediately!')

    def uninstall(self):
        """ Uninstall everything this system has deployed

        This is yet to be completed.
        """

        if not Avalon.ask('Are you sure to uninstall defense matrix completely?'):
            return

        # Restore original passwd binary
        passwd.restore_original_passwd()

        # Remove SCUTUM
        Utilities.execute(['scutum', '--uninstall'])

        # Flush iptables and arptables
        Utilities.execute(['iptables', '-F'])
        Utilities.execute(['arptables', '-F'])

        # Remove defense matrix directory
        shutil.rmtree(self.install_dir)

        # Remove linked executables
        os.remove(self.executable)

        exit(0)

    def _install_defense_matrix(self):
        """ Installs defense matrix to system and
        link defense matrix executable to bin path.
        """

        # Get installation destination from user
        user_install_dir = Avalon.gets('Installation destination (\"/usr/share/defense-matrix\")')
        if user_install_dir != '':
            self.install_dir = user_install_dir

        # If files already at the correct directory, return
        if self.current_dir == self.install_dir:
            return

        # Check if destination directory occupied
        if os.path.isdir(self.install_dir) or os.path.islink(self.install_dir):
            if not Avalon.ask('Target directory exists. Overwrite?', True):
                Avalon.warning('Aborting installation: target directory not writable')
            if os.path.isdir(self.install_dir):
                shutil.rmtree(self.install_dir)
            else:
                os.remove(self.install_dir)

        # Copy defense matrix to destination directory
        shutil.copytree(self.current_dir, self.install_dir)

        # If defense-matrix is already linked to path, remove it
        if os.path.islink(self.executable) or os.path.isfile(self.executable):
            os.remove(self.executable)  # Remove old file or symbolic links

        # Link current defense-matrix.py to path
        Utilities.execute(['ln', '-s', '{}/bin/defense-matrix.py'.format(self.current_dir), self.executable])

    def _install_tigher(self):
        """ Install tiger

        Tiger is a package that will help controlling tripwire,
        an HIDS, which hardens the system from the binary aspect.
        """
        if not shutil.which('tiger'):
            Utilities.install_package('tiger')

    def _install_rkhunter(self):
        """ Install rkhunter

        rkhunter is a rootkit detector that runs sanity checks
        on system binary files and system misconfigurations.
        """
        if not shutil.which('rkhunter'):
            Utilities.install_package('rkhunter')

    def _install_passwdcmplx(self):
        """ Install passwd

        Replace the system default passwd command with our
        own passwd command.
        """
        passwd.replace_original_passwd()

    def _install_scutum(self):
        """ Installing SCUTUM

        SCUTUM will control iptables and arptables, providing
        security for TCP/UDP/ICMP/ARP.
        """
        if shutil.which('curl'):
            os.system('sudo sh -c \"$(curl -fsSL https://raw.githubusercontent.com/K4YT3X/scutum/master/bin/quickinstall.sh)\"')
        elif shutil.which('wget'):
            os.system('sudo sh -c \"$(wget https://raw.githubusercontent.com/K4YT3X/scutum/master/bin/quickinstall.sh -O -)\"')
