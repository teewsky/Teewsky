import socket

HOST = "127.0.0.1"
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "hello dream lab! 测试UDP回声"
s.sendto(msg.encode(), (HOST, PORT))

data, addr = s.recvfrom(1024)
print(f"服务端返回：{data.decode()}")
s.close()
