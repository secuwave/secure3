import re


"""
정규식 매칭된 부분 가져오기
* grup(): 정규식에 일치한 파트 전체
* group(n): n번째 일치된 그룹. 0번째는 일치된 파트 전체
"""

# 문자열에서 주최한 회사, 세미나 이름, 장소, 날짜만 뽑는 정규식. 
# 괄호를 이용해서 정규식의 group을 지정해 원하는 파트별로 뽑을 수 있다.
dummy = 'Openbase-CyberSecuritySeminar At Koex 2018.12.03 - Speaker: Richard'
p = re.compile(r'^(.+)-(.+)Seminar At (.+) ([\d\.]{10})')
m = p.search(dummy)
print('match group() = %s  ' % m.group())
print('match group(0) = %s  ' % m.group(0))
print('match group(1) = %s  ' % m.group(1))
print('match group(2) = %s  ' % m.group(2))
print('match gruop(3) = %s  ' % m.group(3))
print('match gruop(4) = %s  ' % m.group(4))