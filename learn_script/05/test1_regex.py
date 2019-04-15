import re


"""
정규식의 활용
- 2018로 시작하는 8자리 숫자가 있는지 존재 여부 확인
"""

dummy_string1 = 'aaabbccc dream (20181203-001)'
dummy_string2 = 'serial-987620181203001'

# test1
m  = re.search(r'\D2018\d{4}\D', dummy_string1)
if m:
    print('"{}" matched'.format(dummy_string1))
else:
    print('"{}" not matched'.format(dummy_string1))

# test2
m  = re.search(r'\D2018\d{4}\D', dummy_string2)
if m:
    print('"{}" matched'.format(dummy_string2))
else:
    print('"{}" not matched'.format(dummy_string2))