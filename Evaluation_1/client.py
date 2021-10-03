import socket
import io
import pandas as pd

c = socket.socket()
host = '127.0.0.1'
port = 5001
c.connect((host, port))
data_string = c.recv(1024).decode()
data = io.StringIO(data_string)
df = pd.read_csv(data, sep=" ",skipinitialspace = True)
df.reset_index(drop=True)

print("DataFrame:")
print(df)
print(df.dtypes)
print(df.columns)
print("Choose what you want to do: ")

def get_total_client(df):
    name = str(input())
    result1 = df.groupby('telco')['drop_call_rate'].sum()
    result2 = df.groupby('telco')['drop_call_rate'].mean()
    print(result1)
    print(result2)

def get_total_server(df):
    name = str(input())
    result1 = df.groupby('month')['drop_call_rate'].sum()
    result2 = df.groupby('month')['drop_call_rate'].mean()
    print(result1)
    print(result2)


cp = input()

if(cp=='T'):
    get_total_client(df)
elif(cp=='U'):
    get_total_server(df)

c.close()
