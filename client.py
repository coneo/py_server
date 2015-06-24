import socket
import os
import json

def client(string):
	HOST,PORT = 'localhost', 5566
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST,PORT))
	sock.send(string)
	is_running = True
	if is_running:
		print 'is running ... '
		reply = sock.recv(1024 * 64)
		print reply
	sock.close()
	print 'end client ... '
	
str = json.dumps({"a":1, "b":2, "c":3})
client(str)


#print 'start ...'
#ret = os.system("test.bat")
#print ret
#print 'end ...' 