## whois 조회 5- 파일로 도메인 목록 입력

다음은 파일을 읽으면서 달라진 부분입니다.

```python
with open('domain_input.txt', encoding='utf8') as input_file:
    for line in input_file:
        line = line.strip()
```

### 전체 코드
```python
# -*- encoding: utf-8 -*-

# whois 조회에 이용할 python module을 import
import whois
import json


# address를 받아서 whois 조회 결과를 되돌려주는 함수 정의
def whois_check(address):
    result = whois.whois(address)
    return str(result)


with open('domain_input.txt', encoding='utf8') as input_file:
    for line in input_file:
        line = line.strip()
        print("check address = [{}]".format(line))
        if len(line):  # address 길이가 0보다 크면 whois 조회
            ret = whois_check(line)
            dict_data = json.loads(ret)  # json 문자열 데이터를 딕셔너리 데이터로 변환, 이후 key로 액세스가능

            print("- country: {}".format(dict_data.get('country')))
            print("- city: {}".format(dict_data.get('city')))

            owner_address = dict_data.get('address', dict_data.get('registrant_address'))
            owner_zipcode = dict_data.get('zipcode', dict_data.get('registrant_zip'))
            print("- address: {} (zip:{})".format(owner_address, owner_zipcode))

            owner_org = dict_data.get('org', dict_data.get('registrant_org'))
            print("- organization: {}".format(owner_org))

            print("- admin email: {}".format(dict_data.get('admin_email')))
            print("\n")
        else:
            print("- Address is empty. Skip whois check.\n")

```