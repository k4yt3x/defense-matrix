import os
import subprocess


def __init__(self, interface):
    self.interface = interface


def getDefaultRule(self):
    """
    Checks if the default rule of iptables is ACCEPT or DROP
    """
    cout = subprocess.Popen(["iptables", "-L"], stdout=subprocess.PIPE).communicate()[0]
    coutparsed = cout.decode().split('\n')
    for line in coutparsed:
        if "Chain INPUT (policy DROP)":
            return True
    return False


def allow(address, port):
    """
    Accept all traffic from one address

    Arguments:
        address {string} -- Address of target machine
        port {int} -- Port number
    """
    os.system("iptables -A INPUT -p tcp --source " + address + " --sport " + port + " -j ACCEPT")


def expire(address):
    """
    Disallows all traffic from one address

    Arguments:
        address {string} -- Address of target machine
    """
    output = subprocess.Popen(['iptables', '-nL', '--line-numbers'], stdout=subprocess.PIPE).communicate()[0]
    output = output.decode().split('\n')
    for line in output:
        if address in line:
            os.system('iptables -D INPUT ' + line.split(' ')[0])
