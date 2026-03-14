import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost",11111))
print(client.recv(1024).decode())
client.close()