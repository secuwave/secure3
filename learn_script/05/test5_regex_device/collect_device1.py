# -*- encoding: utf-8 -*-

import re

"""
아래의 스크립트는 
input.txt의 내용을 줄단위로 읽어서 
'\\통합\\(.+)\.log' 정규식에 일치하는 경우 그룹1(괄호안)부분만 output1.txt에 쓴다.

즉, '통합' 하위 폴더의 로그 파일 이름에서 확장자 부분을 제거하고 장비 이름만 기록한다.
"""

p = re.compile(r'\\통합\\(.+)\.log')

with open('input.txt', encoding='utf8') as inf:
    with open('output1.txt', 'w') as of:
        for line in inf:
            print(line)
            m = p.search(line)
            if m:
                of.write(m.group(1)+'\n')
