# -*- encoding: utf-8 -*-

import re

"""
아래의 스크립트는 
traffic log를 줄단위로 읽어서 
ip 주소를 그 앞의 정보를 포함해서 추출한다.

"""

p = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')

with open('forwardTrafficLog.Log', encoding='utf8') as inf:
    with open('output.txt', 'w') as of:
        for line in inf:
            print(line)
            new_line = p.sub('vvv.vvv.vvv.vvv', line)
            of.write(new_line)
