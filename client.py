#client program
import socket
import time

serverName = 'localhost'
serverPort = 5555

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = raw_input('enter file name: ')
print("sentence = ",sentence)
clientSocket.send(sentence)
starttime = time.time()
mSentence = clientSocket.recv(1024)
endtime = time.time()
rtt = endtime - starttime
	
cfamily  = str(socket.AF_INET)
ctype = str(socket.SOCK_STREAM)
ctimeout = str(clientSocket.gettimeout())
chostname = str(socket.gethostname())
print("cfamily",cfamily)
print("ctype",ctype)
print("ctimeout",ctimeout)
print("chostname",chostname)
print("protocol TCP")

print("From Server : ", mSentence)
clientSocket.close()
