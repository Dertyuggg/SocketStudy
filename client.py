import socket
s= socket.socket()
s.connect(('localhost',9000))
print("Client Socket:",s.getsockname)
data= s.recv(1024).decode()
print("Server Date & Time:",data)
s.send("Acknowledgement received from client".encode())
s.close()