import win32service
import win32serviceutil
import win32event
import logging

logging.basicConfig(filename='C:\Users\hongxiaoqiang\Desktop\py_server\log\daemon.log',
					level=logging.DEBUG,  
					format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger('daemonservice')

class PySvc(win32serviceutil.ServiceFramework):
    # you can NET START/STOP the service by the following name
	_svc_name_ = "LuanDunPython"
    # this text shows up as the service name in the Service
    # Control Manager (SCM)
	_svc_display_name_ = "LuanDunPython Service"
    # this text shows up as the description in the SCM
	_svc_description_ = "This service writes stuff to a file"
    
	def __init__(self, args):
		win32serviceutil.ServiceFramework.__init__(self,args)
        # create an event to listen for stop requests on
		self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
    
    # core logic of the service   
	def SvcDoRun(self):
		import servicemanager
        
		"""
        f = open('test.dat', 'w+')
        rc = None
        
        # if the stop event hasn't been fired keep looping
        while rc != win32event.WAIT_OBJECT_0:
            f.write('TEST DATA\n')
            f.flush()
            # block for 5 seconds and listen for a stop event
            rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)
            
        f.write('SHUTTING DOWN\n')
        f.close()
		"""
		self.start()
		logger.debug('svc starting ...')
		win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
    
    # called when we're being shut down    
	def SvcStop(self):
        # tell the SCM we're shutting down
		self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # fire the stop event
		win32event.SetEvent(self.hWaitStop)
		self.stop()
		logger.debug('svc stopping ....')
		
	def start(self):
		pass
		
	def stop(self):
		pass

"""
class MyS(PySvc):
	def start(self):
		logger.debug('my starting ..... ')
		
	def stop(self):
		logger.debug('my stopping ....')
		
if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(MyS)
	"""