import socket
import threading

port =input("port for server:")
server=socket.gethostbyname(socket.gethostname())

addr=(server,int(port))

header=64

passuser=input("password for server:")
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

FORMAT='utf-8'

server.bind(addr)

conns=[]

def broadcast(message):
    classic="|"
    message=message.encode(FORMAT)
    classic=classic.encode(FORMAT)
    for conn1 in conns:
        conn1.send(message)
        conn1.send(classic)
        

def handle_client(conn,addr):
    print("New connections....")
    connected=True
    while connected==True:
        msg_length=1
        #msg_length=conn.recv(header).decode(FORMAT)
        if msg_length:
            #msg_length=int(msg_length)
            msg=conn.recv(64).decode(FORMAT)
            if msg=="dis":
                connected=False
                #conn.close()
            else:
                print(msg)
                broadcast(msg)
            #msg=msg.encode(FORMAT)
            #server.send(msg)
    print(addr+" "+msg)
        
def start():
    server.listen()
    while True:
        conn,addr=server.accept()
        password=conn.recv(64).decode(FORMAT)
        if password==passuser:
            welcome="connection accepted..."
            welcome=welcome.encode(FORMAT)
            conn.send(welcome)
            conns.append(conn)
            thread=threading.Thread(target=handle_client,args=(conn, addr))
            thread.start()
        else:
            decline="connection refused"
            decline=decline.encode(FORMAT)
            conn.send(decline)
            conn.close()
        #print("Active connections= "+threading.activeCount()-1)

print("server is starting...")

start()
