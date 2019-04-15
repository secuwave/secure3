## 지정한 네트워크 대역의 호스트들에 ping 체크하기

지정한 대역에 해당하는 IPv4 주소를 구한다.

```python
import ipaddress


for addr in ipaddress.IPv4Network('61.82.88.0/28'):
    print('IP: {}'.format(addr))
```
출력:
```
IP: 61.82.88.0
IP: 61.82.88.1
IP: 61.82.88.2
IP: 61.82.88.3
IP: 61.82.88.4
IP: 61.82.88.5
IP: 61.82.88.6
IP: 61.82.88.7
IP: 61.82.88.8
IP: 61.82.88.9
IP: 61.82.88.10
IP: 61.82.88.11
IP: 61.82.88.12
IP: 61.82.88.13
IP: 61.82.88.14
IP: 61.82.88.15
```

네트워크의 IP들에 대해 ping 상태를 체크한다. 

ping 명령 실행에는 subprocess 모듈을 이용하고, 

ping 결과에서 호스트 up/down을 정규식으로 확인한다.

```python
import ipaddress
import subprocess
import re

p = re.compile(r'응답\:\s(.+)')

for addr in ipaddress.IPv4Network('61.82.88.0/28'):
    # print('test ping {}'.format(addr))
    ping_response = subprocess.Popen(["ping", str(addr), "-n", '1'], 
           stdout=subprocess.PIPE, universal_newlines=True).stdout.read()
    # print(ping_response)

    m = p.search(ping_response)
    if m:
        print('{}: up({})'.format(str(addr), m.group(1)))
    else:
        print('{}: down'.format(str(addr)))
```
출력:
```
61.82.88.0: down
61.82.88.1: up(바이트=32 시간=7ms TTL=46)
61.82.88.2: down
61.82.88.3: down
61.82.88.4: down
61.82.88.5: down
61.82.88.6: up(바이트=32 시간=13ms TTL=45)
61.82.88.7: down
61.82.88.8: down
61.82.88.9: down
61.82.88.10: up(바이트=32 시간=6ms TTL=233)
61.82.88.11: down
61.82.88.12: down
61.82.88.13: down
61.82.88.14: down
61.82.88.15: up(바이트=32 시간=8ms TTL=236)
```