#!/usr/bin/env python3

import ipaddress
import socket
import sys

from collections import namedtuple

from typing import List, NamedTuple

from scapy.all import srp, Ether, ARP

"""
A script to list the IP addresses of things connected to the network.

Defaulting to 192.168.3.0, but specifiable on the command line, list the IP addresses of things active on the network.
"""

__author__ = 'Russel Winder'
__copyright__ = 'Copyright © 2016  Russel Winder'
__version__ = '0.0.1'
__date__ = '2016-09-19T06:56+01:00'
__license__ = 'GPLv3'

ConnectionData = NamedTuple('ConnectionData', [('ip_net', str), ('iface', str)])


def process_arguments(args: List[str]) -> ConnectionData:
    assert isinstance(args, list)
    for a in args:
        assert isinstance(a, str)
    if len(args) == 0:
        #rv = ConnectionData(ip_net='192.168.3.0/24', iface='eth0')
        rv = ConnectionData(ip_net='192.168.3.0/24', iface='wlan0')
    elif len(args) == 1:
        rv = ConnectionData(ip_net=args[0], iface='eth0')
    elif len(args) == 2:
        rv = ConnectionData(ip_net=args[0], iface=args[1])
    else:
        print('Incorrect number of arguments.')
        sys.exit(1)
    try:
        ipaddress.ip_network(rv.ip_net)
    except ValueError:
        print("First parameter doesn't appear to be an IP network specification.")
        sys.exit(1)
    return rv


def discover(data: ConnectionData) -> None:
    assert isinstance(data, ConnectionData)
    ip_net, iface = data
    try:
        ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_net), iface=iface, timeout=2, verbose=False)
        for s, r in ans:
            line = r.sprintf("%Ether.src%  %ARP.psrc%")
            try:
                hostname = socket.gethostbyaddr(r.psrc)
                line += '  ' + hostname[0]
            except socket.herror:
                pass
            print(line)
    except PermissionError:
        print('Cannot execute necessary code, did you run as root?')
        sys.exit(1)
    except:
        raise


def main(args):
    discover(process_arguments(args))


if __name__ == '__main__':
    main(sys.argv[1:])
