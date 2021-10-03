import socket
import pandas as pd
df = open('D:/Study/Networking/Evaluation_1/calldrop_set3 (1).csv')
data = df.read()
s= socket.socket()
print("Server starting up.")
s.bind(('127.0.0.1',5001))
s.listen(3)
while True:
    c,addr = s.accept()
    print("Server address: ", addr)
    c.send(bytes(data,'utf8'))
