import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import time
import psutil
import threading
import logging

from nose.plugins import Plugin

__all__ = ["PSProfile"]

logger = logging.getLogger('nose.plugins.psprofile')


class PSProfile(Plugin):
	# http://nose.readthedocs.org/en/latest/plugins/interface.html
	# http://nose.readthedocs.org/en/latest/plugins/writing.html

	name = 'psprofile'

	def __init__(self):
		 super(PSProfile, self).__init__()
		 self.__profile = {}

	def options(self, parser, env = os.environ):

		Plugin.options(self, parser, env)

		parser.add_option(
			"--psp-file", 
			action = "store", 
			default = env.get("NOSE_PSP_FILE", "psprofile.xml"), 
			dest = psp_file, metavar="FILE"
			help = "Default is the psprofile.json in the working directory"
		super(PSProfile, self).options(parser, env = env)

	def startTest(self, test):
		if self.__profiler:
			self.__profiler.stop_profiler()

		self.__profiler = PSProfileThread(os.getpid());
		pass
		# start profiling

	def stopTest(self, test):
		self.__profiler.stop_profiler()

	def finalize(self, result):
		pass

	def configure(self, options, conf):
        super(PSProfile, self).configure(options, conf)

class PSProfileThread(threading.Thread):

	def __init__(self, pid):
		super(PSProfileThread, self).__init__()
		self.__pid = pid
		
		self.__stop = threading.Event()
		self.__stop.clear()

		self.__ps = psutil.Process(self._pid)

	def stop_profiler(self):
		self.__stop.set()

	def gather_data(self):
		pass

	def run(self):
		while not self.__stop.is_set():
	    	pass
    	    #print self.__ps.cpu_percent(interval=1)
	    	#print self.__ps.virtual_memory()
	    	#print self.__ps.swap_memory()


if __name__ == "__main__":
    test_monitor = PSProfile(sys.argv[1])
    test_monitor.start()
    test_monitor.join()