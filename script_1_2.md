# Running Script 1
## 1. 자바스크립트
### 1.2 Base64 

```html
<!doctype html>
<html>
<head>
    <title>Test2</title>
</head>
<body>
<form id="testform">
    ASCII: <input type="text" name="ascii">
    <input type="button" value="Base64 변환" onclick="convert2Base64()"></input>
    <br>
    Base64: <input type="text" name="base64">
</form>
</body>
<script type="text/javascript">
function convert2Base64()
{
    result = window.btoa(document.forms["testform"]["ascii"].value)
    document.forms["testform"]["base64"].value = result;
}
</script>
</html>
```

