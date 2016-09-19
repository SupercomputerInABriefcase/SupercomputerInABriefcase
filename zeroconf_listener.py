#!/usr/bin/env python3

import ipaddress

from six.moves import input
from zeroconf import ServiceBrowser, Zeroconf

NODES_FILE_PATH = './nodes.txt'

def append_ip_to_nodes_file(ip):
    with open(NODES_FILE_PATH, 'r+') as f:
        ips = f.read().splitlines()
        if ip not in ips:
            f.write('{}\n'.format(ip))

class MyListener(object):

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        """This gets called for services discovered.

        Example:

        Service SupercomputerInABriefcase on tom-xps._sciabc._tcp.local. added,
        service info:
            ServiceInfo(
                type='_sciabc._tcp.local.',
                name='SupercomputerInABriefcase on tom-xps._sciabc._tcp.local.',
                address=b'\n\xb7\xcd\xb6',
                port=34343,
                weight=0,
                priority=0,
                server='tom-xps.local.',
                properties={}
            )
        """
        info = zeroconf.get_service_info(type, name)
        print("Service %s added, service info: %s" % (name, info))
        ip = ipaddress.ip_address(info.address)
        append_ip_to_nodes_file(str(ip))


zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_sciabc._tcp.local.", listener)
try:
    input("Press Ctrl-C to exit...\n\n")
except KeyboardInterrupt:
    print('Exiting.')
finally:
    zeroconf.close()
