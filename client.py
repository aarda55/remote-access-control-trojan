import socket

HOST = 0 #client-ip
PORT = 65432       

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while(True):
        msg = input("Your command: ")
        s.sendall(str.encode(msg))
        if(msg == "exit"):
            break
        data = s.recv(2048)
        print('Received:\n', data.decode())