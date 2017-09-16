import inspect
import os
import sys
import avalon as av

class Install:
	def __init__ (self, install_location):
		self.install_location = install_location
		self._installed = {
			'iptables': False,
			'arptables': False,
			'rkhunt': False,
			'tripwire': False,
			'passwdcmplx': False,
			'config': False
			}

	def install (self):
		# run all the required installations
		# TODO: allow user to choose which parts they want installed
		self._install_iptables()
		self._install_arptables()
		self._install_rkhunt()
		self._install_tripwrire()
		self._install_passwdcmplx()
		self._install_config()

	def uninstall (self):


	def _install_iptables (self):


	def _install_arptables (self):
		# check arptables installation
		if not (os.path.isfile('/usr/bin/arptables')
				or os.path.isfile('/sbin/arptables')):
			# alert user
			print(av.FM.BD + av.FG.R + 'We have detected that you ' +
				'don\'t have arptables installed!' + av.FM.RST)
			print('This is required for installation')
			if av.ask('Install arptables?', True):
				if os.path.isfile('/usr/bin/apt'):
					os.system('apt update && apt install arptables -y')
				elif os.path.isfile('usr/bin/yum'):
					os.system('yum install arptables -y')
				elif os.path.isfile('usr/bin/pacman'):
					os.system('pacman -S arptables --noconfirm')
				else:
					av.error('Sorry, we can\'t find a package manager ' +
						'that we currently support. Aborting... ' +
						'(apt, yum, pacman are currently supported)')
					self._abort()

	def _install_rkhunt (self):


	def _install_tripwire (self):

	def _install_passwdcmplx (self):

	def _install_config (self):

	def _abort (self):
		for method in self._installed:
			if method:

		sys.exit(0)
		exit(0)



