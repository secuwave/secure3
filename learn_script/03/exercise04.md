## whois 조회 - json 데이터에서 필요한 부분만 출력2. 주소('address') 항목에 값이 없으면 대체값('')을 읽는다.


달라진 부분은 다음 부분입니다. 다른 곳은 똑같습니다. 

위 두줄이 이전 스크립트이고, 아래 두 줄이 없을 때 대체값을 구해 넣는 스크립트입니다.

```python
 # owner_address = dict_data.get('address')
 # owner_zipcode = dict_data.get('zipcode')
 owner_address = dict_data.get('address', dict_data.get('registrant_address'))
 owner_zipcode = dict_data.get('zipcode', dict_data.get('registrant_zip'))
```


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

for address in new_todo_list: #리스트 요소들에 대한 whois 조회 및 결과 출력
    print("check address = [{}]".format(address))
    if len(address): # address 길이가 0보다 크면 whois 조회
        ret = whois_check(address)
        dict_data = json.loads(ret) # json 문자열 데이터를 딕셔너리 데이터로 변환, 이후 key로 액세스가능

        print("- country: {}".format(dict_data.get('country')))
        print("- city: {}".format(dict_data.get('city')))
        # owner_address = dict_data.get('address')
        # owner_zipcode = dict_data.get('zipcode')
        owner_address = dict_data.get('address', dict_data.get('registrant_address'))
        owner_zipcode = dict_data.get('zipcode', dict_data.get('registrant_zip'))
        print("- address: {} (zip:{})".format(owner_address, owner_zipcode))
        print("- city: {}".format(dict_data.get('city')))
        print("- organization: {}".format(dict_data.get('org')))
        print("\n")
    else:
        print("- Address is empty. Skip whois check.")

```