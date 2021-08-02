import pandas as pd
import socket 

s = socket.socket()
port = 5003
host = socket.gethostname()
s.bind((host,port))
s.listen(3)
file = open("C:/Users/RASWANTH.SR/Desktop/temp.csv","r")
data = file.read()
print("Server Running ...")
while True:
    conn,addr = s.accept()
    print("Connected with ",addr)
    conn.send(data.encode("utf-8","ignore"))
conn.close()