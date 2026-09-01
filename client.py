import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 8888

client_socket.connect((host, port))
msg = "hello dream lab！测试TCP回声"
client_socket.send(msg.encode("utf‑8"))

res = client_socket.recv(1024)
print(f"服务器返回：{res.decode('utf‑8')}")

client_socket.close()
