#!/usr/bin/python

import os

# ȯ�溯���� PATH�� ���Ѵ�.
system_path = os.environ['PATH']
print("path ȯ�溯��: {}".format(system_path))

# ���� ��ũ��Ʈ�� �����ϴ� ��ġ�� ���Ѵ�.
current_path = os.getcwd()
print("���� ���: {}".format(current_path))