#Server program

import socket
import thread

def splitter(connectionSocket,addr) :    
    sentence = connectionSocket.recv(1024)
    print("Received data ", sentence)
    file1 = str(sentence)
    print("SENTENCE= ",sentence)   
    file2 = file1.split()[1]
    filen = file2[1:]  
    
    try : 	
    	myobj = open(filen,"r")
    except :
        headert = "\HTTP/1.1 404 NOT FOUND"
        header = str(headert)
        text = header
    else :        
        headert = "\HTTP/1.1 200 OK"
        header = str(headert)
        text2 = myobj.read()
        text = header +text2
    
    sentence = text
    connectionSocket.send(sentence)
    myobj.close()
    connectionSocket.close()
    
serverName = 'localhost'
serverPort = 5555

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(5)
sfamily  = str(socket.AF_INET)
stype = str(socket.SOCK_STREAM)
stimeout = str(serverSocket.gettimeout())
shostname = str(socket.gethostname())
print("sfamily",sfamily)
print("stype",stype)
print("stimeout",stimeout)
print("shostname",shostname)
print("protocol TCP")

print("Server is ready to receive")


while(1) :

    connectionSocket, addr = serverSocket.accept()
    print("connection from ", addr)
    thread.start_new_thread(splitter,(connectionSocket,addr))

