
import sys, os
import logging
import json
import threading
import SocketServer, subprocess
from threading import Thread
from daemon import Daemon
from svc import PySvc
import win32serviceutil

HOST = 'localhost'
PORT = 5566MAX_DATASIZE = 1024 * 64

logging.basicConfig(filename='C:\Users\hongxiaoqiang\Desktop\py_server\log\server.log',
					level=logging.DEBUG, 
					format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger('server')

#bat -> msg map
bat_map = {
	'Pkgconfig.bat' : (
		'Config'
		),
	'PkgIOSAB.bat' : (
		'IOS_Fright_AB', 
		'IOS_Common_AB',
		'IOS_Shop_AB'
		),
	'PkgANDROIDAB.bat' : (
		'ANDROID_Fright_AB',
		'ANDROID_Common_AB'
		),
	'PkgANDROIDAE.bat' : (
		'ANDROID_AE'
		),
}
def findBat(msg):
	"find bat file by msg type in bat_map"
	for key in bat_map:
		if msg in bat_map[key]:
			return key
	
	return False


class FirTcpHandle(SocketServer.BaseRequestHandler):
	"One instance per connection.  Override handle(self) to customize action."
	success_threads = 0
	def handle(self):
		data = self.request.recv(MAX_DATASIZE)
		print data
		self.msg_parse(data)
		self.request.close()
		
	def msg_parse(self,json_str):
		data = json.loads(json_str)
		logger.debug(data)
		#print 'a:' + str(data['a'])
		
		threads = []
		t1 = threading.Thread(target=self.run_bat, args=(1,))
		t2 = threading.Thread(target=self.run_bat, args=(2,))
		threads.append(t1)
		threads.append(t2)
		t1.start()
		t2.start()
		for t in threads:
			t.join()
		if self.success_threads == 2:
			self.request.send( 'success from server')
		else:
			self.request.send(' failed from server')
		
	def run_bat(self, type):
		#type stands for which bat to run
		if 1 == type:
			ret = os.system("test.bat")
			if ret == 1:
				print 'test.bat success'
				self.success_threads += 1
		elif 2 == type:
			ret = os.system("test2.bat")
			if ret == 1:
				print 'test2.bat success'
				self.success_threads += 1
		
class FirTcpServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	daemon_threads = True
	allow_reuse_address = True
	
	def __init__(self, server_address, RequestHandlerClass):
		SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass)
		

class Engine(PySvc):
	def start(self):
		logger.debug('starting engine ... ')
		server = FirTcpServer((HOST, PORT), FirTcpHandle)
		server.serve_forever()
		
	def stop(self):
		logger.debug('stopping engine ...')
		
if __name__ == '__main__':
	win32serviceutil.HandleCommandLine(Engine)

'''
	server = FirTcpServer((HOST, PORT), FirTcpHandle)
	try:
		print 'starting server ... '
		server.serve_forever()
	except KeyboardInterrupt:
		sys.exit(0)
'''