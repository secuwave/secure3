## whois 조회 3 - json 데이터에서 필요한 부분만 출력

1. json 모듈을 import 합니다.
2. json 모듈의 loads() 함수로 json 문자열을 딕셔너리 자료형으로 만듭니다. 
```python
 dict_data = json.loads(ret)
```
3. 키로 데이터를 찾아서 출력합니다.


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
order1 = 'www.naver.com,  , ,www.google.com,     ,www.openbase.co.kr,www.daum.net,www.seoul.go.kr,www.seoul.go.kr'

order2 = order1.replace(' ', '')  # 목록에서 space를 제거
todo_list = order2.split(',')  # 도메인 목록을 ,로 잘라서 리스트 자료형으로 만듦
new_todo_list = set(todo_list)  # 리스트 자료형을 집합(set)으로 변환해서 중복요소를 제거

for address in new_todo_list:  # 리스트 요소들에 대한 whois 조회 및 결과 출력
    print("check address = [{}]".format(address))
    if len(address):  # address 길이가 0보다 크면 whois 조회
        ret = whois_check(address)
        dict_data = json.loads(ret)  # json 문자열 데이터를 딕셔너리 데이터로 변환, 이후 key로 액세스가능

        print("- country: {}".format(dict_data.get('country')))
        print("- city: {}".format(dict_data.get('city')))

        owner_address = dict_data.get('address')
        owner_zipcode = dict_data.get('zipcode')
        print("- address: {} (zip:{})".format(owner_address, owner_zipcode))

        owner_org = dict_data.get('org')
        print("- organization: {}".format(owner_org))

        print("- admin email: {}".format(dict_data.get('admin_email')))
        print("\n")
    else:
        print("- Address is empty. Skip whois check.\n")

```