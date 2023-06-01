import socket

ip = "192.168.11.214"
port = 5555

def receive_message(ip,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))

message = "aaaalmila!"
sock.sendall(message.encode())

sock.close()

while True:
    receive_message(ip, port)