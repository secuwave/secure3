---
layout: default
---
# 정규식 활용

## 특정 조건의 숫자 존재 여부 체크

Python으로 문자열 데이터에 2018년도의 날짜 데이터가 있는지 체크

[exercise 1](./exercise01.md) [(스크립트)](./test1_regex.py)

---------------------------

## 구해진 whois 정보(json) 검토
추출된 whois 데이터는 json 형식으로 표현되어 있습니다. 이 중 "www.naver.com"의 것을 샘플로 보면 아래와 같습니다.
  * [www.naver.com의 whois 정보](./naver_whois.json.md)

## 필요한 정보만 추출
그런데 사실 이 장황한 도메인들의 정보가 모두 필요한 것은 아닙니다.  
도메인의 국가, 소재지, 주소, 소유기관명만 필요합니다.  
json 데이터에서 일부만 꺼내서 정리하려고 합니다. 어떻게 할까요?  
* [결과 보기](./exercise03.md)

그런데, 일부 주소지가 나오지 않는 도메인들이 있습니다.  
이제 보니 주소지가 'address'가 아닌 'registrant_address'항목에 기록된 것들이 있군요.  
organization도 'org'가 아닌 'registrant_org'항목에 있는 경우가 있습니다.  
"'address'에 주소가 없으면 'registrant_address'의 값을 읽어와라" 라고 보강하려면 어떻게 해야 할까요?  
* [결과 보기](./exercise04.md)

---------------------------

## 파일로 입출력 처리

팀장은 원래 도메인 목록을 파일로 줬습니다. 이제 그 파일에서 도메인 목록을 읽어서 whois 정보를 수집하고, 결과도 파일로 정리해보도록 하겠습니다.  
그러면 깔끔하게 보고하기도 쉬울것 같네요.  
입력을 파일에서 읽으면 스크립트의 도메인 목록 부분을 매번 수정할 필요도 없습니다.  
가능한 스크립트는 스크립트의 기능을 바꾸는 경우가 아니라면 수정을 피해야 합니다. 불필요한 수정은 오류를 만들 수 있습니다.  

### 1. 파일에서 도메인 목록 읽기

'domain_input.txt'에 도메인 목록이 다음과 같은 도메인이 60개 들어 있습니다.
한줄에 도메인 하나씩 입니다. 단, 도메인 앞뒤로 스페이스가 있을 수도 있습니다. 
(실제 테스트에는 이 파일을 다운로드해서 사용합니다. [domain_input.txt](./domain_input.txt))

```text
www.naver.com
 www.google.com
www.openbase.co.kr
www.daum.net
www.seoul.go.kr
www.data.go.kr
 www.yes24.com
... 이하생략
```
* [결과 보기](./exercise05.md)

### 2. 결과도 파일에 기록하기

'whois.dat'에 whois 정보를 기록하겠습니다. 필요한 부분만 추출하지 않고 모든 정보를 기록합니다.
* [결과 보기](./exercise06.md)

### 3. 필요한 결과만 정리하여 csv 리포트 작성하기

이번에는 'whois.csv'에 필요한 정보만 기록합니다.  
결과 파일을 열면 엑셀에 잘 정리된 데이터를 볼 수 있습니다.  

* [결과 보기](./exercise07.md)
* [결과 whois.csv 샘플](./whois.csv)