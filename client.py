import socket


print("Hello I'm Client")

host='192.168.0.105'
port=7888
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))


message_from_client="Hello Server This is client".encode('utf-8')
client.send(message_from_client)
print(client.recv(1024).decode('utf-8'))


