import socket,pickle
from threading import Thread
import tkinter as tk

def button_func():
    sendname()
    top.destroy()

def sendname():
    global E1,E2,E3
    string1 = E1.get() 
    string2 = E2.get() 
    string3 = E3.get() 
    data_array=[string1,string2,string3]
    data_string = pickle.dumps(data_array) 
    client_socket.send(data_string)
    client_socket.close()



top = tk.Tk()
top.title("Poll")

L1 = tk.Label(top, text="Enter Your Name: ")
L1.grid(row=0, column=0)
E1 = tk.Entry(top, bd = 5)
E1.grid(row=0, column=1)
L2 = tk.Label(top, text="Enter Your Email: ")
L2.grid(row=1, column=0)
E2 = tk.Entry(top, bd = 5)
E2.grid(row=1, column=1)
L4 = tk.Label(top, text="Your Vote")
L4.grid(row=2, column=0)
L5 = tk.Label(top, text="1) Option 1   2) Option 2   3) Option 3")
L5.grid(row=2, column=1)
L3 = tk.Label(top, text="Your Choice: ")
L3.grid(row=3, column=0)
E3 = tk.Entry(top, bd = 5)
E3.grid(row=3, column=1)
MyButton1 = tk.Button(top, text="Submit", width=10, command=button_func)
MyButton1.grid(row=4, column=1)

HOST=socket.gethostname()
PORT=5000
ADDR = (HOST, PORT)

client_socket=socket.socket()
client_socket.connect(ADDR)

tk.mainloop()