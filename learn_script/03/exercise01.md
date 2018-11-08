## whois 조회

```python
# -*- encoding: utf-8 -*-

# whois 조회에 이용할 python module을 import
import whois

# address를 받아서 whois 조회 결과를 되돌려주는 함수 정의
def whois_check(address):
    result = whois.whois(address)
    return str(result)


# whois 정보를 조회할 도메인들의 목록
order="www.naver.com,www.google.com,www.openbase.co.kr,www.daum.net,www.seoul.go.kr,www.seoul.go.kr,www.seoul.go.kr"

todo_list = order.split(',')  # 도메인 목록을 ,로 잘라서 리스트 자료형으로 만듦
new_todo_list = set(todo_list)  # 리스트 자료형을 집합(set)으로 변환해서 중복요소를 제거

for address in new_todo_list: #리스트 요소들에 대한 whois 조회 및 결과 출력
    ret = whois_check(address)
    print(ret)

```