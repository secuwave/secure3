# Running Script 1
## 1. 자바스크립트
### 1.1 html 자바스크립트

```html
<!doctype html>
<html>
<head>
    <title>Test</title>
</head>
<body>
    <h1>greeting</h1>
</body>
<script>
    birthday_member = "오픈베이스"
    member = prompt("이름을 입력하세요: ");
    if (member == birthday_member) {
        alert(member + "님 생일축하합니다!");
    }
    else {
        alert(member + "님 반갑습니다!");
    }
</script>
</html>

```
### 1.2 자바스크립트 파일

```html
<!doctype html>
<html>
<head>
    <title>Test</title>
</head>
<body>
    <h1>greeting</h1>
</body>
<script src="greeting.js"></script>
<!-- 
<script>
    birthday_member = "오픈베이스"
    member = prompt("이름을 입력하세요: ");
    if (member == birthday_member) {
        alert(member + "님 생일축하합니다!");
    }
    else {
        alert(member + "님 반갑습니다!");
    }
</script>
-- >
</html>
```

**지각하지 않기** and 일 두배로 하기 and `보고잘하기` ^^
