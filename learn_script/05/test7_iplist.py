"""
지정한 대역에 해당하는 IPv4 주소를 구한다.
"""
import ipaddress


for addr in ipaddress.IPv4Network('61.82.88.0/28'):
    print('IP: {}'.format(addr))