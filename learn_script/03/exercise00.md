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

## whois 정보(json) 검토
추출된 "www.naver.com"의 whois 정보를 보면 json 형식으로 전달되었습니다.
  * [www.naver.com의 whois 정보](./naver_whois.json.md)

사실 조회한 도메인들의 모든 정보가 필요한 것은 아닙니다. 도메인의 국가, 소재지, 주소, 소유자만 필요합니다.
json 데이터에서 일부만 꺼내서 정리해야 합니다. 어떻게 할까요?







