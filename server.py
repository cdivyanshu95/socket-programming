import socket

print("1 Hello I'm Server")
host='192.168.0.105'
port=7888

server=socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)

while True:
    communication_socket,address=server.accept()
    print(f"connected to {address}")
    message=communication_socket.recv(1024).decode('utf-8')
    print(f"your message {message}")
    communication_socket.send("Got your message Thanks".encode('utf-8'))
    communication_socket.close()
    print(f"connection terminated to {address} !")
