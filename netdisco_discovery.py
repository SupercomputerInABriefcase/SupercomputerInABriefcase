#!/usr/bin/env python
# This script is taken from https://github.com/home-assistant/netdisco and is under the MIT license.

import time
from netdisco.discovery import NetworkDiscovery

netdis = NetworkDiscovery()

netdis.scan()

for dev in netdis.discover():
	    print(dev, netdis.get_info(dev))

	    netdis.stop()
