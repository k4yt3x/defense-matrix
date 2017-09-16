import inspect
import os
import sys
import avalon_framework as av
import settings as st


class Install:
    def __init__(self, install_location='/usr/share/'):
        self.install_location = install_location
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

    def _install_arptables(self, remove=False):
        def uninstall():
            os.system(st.gen_pack_remove(st.package_manager, 'arptables'))
        if remove:
            return uninstall()

        # check arptables installation
        if not (os.path.isfile('/usr/bin/arptables')
                or os.path.isfile('/usr/sbin/arptables')):
            if os.system(st.gen_pack_install(st.package_manager, 'arptables')):
                print('Invalid package manager. Unable to proceed. ')
        else:
            av.error('arptables not installed. Unable to proceed. ' +
                     'Aborting...')
            self._install_arptables().uninstall()

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

