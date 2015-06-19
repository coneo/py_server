import socket
import os
import json

def client(string):
	HOST,PORT = 'localhost', 5566
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST,PORT))
	sock.send(string)
	reply = sock.recv(1024 * 64)
	sock.close()
	return reply
	
str = json.dumps({"a":1, "b":2, "c":3})
print client(str)


#print 'start ...'
#ret = os.system("test.bat")
#print ret
#print 'end ...'