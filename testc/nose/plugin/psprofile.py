import sys

assert sys.version >= '2' # and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import time
import threading
import logging
import json
import traceback

import psutil

import nose
from nose.plugins import Plugin

__test__ = False
__all__ = ["PSProfile", "PSProfileThread"]

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class PSProfile(Plugin):
	# http://nose.readthedocs.org/en/latest/plugins/interface.html
	# http://nose.readthedocs.org/en/latest/plugins/writing.html
	# http://nose.readthedocs.org/en/latest/plugins/testid.html
	# http://community.activestate.com/impatient-developers-guide-writing-python-nose-plugins

	name = 'psprofile'
	enabled = True

	def __init__(self):
		logger.debug("__init__(self):...")
		super(PSProfile, self).__init__()
		self.testname = ""
		
	def options(self, parser, env = os.environ):
		logger.debug("options(self, parser, env = os.environ):...")
		Plugin.options(self, parser, env)

		parser.add_option(
			"--psprofile-file", 
			action = "store", 
			default = env.get("NOSE_PSP_FILE", "psprofile.xml"), 
			dest = "psp_file", 
			metavar="FILE",
			help = "Default is the psprofile.json in the working directory")

	def configure(self, options, conf):
		logger.debug("configure(self, options, conf):...")
		super(PSProfile, self).configure(options, conf)
		if not self.enabled:
			return

	def prepareTestCase(self, test):
		pid = os.getpid()
		self.testname = self.testName(test)
		self.profiler = PSProfileThread(pid)
		logger.debug("prepareTestCase(self, test):... %s [%s]" % (self.testname, pid))

	def startTest(self, test):
		logger.debug("startTest(self, test):... %s" % self.testname)
		#pass#self.__profiler.start_profiler()

	def stopTest(self, test):
		logger.debug("stopTest(self, test):... %s" % self.testname)
		#pass#self.__profiler.stop_profiler()

	def report(self, stream):
		logger.debug("report(self, stream):...")
		#profile_data = self.__profiler.profile_data()
		#profile_data["test"] = self.testname
		
		# if self.conf.verbosity > 1:
		# 	for e in self.__dict__:
		# 		stream.writeln(str(e))

	def finalize(self, result):
		logger.debug("report(self, stream):... %s")

class PSProfileThread(threading.Thread):

	def __init__(self, pid, interval = 1):
		super(PSProfileThread, self).__init__()
		self.__pid = pid
		self.__interval = interval
		self.__stop = threading.Event()
		self.__cpu = []
		self.__ioc = []
		self.__fds = []
		self.__mem = []
		self.__time = []

	def stop_profiler(self):
		self.__stop.set()

	def gather_data(self):
		try:
			self.__cpu.append(self.__ps.cpu_percent(interval = self.__interval))
			self.__ioc.append(self.__ps.io_counters())
			self.__fds.append(self.__ps.num_fds())
			self.__mem.append(self.__ps.memory_info())
			self.__time.append(time.time())
		except:
			self.stop_profiler()

	def start_profiler(self):
		self.__ps = psutil.Process(self.__pid)
		self.__stop.clear()
		self.start()

	def profile_data(self):
		return { 
			"cpu"  : self.__cpu,
			"ioc"  : self.__ioc,
			"fds"  : self.__fds,
			"mem"  : self.__mem,
			"time" : self.__time
			}

	def run(self):
		while not self.__stop.is_set():
			if self.__ps.status():
				self.gather_data()
			else:
				self.stop_profiler()

if __name__ == "__main__":
	# Note to be deleted:
	# /usr/lib/python2.6/site-packages/psutil-2.1.3-py2.6-linux-x86_64.egg
	# e.g.: /usr/lib/python2.6/site-packages/psutil-2.1.3-py2.6-linux-x86_64.egg/psutil
    profiler = PSProfileThread(int(sys.argv[1]))
    profiler.start_profiler()
    profiler.join()
    print json.dumps(profiler.profile_data())