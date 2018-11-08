## whois 조회 - 불필요 문자 제거

### 방법
1. replace() 함수를 써서 order1의 빈 문자(space)를 제거하고 order2로 저장합니다.
2. order2를 입력 도메인리스트로 줘서 whois 정보 조회를 합니다.

### 참고
* 아래 예를 실행하면 "Address is empty. Skip whois check."가 한번 찍힙니다. space가 제거되면서 ",,"으로 변한 부분이 있기 때문입니다.


```python
# -*- encoding: utf-8 -*-

# whois 조회에 이용할 python module을 import
import whois

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
        print("whois result = {}".format(ret))
    else:
        print("Address is empty. Skip whois check.")

```