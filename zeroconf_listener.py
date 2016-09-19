#!/usr/bin/env python

from six.moves import input
from zeroconf import ServiceBrowser, Zeroconf


class MyListener(object):

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        """This get's called for services discovered.

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


zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_sciabc._tcp.local.", listener)
try:
    input("Press enter to exit...\n\n")
finally:
    zeroconf.close()
