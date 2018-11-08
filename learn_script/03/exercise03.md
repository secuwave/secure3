## whois 조회 - 불필요 문자 제거

```python
# -*- encoding: utf-8 -*-

# whois 조회에 이용할 python module을 import
import whois
import json

# address를 받아서 whois 조회 결과를 되돌려주는 함수 정의
def whois_check(address):
    result = whois.whois(address)
    return str(result)


# whois 정보를 조회할 도메인들의 목록
order1 = "www.naver.com,  , ,www.google.com,     ,www.openbase.co.kr,www.daum.net,www.seoul.go.kr,www.seoul.go.kr"

order2 = order1.replace(' ', '')  # 목록에서 space를 제거
todo_list = order2.split(',')  # 도메인 목록을 ,로 잘라서 리스트 자료형으로 만듦
new_todo_list = set(todo_list)  # 리스트 자료형을 집합(set)으로 변환해서 중복요소를 제거

for address in new_todo_list: #리스트 요소들에 대한 whois 조회 및 결과 출력
    print("check address = [{}]".format(address))
    if len(address): # address 길이가 0보다 크면 whois 조회
        ret = whois_check(address)
        dict_ret = json.loads(ret)
    else:
        print("Address is empty. Skip whois check.")

```