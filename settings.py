#!/usr/bin/python3

import os

# ------global variables------

# filepaths
CONFPATH = '/etc/DefenseMatrix.conf'
INSTALLPATH = '/usr/share/DefenseMatrix'
SSHD_CONFIG = '/etc/ssh/sshd_config'

# configuration variables
required_packages = ['ufw', 'iptables', 'arptables']
installed_packages = []


def write_file(data, filename, mode='wb'):
    if not os.path.exists(filename):
        os.system('touch %s' % filename)
    with open(filename, mode) as fname:
        fname.writelines(data)


def read_file(filename, mode='r'):
    content = []
    with open(filename, mode) as fname:
        for line in fname:
            content.append(line)

    return content


def get_ifaces():
    return [line.split(':')[0] for line in read_file('/proc/net/dev')
            if line.split(':')]


def get_package_manager(manager):
    if os.path.isfile('/usr/bin/%s' % manager.strip()):
        return True
    return False


def gen_pack_install(manager, packs):
    if manager not in valid_managers.keys():
        return False
    if manager == 'apt':
        return 'apt install %s -y' % packs
    elif manager == 'yum':
        return 'yum install %s -y' % packs
    elif manager == 'pacman':
        return 'pacman -S %s --noconfirm' % packs


def gen_pack_remove(manager, packs):
    if manager not in valid_managers.keys():
        return False
    if manager == 'apt':
        return 'apt autoremove %s -y' % packs
    elif manager == 'yum':
        return 'yum remove %s -y' % packs
    elif manager == 'pacman':
        return 'pacman -R %s --noconfirm' % packs


valid_managers = {
    'apt': get_package_manager('apt'),
    'yum': get_package_manager('yum'),
    'pacman': get_package_manager('pacman')
}

package_manager = [man for man in valid_managers.keys() if valid_managers[man]][0]
ifaces = get_ifaces(
    )