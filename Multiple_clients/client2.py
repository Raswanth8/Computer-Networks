import socket 
import csv
import numpy as np
  
def Main(): 
    # local host IP '127.0.0.1' 
    host = '127.0.0.1'
  
    # Define the port on which you want to connect 
    port = 5000
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to server on local computer 
    s.connect((host,port)) 
    def files():
        fields = ['quality','pH','volatile acidity', 'alcohol'] 
        rows = [ [5,3.51,0.7,9.4], 
                [5,3.2,0.88,9.8],[5,3.26,0.76,9.8],[6,3.16,0.28,9.8],[5,3.51,0.7,9.4],[5,3.51,0.66,9.4],[5,3.3,0.6,9.4],[7,3.39,0.65,10],[7,3.36,0.58,9.5],[5,3.35,0.5,10.5],[5,3.28,0.58,9.2],[5,3.35,0.5,10.5]] 
        file = open('file.csv','w')

        csvwriter = csv.writer(file) 
        csvreader = csv.reader(file)

        csvwriter.writerow(fields)
        csvwriter.writerow(rows)
        i = input()
        for row,i in rows:
            if (row[0] & i )== 5 :
                print(np.mean(row[3]))
            elif (row[0] & i )== 6 :
                print(np.mean(row[3]))
            elif (row[0] & i )== 7 :
                print(np.mean(row[3]))
        
    while True: 
        inp = input(" > ")
        message = "From Client 2: "+inp
        # message sent to server 
        s.send(message.encode('ascii')) 
  
        # messaga received from server 
        data = s.recv(1024) 
  
        # print the received message 
        # here it would be a reverse of sent message 
        print('Received from the server :',str(data.decode('ascii'))) 
  
        # ask the client whether he wants to continue 
        ans = input('\nDo you want to continue(y/n) :') 
        if ans == 'y': 
            files()
        else: 
            break
    # close the connection 
    s.close() 
  
if __name__ == '__main__': 
    Main() 
