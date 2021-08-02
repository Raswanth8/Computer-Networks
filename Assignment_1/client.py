import socket
import csv 
s = socket.socket()
host = socket.gethostname()
port = 5003
s.connect((host,port))

print("Received: ")

fields = ['Firstname', 'Lastname','Designation','Contact','Salary','City'] 
rows = [ ['Raswanth', 'Rajangam','CEO','9994529791',50000,'Bangalore'], 
         ['Fahad' ,'Fasil','CTO','9994528791',25000,'Bangalore']] 
file = open('file.csv','w')

csvwriter = csv.writer(file) 
csvreader = csv.reader(file)

csvwriter.writerow(fields)

for row in rows:
    row[4] =  row[4] + row[4]*0.1
    csvwriter.writerows(rows)

s.close()