#!/usr/bin/python3

from iptables import ufw
import avalon_framework as avalon
import sys

try:
    ports = []
    for port in sys.argv[1:]:
        ports.append(int(port))
    for port in ports:
        ufw.allow(port)
except ValueError:
    avalon.error("Not a valid port number!")
