from chopsticks.group import Group
from chopsticks.facts import ip

from to_compute import uptime

NODES_FILE_PATH = 'nodes.txt'

addrs = open(NODES_FILE_PATH).read().splitlines()
group = Group(addrs)

for host, addr in group.call(uptime).iteritems():
    print('%s ip:' % host, addr)
