from chopsticks.tunnel import Tunnel
from chopsticks.facts import ip

tun = Tunnel('pi@192.168.3.4')

print('%s ip:' % tun.host, tun.call(ip))
