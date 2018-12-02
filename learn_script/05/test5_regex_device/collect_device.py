# -*- encoding: utf-8 -*-

import re

"""
아래의 스크립트는 
input.txt의 내용을 줄단위로 읽어서 변형없이 output.txt에 쓴다.
두 파일의 내용이 같아진다.
"""


with open('input.txt', encoding='utf8') as inf:
    with open('output.txt', 'w') as of:
        for line in inf:
            print(line)
            of.write(line)
