
"""
if __name__ == '__main__':
	print 'hello shok'
	"""

"""
import daemon

from spam import do_main_program

with daemon.DaemonContext():
	do_main_program()
	
	"""
	
from servicemgr import MgrService

class Engine(MgrService):
	def start(self):
		print 'start ... '
		
	def stop(self):
		print 'stop ...'