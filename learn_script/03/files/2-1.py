#!/usr/bin/python

result = []
for i in range (0, 20):
    print("current number = {}".format(i))
    if i%4 == 0:
        print("4의 배수 발견: {}".format(i))
        result.append(i)