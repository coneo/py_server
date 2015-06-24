import win32service
import win32serviceutil
import win32event
import logging

logging.basicConfig(filename='daemon.log',
					level=logging.DEBUG,  
					format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger('servicemgr')

class MgrService(win32serviceutil.ServiceFramework): 
    """
    Usage: 'python topmgr.py install|remove|start|stop|restart'
    """
    _svc_name_ = "LuanDunResPack"
    _svc_display_name_ = "LuanDunResPack"
    _svc_description_ = "this is for res pack for luandun"

    def __init__(self, args): 
        win32serviceutil.ServiceFramework.__init__(self, args) 
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcDoRun(self):
		import servicemanager
		#self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
		logger("mgr startting...")
		#self.ReportServiceStatus(win32service.SERVICE_RUNNING)
		f = open('test1.dat', 'w+')
		rc = None
		
        # if the stop event hasn't been fired keep looping
		while rc != win32event.WAIT_OBJECT_0:
			f.write('TEST DATA\n')
			f.flush()
            # block for 5 seconds and listen for a stop event
			rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)
            
		f.write('SHUTTING DOWN\n')
		f.close()
		logger("mgr waitting...")
		#win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
		logger("mgr end")
        
    def SvcStop(self): 
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        logger("mgr stopping...")
        self.stop()
        logger("mgr stopped")
       
        win32event.SetEvent(self.hWaitStop)
        #self.ReportServiceStatus(win32service.SERVICE_STOPPED)

    def start(self): pass

    def stop(self): pass
		
if __name__ == '__main__':
	win32serviceutil.HandleCommandLine(MgrService)
