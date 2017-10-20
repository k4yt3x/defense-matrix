#!/usr/bin/python3

'''
This is the script that is called to install DefenseMatrix.
Customizability (things to input) to this class are:
    install_location = /absolute/path/
    network manager = [WICD, NetworkManager, BOTH], BOTH is default
    network adapter = name (as listed under ifconfig), ALL is default

'''
from __future__ import print_function
import avalon_framework as avalon
from iptables import ufw
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
        # check if we're already installed
        # if self.check_install():
        #    print('DefenseMatrix is already installed.')
        #    return
        # check for which packages we need to install
        self.printIcon()
        self._install_packages()
        open_ports, ssh_port = self._get_inputs()
        self._install_iptables(open_ports + [ssh_port])
        self._install_arptables()
        self._install_passwdcmplx()
        self._install_config(ssh_port)
        self._install_service()
        self._install_port_controllers()
        self._install_tigher()
        self._install_ufw
        os.system("chmod -R 755 " + st.INSTALLPATH)

        avalon.info("Installation Wizard Completed!")
        avalon.info("Settings will be effective immediately!")
        os.system("systemctl enable DefenseMatrix")
        os.system("systemctl start DefenseMatrix")

    # to uninstall just read the list of all installed packages and
    # crated files, and remove them.
    # (i.e. anything at st.CONFPATH, st.INSTALLPATH, and the st.packages list)
    def uninstall(self):
        os.system('iptables -F')
        os.system('arptables -F')
        sys.exit(0)
        exit(0)

    def _get_inputs(self):
        # welcome and banner
        server_types = [
            "Web Server",
            "Mail Server",
            "Minecraft PC Server",
        ]

        print(avalon.FG.G + avalon.FM.BD + "Welcome to DefenseMatrix!")
        print("This is the setup wizard")
        print("You will be asked to answer basic questions about your server" + avalon.FM.RST)

        for index in range(len(server_types)):
            print(str(index) + ". " + server_types[index])

        while True:
            server_select = avalon.gets("Select your type of server: ")
            try:
                server_type = server_types[int(server_select)]
                break
            except ValueError:
                avalon.error("Invalid Input!")

        if server_type == "Web Server":
            open_ports = [80, 443]
        elif server_type == "Mail Server":
            open_ports = [25, 110, 587]
        elif server_type == "Minecraft PC Server":
            open_ports = [25565]

        print(open_ports)
        avalon.info("DefenseMatrix takes care of your firewall settings for you.")
        avalon.warning("This following step is going to reset your iptables configuration")
        if not avalon.ask("Is is okay to proceed?", True):
            exit(0)

        os.system("iptables -F")
        os.system("iptables -X")
        os.system("ufw --force reset")

        ssh_port = 22
        avalon.info("It is " + avalon.FM.BD + "HIGHLY recommended to change your default port for ssh")
        if avalon.ask("Do you want to change it now?", True):
            while True:
                try:
                    ssh_port = avalon.gets("Which port do you want to change to?: ")
                    if len(ssh_port) == 0:
                        avalon.error("Please enter a valid port number between 1-65565!")
                        pass
                    else:
                        ssh_port = int(ssh_port)
                        break
                except ValueError:
                    avalon.error("Please enter a valid port number between 1-65565!")
        else:
            avalon.info("You can always change it using the command \"dm --ssh-port [port]\"")

        return open_ports, ssh_port

    def _install_ufw(self):
        if not os.path.isfile("/usr/sbin/ufw"):
            os.system(st.gen_pack_install(st.package_manager, "ufw"))

    def _install_tigher(self):
        if not os.path.isfile("/usr/sbin/tiger"):
            os.system(st.gen_pack_install(st.package_manager, "tiger"))

    def _install_port_controllers(self):
        os.system('ln -s %s/openport.py /usr/bin/openport' % st.INSTALLPATH)
        os.system("chmod 755 %s/openport.py" % st.INSTALLPATH)
        os.system('ln -s %s/closeport.py /usr/bin/closeport' % st.INSTALLPATH)
        os.system("chmod 755 %s/closeport.py" % st.INSTALLPATH)

    def _install_service(self):
        shutil.copyfile("DefenseMatrix", "/etc/init.d/DefenseMatrix")
        os.system("chmod 755 /etc/init.d/DefenseMatrix")
        os.system("update-rc.d DefenseMatrix defaults")

    def _install_packages(self):
        cur_packs = [curpack.split()[1] for curpack in
                     os.popen('dpkg -l').read().split('\n') if len(curpack.split()) > 1]

        to_install = [pack for pack in st.required_packages if pack not in cur_packs]
        os.system(st.gen_pack_install(st.package_manager, ' '.join(to_install)))

    def _install_iptables(self, open_ports):
        for port in open_ports:
            ufw.allow(port)
            ufw.adjustStatus()

    def _install_arptables(self, network_managers='all', remove=False):
        def uninstall():
            os.system(st.gen_pack_remove(st.package_manager, 'arptables'))
        if remove:
            return uninstall()

        # check arptables installation
        if not (os.path.isfile('/usr/bin/arptables') or os.path.isfile('/usr/sbin/arptables')):
            if os.system(st.gen_pack_install(st.package_manager, 'arptables')):
                print('Invalid package manager. Unable to proceed. ')
        else:
            avalon.error('arptables not installed. Unable to proceed. Aborting...')
            uninstall()

        # retrieve method name and set its respective value in _installed
        # self._installed[inspect.stack()[0][3].rsplit('_', 1)[-1]] = True

    def _install_passwdcmplx(self):
        passwd.replaceOriginalPasswd()

    def _install_config(self, ssh_port):
        # generate ssh port configuration
        sshd_config = [line.strip() for line in st.read_file(st.SSHD_CONFIG)
                       if line[0:5] != 'Port ']
        sshd_config.append('Port %s\n' % str(ssh_port))
        st.write_file('\n'.join(sshd_config), st.SSHD_CONFIG, mode='w')
        avalon.info("SSH Port successfully set to " + str(ssh_port))
        os.system("service ssh restart")
