import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import time
import psutil
import threading
import logging

from nose.plugins import cover
from nose.plugins import Plugin

__all__ = ["PSProfile"]

logger = logging.getLogger('nose.plugins.psprofile')

class PSProfile(cover.coverage):
	"""Add a JSON PS profile report to the built-in nose.plugins.cover plugin. 
	"""

	def options(self, parse, env):
		"""
		Add options to the command line
		"""
		Plugin.add_option(
			"--psp-file", 
			action = "store", 
			default = env.get("NOSE_PSP_FILE", "psprofile.json"), 
			dest = psp_file, metavar="FILE"
			help = "Default is the psprofile.json in the working directory")


class PSProfileThread(threading.Thread):

	def __init__(self, pid):
		super(PSProfile, self).__init__()
		self.__counter = 5
		self.__pid = pid
		self.__stop = threading.Event()
		self.__stop.clear() # self.__stop.set()
		self.__ps = psutil.Process(self._pid)

	def stop_t(self):
		self.__stop.set()

	def run(self):
		while not self.__stop.is_set() and self.__counter:
	    	#time.sleep(1)
	    	self.__counter -= 1
    	    print self.__ps.cpu_percent(interval=1)
	    	print self.__ps.virtual_memory()
	    	print self.__ps.swap_memory()


if __name__ == "__main__":
    test_monitor = PSProfile(sys.argv[1])
    test_monitor.start()
    test_monitor.join()