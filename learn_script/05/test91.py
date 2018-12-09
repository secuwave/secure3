
try:
    with open('test91.py', 'r', encoding='utf8') as f:
        for line in f:
            print(line.strip())
except Exception as e:
    print("에러메지시: {}".format(e))


try:
    with open('test91.py', 'r', encoding='utf8') as f:
        f.write("aaaaaa")
except Exception as e:
    print("에러메지시: {}".format(e))
    