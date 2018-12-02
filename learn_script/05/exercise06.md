## 방화벽 로그에서 IP 주소만 찾아 변경하기

아래의 스크립트는 traffic log를 줄단위로 읽어서 

모든 ip 주소를 'vvv.vvv.vvv.vvv'로 변경한다.

- 입력: [forwardTrafficLog.Log](./test6_regex_ip/forwardTrafficLog.log)

```python
import re


p = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')

with open('forwardTrafficLog.Log', encoding='utf8') as inf:
    with open('output.dat', 'w') as of:
        for line in inf:
            print(line)
            new_line = p.sub('vvv.vvv.vvv.vvv', line)
            of.write(new_line)
```
- 결과: [output.dat](./test6_regex_ip/output.dat)