import re


"""
정규식의 활용
1. re.match() - 문자열의 처음위치부터 정규식과 일치 여부를 검사한다. 따라서 일치하는 부분이 문자열 중간에 나오면 매칭되지 않음으로 판단한다.
2. re.search() - 문자열의 모든 영역에서 정규식과 일치 여부를 검사한다.
3. re.findall() - match(), search()는 일치 여부 확인에 중점을 두므로 일단 매치되는 1건을 확인하고 끝난다. findall()은 모든 일치하는 부분을 검색한다.
"""

dummy_string = '12.aaabbcccdream333-taa(20181203-001)'

print('---------------------')
print('문자열 "{}"에서 정규식 "\\d+" 일치를 테스트\n'.format(dummy_string))
m = re.match(r'\d+', dummy_string)  # \d+ : 숫자. 1, 11, 234555 ...
print('match m = {}'.format(m))

m = re.search(r'\d+', dummy_string)
print('search m = {}'.format(m))

m = re.findall(r'\d+', dummy_string)
print('findall m = {}'.format(m))

print('---------------------')
regex = r'a+'  # a+ : a로만 이뤄진 길이 1개 이상의 문자열: a, aa, aaa, aaaa ....
print('문자열 "{}"에서 정규식 "{}" 일치를 테스트\n'.format(dummy_string, regex))

m = re.match(regex, dummy_string)
print('match m = {}'.format(m))

m = re.search(regex, dummy_string)
print('search m = {}'.format(m))

m = re.findall(regex, dummy_string)
print('findall m = {}'.format(m))

for i in m:
    print('matched item: {}'.format(i))