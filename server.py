import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8888
server_socket.bind((host, port))
server_socket.listen(1)
print(f"回声服务器启动，监听 {host}:{port}")

conn, addr = server_socket.accept()
print(f"客户端已连接：{addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    msg = data.decode("utf‑8")
    print(f"收到消息：{msg}")
    conn.send(data)

conn.close()
server_socket.close()
