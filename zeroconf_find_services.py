#!/usr/bin/python3
from zeroconf import ZeroconfServiceTypes
print('\n'.join(ZeroconfServiceTypes.find()))
