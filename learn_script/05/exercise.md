---
layout: default
---
# 정규식 활용

## 1.Python으로 문자열 데이터에 2018년도의 날짜 데이터가 있는지 체크

[보기](./exercise01.md) [(test1_regex.py 다운로드)](./test1_regex.py)

---------------------------

## 2.정규식 활용 - search() vs match() vs findall()

[보기](./exercise02.md) [(test2_regex.py 다운로드)](./test2_regex.py)

---------------------------

## 3.정규식 컴파일

[보기](./exercise03.md) [(test3_regex.py 다운로드)](./test3_regex.py)

---------------------------

## 4.정규식 컴파일

[보기](./exercise04.md) [(test4_regex.py 다운로드)](./test4_regex.py)

---------------------------

## 5.정규식 컴파일

[보기](./exercise05.md) [(test5_regex.py 다운로드)](./test5_regex.py)

---------------------------
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