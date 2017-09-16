#!/usr/bin/python3

import os
import sys


def get_package_manager (manager):
	if os.path.isfile('/usr/bin/%s' % manager.strip()):
		return True
	return False


def gen_pack_install (manager, packs):
	if manager not in valid_managers.keys():
		return False
	if manager == 'apt':
		return 'apt install %s -y' % packs
	elif manager == 'yum':
		return 'yum install %s -y' % packs
	elif manager == 'pacman':
		return 'pacman -S %s --noconfirm' % packs


def gen_pack_remove (manager, packs):
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
