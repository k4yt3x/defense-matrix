#!/usr/bin/python3

'''
This is the script that is called to install DefenceMatrix.
Customizability (things to input) to this class are:
    install_location = /absolute/path/
    network manager = [WICD, NetworkManager, BOTH], BOTH is default
    network adapter = name (as listed under ifconfig), ALL is default

'''
from iptables import ufw
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


def setSSHPort(port):
    SSHD_CONFIG = '/etc/ssh/sshd_config'
    TEMP = '/tmp/sshd_config'
    with open(TEMP, 'w') as temp:
        with open(SSHD_CONFIG, 'r') as sshd:
            for line in sshd:
                if line[0:5] != 'Port ':
                    temp.write(line)
            temp.write('Port ' + str(port) + '\n')
    shutil.move(TEMP, SSHD_CONFIG)


def installWizard():
    print(avalon.FG.G + avalon.FM.BD + "Welcome to DefenseMatrix!")
    print("This is the setup wizard")
    print("You will be asked to answer basic questions about your server" + avalon.FM.RST)

    serverTypes = [
    "Web Server",
    "Mail Server",
    "Minecraft PC Server",
    ]
    print(serverTypes[0])

    for index in range(len(serverTypes)):
        print(str(index) + ". " + serverTypes[index])

    while True:
        serverSelection = avalon.gets("Which type of server it this?: ")
        try:
            serverType = serverTypes[int(serverSelection)]
            break
        except TypeError:
            avalon.error("Invalid Input!")

    if serverType == "Web Server":
        portsOpen = [80, 443]
    elif serverType == "Mail Server":
        portsOpen = [25, 587, 110]
    elif serverType == "Minecraft PC Server":
        portsOpen = [25565]

    avalon.info("DefenseMatrix takes care of your firewall settings for you")
    avalon.warning("This following step is going to reset your iptables configuration")
    if not avalon.ask("Is is okay to proceed right now?", True):
        exit(0)

    os.system("iptables -F")
    os.system("iptables -X")

    ufwctrl = iptables.ufw()

    sshSet = False
    avalon.info("It is " + avalon.FM.BD + "HIGHLY recommended to change your default port for ssh")
    if avalon.ask("Do you want to change it right now?", True):
        while True:
            sshport = avalon.gets("Which port do you want to change to?")
            if len(sshport) != 0:
                try:
                    sshport = int(sshport)
                    setSSHPort(sshport)
                    sshSet = True
                    avalon.info("SSH Port successfully set to " + str(sshport))
                    avalon.info("Effective after setup wizard is completed")
                    break
                except TypeError:
                    avalon.error("Please enter a valid port number between 1-65565!")
            else:
                avalon.error("Please enter a valid port number between 1-65565!")
    else:
        avalon.info("You can always change it using the command \"dm --ssh-port [port]\"")

    if sshSet:
        ufwctrl.allow(sshport)
    else:
        ufwctrl.allow(22)
    avalon.info("Installation Wizard Completed!")
    avalon.info("Settings will be effective immediately!")
    os.system("service ssh restart")
