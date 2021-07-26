
import socket               

s = socket.socket()         

port = 12345               

s.connect(('127.0.0.1', port))


input_string = input("Enter data you want to send->")
s.sendall(bytes(input_string,'utf-8'))

print(s.recv(1024).decode())

s.close()