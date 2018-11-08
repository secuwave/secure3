## whois 조회 7 - csv 리포트 파일 작성

보고 싶은 항목만 csv로 정리하여 리포팅합니다.

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


NA_string = '-'  # 데이터가 없을때 기록할 문자

with open('domain_input.txt', 'r', encoding='utf8') as input_file:
    with open('whois.csv', 'w') as output_file:
        output_file.write("domain,country,city,address,zipcode,orgnization,admin email\n")  #c sv 첫 줄에 헤더 라인을 씁니다.

        for line in input_file:
            line = line.strip()
            print("check address = [{}]".format(line))  # 진행 상황을 보기 위해 화면에도 도메인 이름 정도는 출력
            domain = line
            if len(line):  # address 길이가 0보다 크면 whois 조회
                ret = whois_check(line)
                dict_data = json.loads(ret)  # json 문자열 데이터를 딕셔너리 데이터로 변환, 이후 key로 액세스가능

                country = dict_data.get('country', NA_string)

                city = dict_data.get('city', NA_string)

                owner_address = dict_data.get('address', dict_data.get('registrant_address'))
                if not owner_address:
                    owner_address = NA_string

                owner_zipcode = dict_data.get('zipcode', dict_data.get('registrant_zip'))
                if not owner_zipcode:
                    owner_zipcode = NA_string

                owner_org = dict_data.get('org', dict_data.get('registrant_org'))
                if not owner_org:
                    owner_org = NA_string

                admin_email = dict_data.get('admin_email', NA_string)

                output_file.write('"{}","{}","{}","{}","{}","{}","{}"\n'.format(domain, country, city, owner_address, owner_zipcode, owner_org, admin_email))
```