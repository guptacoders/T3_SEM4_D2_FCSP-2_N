# socket-->end point connection
#TCP_client
#client program 
import socket 
host=socket.gethostname()
print(host) #server ip address
port=5000
client_socket= socket.socket()
client_socket.connect((host,port))

message=input("----->")

while message.lower().strip()!="bye":
    client_socket.send(message.encode())
    data=client_socket.recv(1024).decode()#server ans store in data
    print("Recieve from server "+data)
    message=input("----->")
    
client_socket.close()