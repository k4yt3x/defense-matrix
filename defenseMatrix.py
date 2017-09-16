"""
Name: K4YT3X
      Fa11en
Date Created: SEP 16, 2017
Last Modified: SEP 16, 2017

Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt

(C) 2016 - 2017 K4YT3X
(C) 2017 fa11en

"""
import os
import urllib.request

# Import Controller Packages
from iptables import iptables
from arptables import arptables


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


def installWizard():
    print(avalon.FG.G + avalon.FM.BD + "Welcome to DefenseMatrix!")
    print("This is the setup wizard")
    print("You will be asked to answer basic questions about your server")

    serverTypes = [
    "Web Server",
    "Mail Server",
    "Minecraft PC Server",
    ]

    for index in len(serverTypes):
        print(index + ". " + serverTypes[index - 1])

    while True:
        serverSelection = avalon.gets("Which type of server it this?")
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

    ifacesSelected = []
    while True:
        print(avalon.FM.BD + '\nWhich interface do you wish to install for?' + avalon.FM.RST)
        ifaces = []
        with open('/proc/net/dev', 'r') as dev:
            for line in dev:
                try:
                    if line.split(':')[1]:
                        ifaces.append(line.split(':')[0])
                except IndexError:
                    pass
        if not len(ifaces) == 0:
            idx = 0
            for iface in ifaces:
                print(str(idx) + '. ' + iface.replace(' ', ''))
                idx += 1
        print('99. Manually Enter')
        selection = avalon.gets('Please select (index number): ')

        try:
            if selection == '99':
                manif = avalon.gets('Interface: ')
                if manif not in ifacesSelected:
                    ifacesSelected.append(manif)
                if avalon.ask('Add more interfaces?', False):
                    pass
                else:
                    break
            elif int(selection) >= len(ifaces):
                avalon.error('Selected interface doesn\'t exist!')
            else:
                ifacesSelected.append(ifaces[int(selection)].replace(' ', ''))
                if avalon.ask('Add more interfaces?', False):
                    pass
                else:
                    break
        except ValueError:
            avalon.error('Invalid Input!')
            avalon.error('Please enter the index number!')

    avalon.info("DefenseMatrix takes care of your firewall settings for you")
    avalon.warning("This following step is going to reset your iptables configuration")
    if not avalon.ask("Is is okay to proceed right now?", True):
        exit(0)

    ifaceobjs_iptables = []
    ifaceobjs_arptables = []

    for interface in ifacesSelected:
        iptablesobj = iptables(interface)
        ifaceobjs_iptables.append(iptablesobj)
        arptablesobj = arptables(interface)
        ifaceobjs_arptables.append(arptablesobj)

    for iface in ifaceobjs_iptables:
        for port in portsOpen:
            iface.allow(port)

    avalon.info("It is " + avalon.FM.BD + "HIGHLY recommended to change your default port for ssh")
    if avalon.ask("Do you want to change it right now?", True):
        while True:
            port = avalon.gets("Which port do you want to change to?")
            if len(port) != 0:
                try:
                    port = int(port)
                    break
                except TypeError:
                    avalon.error("Please enter a valid port number between 1-65565!")
            else:
                avalon.error("Please enter a valid port number between 1-65565!")
    else:
        avalon.info("You can always change it using the command \"dm --ssh-port [port]\"")


# -------------------------------- Procedural --------------------------------
