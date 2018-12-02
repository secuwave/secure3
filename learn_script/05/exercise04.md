## 정규식 group의 활용: 일치된 파트 중 특정 부분 추출

사용할 정규식의 컴파일
아래와 같이 정규식과 문자열을 파라미터로 매번 넘겨줘서 정규식 매칭을 검사할 수 있지만, 
한가지 정규식이 여러번 반복 사용된다면 한번 컴파일 하여 사용하는 것이 편리하다.
- re.search('\d+', '123456abcdefg')
- re.match('\d+', '123456abcdefg')
- re.findall('\d+', test_string)

```python
import re


dummy_string = '12.aaabbcccdream333-taa(20181203-001)'

# 컴파일하지 않는 예
regex = r'\d{3,4}'  #3~4자리의 숫자
m = re.search(regex, dummy_string)
print('search m = {}'.format(m))

m = re.findall(regex, dummy_string)
print('findall m = {}'.format(m))

# 정규식 컴파일
p = re.compile(regex)

m = p.search(dummy_string)
print('(compile) search m = {}'.format(m))

m = p.findall(dummy_string)
print('(compile) findall m = {}'.format(m))
```