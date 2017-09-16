#!/usr/bin/python3

'''
This is the script that is called to install DefenceMatrix.
Customizability (things to input) to this class are:
    install_location = /absolute/path/
    network manager = [WICD, NetworkManager, BOTH], BOTH is default
    network adapter = name (as listed under ifconfig), ALL is default

'''
import avalon_framework as avalon
from iptables import ufw
import inspect
import os
import sys
import settings as st


class Install:
    def __init__(self):
        # copy self to installation directory upon initialization
        os.system('mkdir -p %s' % st.INSTALLPATH)
        os.system('cp -r %s/* %s' % (os.getcwd(), st.INSTALLPATH))
        os.system('ln -s %s/defenceMatrix.py /usr/bin/defencematrix'
                  % st.INSTALLPATH)

    def check_install(self):
        return os.path.exists(st.CONFPATH)

    def install(self):
        # check if we're already installed
        if self.check_install():
            print('DefenseMatrix is already installed.')
            return
        open_ports, ssh_port = self._get_inputs()
        self._install_iptables(open_ports + [ssh_port])
        self._install_arptables()
        self._install_rkhunt()
        self._install_passwdcmplx()
        self._install_config(ssh_port)

        avalon.info("Installation Wizard Completed!")
        avalon.info("Settings will be effective immediately!")

    # to uninstall just read the list of all installed packages and
    # crated files, and remove them.
    # (i.e. anything at st.CONFPATH, st.INSTALLPATH, and the st.packages list)
    def uninstall(self):
        sys.exit(0)
        exit(0)

    def _get_inputs(self):
        # welcome and banner
        print(avalon.FG.G + avalon.FM.BD + "Welcome to DefenseMatrix!")
        print("This is the setup wizard")
        print("You will be asked to answer basic questions about your server" + avalon.FM.RST)

        for index, server_type in enumerate(st.server_types):
            print('%d.  %s' % (index, server_type))

        while True:
            server_select = avalon.gets("Select your type of server: ")
            try:
                server_type = list(st.server_types.keys())[int(server_select)]
                break
            except TypeError:
                avalon.error("Invalid Input!")

        for server in st.server_types.keys():
            open_ports = st.server_types[server]

        avalon.info("DefenseMatrix takes care of your firewall settings for you.")
        avalon.warning("This following step is going to reset your iptables configuration")
        if not avalon.ask("Is is okay to proceed?", True):
            exit(0)

        os.system("iptables -F")
        os.system("iptables -X")

        ssh_port = 22
        avalon.info("It is " + avalon.FM.BD + "HIGHLY recommended to change your default port for ssh")
        if avalon.ask("Do you want to change it now?", True):
            while True:
                try:
                    ssh_port = int(avalon.gets("Which port do you want to change to?"))
                    if int(ssh_port) <= 0:
                        raise TypeError
                    else:
                        break
                except TypeError:
                    avalon.error("Please enter a valid port number between 1-65565!")
        else:
            avalon.info("You can always change it using the command \"dm --ssh-port [port]\"")

        return open_ports, ssh_port

    def _install_iptables(self, open_ports):
        ufwctrl = ufw()
        for port in open_ports:
            ufw.allow(port)

    def _install_arptables(self, network_managers='all', remove=False):
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
            avalon.error('arptables not installed. Unable to proceed. ' +
                         'Aborting...')
            uninstall()

        # retrieve method name and set its respective value in _installed
        # self._installed[inspect.stack()[0][3].rsplit('_', 1)[-1]] = True

    def _install_rkhunt(self):
        pass

    def _install_passwdcmplx(self):
        pass

    def _install_config(self, ssh_port):
        # generate ssh port configuration
        sshd_config = [line for line in st.read_file(st.SSHD_CONFIG)
                       if line[0:5] != 'Port ']
        print(sshd_config)
        sshd_config.append('Port %s\n' % str(ssh_port))
        st.write_file('\n'.join(sshd_config), st.SSHD_CONFIG, mode='w')
        avalon.info("SSH Port successfully set to " + str(ssh_port))
        os.system("service ssh restart")

