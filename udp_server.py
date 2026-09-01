import socket

HOST = "127.0.0.1"
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
print(f"UDP回声服务端启动 {HOST}:{PORT}")

while True:
    data, addr = s.recvfrom(1024)
    print(f"收到来自{addr}: {data.decode()}")
    s.sendto(data, addr)
