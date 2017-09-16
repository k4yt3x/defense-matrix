import socket
import struct
import os
import time


class arptables:

    def __init__(self, interface):
        self.interface = interface

    def getGateway(self):
        """Get Linux Default Gateway"""
        with open("/proc/net/route") as fh:
            for line in fh:
                if self.interface in line:
                    fields = line.strip().split()
                    if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                        continue
                    return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))
        return 0

    def getGatewayMac(self):
        """Get Gateway Mac Address"""
        with open('/proc/net/arp') as arpf:
            for line in arpf:
                if line.split(' ')[0] == arptables.getGateway(self) and self.interface in line:
                    for field in line.split(' '):
                        if len(field) == 17 and ':' in field:
                            return field

    def allowGateway(self):
        """
        This function adds the gateway's mac address into
        arptable's whitelist
        """
        while True:  # Wait Until Gateway ARP is cached
            gatewayMac = str(arptables.getGatewayMac(self))
            # os.system('nslookup google.ca')  # Works as well as the following
            try:
                ac = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ac.settimeout(0)
                # Connect to gateway to cache gateway MAC
                ac.connect((arptables.getGateway(self), 0))
                ac.close()
            except Exception:
                pass
            # Check if it's a valid MAC Address
            if gatewayMac != '00:00:00:00:00:00' and len(gatewayMac) == 17:
                break
            time.sleep(0.5)  # Be nice to CPU
        os.system('arptables --flush')
        os.system('arptables -P INPUT DROP')
        os.system('arptables -A INPUT --source-mac ' + gatewayMac + ' -j ACCEPT')
