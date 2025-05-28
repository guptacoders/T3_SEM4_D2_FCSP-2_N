#server side program
import socket

host=socket.gethostname()
port=5000

server_socket=socket.socket()
server_socket.bind((host,port))
server_socket.listen()

conn,address=server_socket.accept()
print(address)
print(conn)


while True:
    data=conn.recv(1024).decode() #conn.recv
    if not data:
        break
    print("from client "+str(data))
    data=input("--->")
    conn.send(data.encode())

conn.close()