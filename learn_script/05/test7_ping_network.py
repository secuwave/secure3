
import ipaddress
import subprocess
import re

p = re.compile(r'응답\:\s(.+)')

for addr in ipaddress.IPv4Network('61.82.88.0/28'):
    # print('test ping {}'.format(addr))
    ping_response = subprocess.Popen(["ping", str(addr), "-n", '1'], stdout=subprocess.PIPE, universal_newlines=True).stdout.read()
    # print(ping_response)

    m = p.search(ping_response)
    if m:
        print('{}: up({})'.format(str(addr), m.group(1)))
    else:
        print('{}: down'.format(str(addr)))