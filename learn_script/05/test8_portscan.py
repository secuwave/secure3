
#!/usr/bin/env python
import socket
import sys
from datetime import datetime

# 스캔할 호스트 입력받기
remote_host    = input("스캔할 호스트 네임(IP): ")
remote_host_ip  = socket.gethostbyname(remote_host)

# "스캔중...." 프린트
print("-" * 60)
print("스캔중.... Host address: ", remote_host_ip)
print("-" * 60)

# 스캔 시작시간 저장. 스캔 소요시간 계산에 이용
t1 = datetime.now()

# 스캔할 포트(범위)를 지정한다.
# port_range = range(1,1025) # 1~1024
# port_range = range(1,101) # 1~100
port_range = [21,22,80,111,443,512,8080]

# 에러의 catch를 위해 try... except 적용
try:
    for port in port_range:  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.4)
        result = sock.connect_ex((remote_host_ip, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        sock.close()
except KeyboardInterrupt:
    print("Ctrl+C 입력됨")
    sys.exit()

except socket.gaierror:
    print("호스트주소 에러")
    sys.exit()

except socket.error:
    print("호스트에 연결할 수 없음")
    sys.exit()

# 종료시간
t2 = datetime.now()

# 스캔 소요시간 계산
elapsed_time =  t2 - t1

# 스캔 소요시간 프린트
print("스캔 소요시간: ", elapsed_time)