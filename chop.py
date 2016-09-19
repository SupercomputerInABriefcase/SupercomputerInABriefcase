from chopsticks.group import Group
from chopsticks.facts import ip

from to_compute import uptime

NODES_FILE_PATH = 'nodes.txt'

addrs = open(NODES_FILE_PATH).read().strip().splitlines()
group = Group(addrs)

def run_on_nodes(func):
    for host, result in group.call(func).iteritems():
        print('%s result:' % host, result)

run_on_nodes(uptime)
