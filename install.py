#!/usr/bin/python3

'''
This is the script that is called to install DefenceMatrix.
Customizability (things to input) to this class are:
    install_location = /absolute/path/
    network manager = [WICD, NetworkManager, BOTH], BOTH is default
    network adapter = name (as listed under ifconfig), ALL is default

'''

import inspect
import os
import sys
import settings as st


class Install:
    def __init__(self, install_location='/usr/share/'):
        self.install_location = install_location.rstrip('/', 1) + '/DefenseMatrix'

        os.system('mkdir -p %s' % self.install_location)
        os.system('cp -r %s/* %s/' % (os.cwd(), self.install_location))
        os.system('ln -s %s/defenceMatrix.py /usr/bin/defencematrix' % self.install_location)

        self._installed = {
            'iptables': False,
            'arptables': False,
            'rkhunt': False,
            'tripwire': False,
            'passwdcmplx': False,
            'config': False
        }

    def install(self):
        # run all the required installations
        # TODO: allow user to choose which parts they want installed
        self._install_iptables()
        self._install_arptables()
        self._install_rkhunt()
        self._install_tripwire()
        self._install_passwdcmplx()
        self._install_config()

    # to uninstall just read the list of all installed packages and
    # crated files, and remove them.
    def uninstall(self):
        for method in self._installed.keys():
            # if self._installed[method]:
            exec('self._install_%s(remove=True)' % method)

        sys.exit(0)
        exit(0)

    def check_install(self):
        return os.path.exists(st.CONFPATH)

    def _install_iptables(self, remove=False):
        def uninstall():
            pass
        if remove:
            return uninstall()

    def _install_arptables(self, network_managers='all', remove=False):
        def uninstall():
            os.system(st.gen_pack_remove(st.package_manager, 'arptables'))
        if remove:
            return uninstall()

        def wicd():
            # if wicd is not installed, ask to install
            if not os.path.isdir('/etc/wicd'):
                if av.ask('WICD not installed, install?', True):
                    if not os.system(st.gen_pack_install(st.package_manager, 'wicd')):
                        abort

        def network_manager():


        # check arptables installation
        if not (os.path.isfile('/usr/bin/arptables')
                or os.path.isfile('/usr/sbin/arptables')):
            if os.system(st.gen_pack_install(st.package_manager, 'arptables')):
                print('Invalid package manager. Unable to proceed. ')
        else:
            av.error('arptables not installed. Unable to proceed. ' +
                     'Aborting...')
            uninstall()



        # retrieve method name and set its respective value in _installed
        self._installed[inspect.stack()[0][3].rsplit('_', 1)[-1]] = True

    def _install_rkhunt(self, remove=False):
        def uninstall():
            pass
        if remove:
            return uninstall()

    def _install_tripwire(self, remove=False):
        def uninstall():
            pass
        if remove:
            return uninstall()

    def _install_passwdcmplx(self, remove=False):
        def uninstall():
            pass
        if remove:
            return uninstall()

    def _install_config(self, remove=False):
        def uninstall():
            pass
        if remove:
            return uninstall()

