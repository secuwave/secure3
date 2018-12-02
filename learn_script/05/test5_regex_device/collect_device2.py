# -*- encoding: utf-8 -*-

import re

"""
아래의 스크립트는 
input.txt의 내용을 줄단위로 읽어서 
'\((.+)@[\w\.]+]\)\\통합\\(.+)\.log' 정규식에 일치하는 경우 그룹1(이메일의 계정 부분), 그룹2(로그파일의 장비 이름 부분)을 output2.csv에 쓴다.

즉, 관리자 계정(이메일에서 계정 이름 추출)과 '통합' 하위 폴더의 로그 파일 이름에서 장비 이름을 구해서 csv파일로 정리한다.
"""

p = re.compile(r'\((.+)@[\w\.]+\)\\통합\\(.+)\.log')

with open('input.txt', encoding='utf8') as inf:
    with open('output2.csv', 'w') as of:
        for line in inf:
            print(line)
            m = p.search(line)
            if m:
                of.write(m.group(1) + ',' + m.group(2) + '\n')
