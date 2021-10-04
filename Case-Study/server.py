import socket,pickle
from threading import Thread

def accept_incoming_connections():
   
    while True:
        client, client_address = SERVER.accept()
        print('Got connection from', client_address)
        addresses[client] = client_address
        handle_client(client)


def handle_client(client):
    try: 
        while True:
                data_string=client.recv(100)
                data_array=pickle.loads(data_string)
                name=data_array[0]
                email=data_array[1]
                response=data_array[2]
                with open('responses.txt','a') as f:
                        f.write(name)
                        f.write(' , ')
                        f.write(email)
                        f.write(' , ')
                        f.write(response)
                        f.write('\n')
                        count1 = 0
                        count2 = 0
                        count3 = 0
                        num = response
                        if num == '1':
                            count1 +=1
                            with open('D:/Study/Networking/case-study/countOP1.txt','a') as m:
                                c1 = str(count1)
                                m.write(c1)
                                m.close()
                        elif num == '2':
                            count2 +=1
                            with open('D:/Study/Networking/case-study/countOP2.txt','a') as n:
                                c2 = str(count2)
                                n.write(c2)
                                n.close()
                        elif num == '3':
                            count3 +=1
                            with open('D:/Study/Networking/case-study/countOP3.txt','a') as o:
                                c3 = str(count3)
                                o.write(c3)
                                o.close()
    except:
        print("Thank you for your response")    
                              
clients = {}
addresses = {}

HOST = socket.gethostname()
PORT = 5000
ADDR = (HOST, PORT)

SERVER = socket.socket()
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()