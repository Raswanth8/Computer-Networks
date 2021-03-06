import pandas as pd
import socket
from _thread import *
import threading

print_lock = threading.Lock()

def threaded(c,addr):
    while True:
        data = c.recv(1024)
        print(str(data.decode()))
        if not data:
            print('Disconnected the client')
            print_lock.release()
            break
        
        
        data = "To Client "+ str(addr[1])
        c.send(str(data).encode())
    c.close()

def main():
    s = socket.socket()
    port = 5000
    host = ""
    s.bind((host,port))
    s.listen(5)

    
    print("Server Running.... ")
    while True:
        c,addr = s.accept()
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,addr)) 

    # con,addr = s.accept()
    # print(data)
    c.close()

if __name__=='__main__':
    main()
