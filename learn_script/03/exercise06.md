## whois 조회 6 - 파일로 수집한 정보 출력

다음은 출력 파일을 오픈하는 부분입니다.

```python
 with open('whois.dat', 'w') as output_file:
```

### 전체 코드
```python
# -*- encoding: utf-8 -*-

# whois 조회에 이용할 python module을 import
import whois


# address를 받아서 whois 조회 결과를 되돌려주는 함수 정의
def whois_check(address):
    result = whois.whois(address)
    return str(result)


with open('domain_input.txt', 'r', encoding='utf8') as input_file:
    with open('whois.dat', 'w') as output_file:
        for line in input_file:
            line = line.strip()
            print("check address = [{}]".format(line))  # 진행 상황을 보기 위해 화면에도 도메인 이름 정도는 출력
            output_file.write("check address = [{}]".format(line)) # 파일에 도메인 이름을 기록
            if len(line):  # address 길이가 0보다 크면 whois 조회
                ret = whois_check(line)
                output_file.write(ret)
                output_file.write("-------------------------------------\n")
            # else:
            #     print("- Address is empty. Skip whois check.\n")
```