---
layout: default
---

## 지난 시간 내용 요약

지난 시간 실습으로 도메인의 whois 조회를 다음과 같은 순서로 했습니다.

1. whois 조회에 필요한 Python 모듈 python-whois 설치: 명령 "pip install python-whois"
2. Python 콘솔에서 직접 "www.naver.com" whois 조회
3. whois 조회 스크립트 작성. 반복 호출할 부분은 함수로 구성.
4. comma(,)로 구분된 도메인 리스트를 받아서 각 도메인별로 whois 정보 추출 반복
5. whois 정보를 추출할 도메인 리스트에서 중복된 도메인이 있으면 하나만 남기고 제거
  * [여기까지 결과 보기](./exercise01.md)


## 남은 문제
whois 조회할 도메인 리스트에 불필요하게 들어간 space가 있으면(아래와 같이) 어떻게 처리 할까요?
  * 문제의 도메인 리스트: 
```json
"www.naver.com,  , ,www.google.com,     ,www.openbase.co.kr,
 www.daum.net,www.seoul.go.kr,www.seoul.go.kr"
```
  * [결과 보기](./exercise02.md)

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

'domain_input.txt'에 도메인 목록이 다음과 같은 도메인이 70개 들어 있습니다.
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
