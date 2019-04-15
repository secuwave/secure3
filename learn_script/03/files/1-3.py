#!/usr/bin/python

import os

# 환경변수중 PATH를 구한다.
system_path = os.environ['PATH']
print("path 환경변수: {}".format(system_path))

# 현재 스크립트를 실행하는 위치를 구한다.
current_path = os.getcwd()
print("현재 경로: {}".format(current_path))