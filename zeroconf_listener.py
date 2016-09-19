#!/usr/bin/env python3

import ipaddress
import os
from tempfile import NamedTemporaryFile

from six.moves import input
from zeroconf import ServiceBrowser, Zeroconf

NODES_FILE_PATH = 'nodes.txt'


def reset_nodes_file():
    with open(NODES_FILE_PATH, 'w') as f:
        pass

def append_ip_to_nodes_file(ip):
    with open(NODES_FILE_PATH) as f:
        ips = set(f.read().splitlines())
        ips.add(ip)

    with NamedTemporaryFile(mode='w', delete=False) as tmpfile:
        tmpfile.write('\n'.join(sorted(ips)))
        # ensure content is on disk
        tmpfile.flush()
        os.fsync(tmpfile.fileno())

    os.rename(tmpfile.name, NODES_FILE_PATH)


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


if __name__ == '__main__':
    zeroconf = Zeroconf()
    listener = MyListener()
    browser = ServiceBrowser(zeroconf, "_sciabc._tcp.local.", listener)

    reset_nodes_file()

    try:
        input("Press Ctrl-C to exit...\n\n")
    except KeyboardInterrupt:
        print('Exiting.')
    finally:
        zeroconf.close()
