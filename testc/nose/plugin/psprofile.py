"""
See: http://code.google.com/p/python-nose/issues/detail?id=105

*ALSO NOTE* that if you pass a unittest.TestSuite
      instance as the suite, context fixtures at the class, module and
      package level will not be used, and many plugin hooks will not
      be called. If you want normal nose behavior, either pass a list
      of tests, or a fully-configured `nose.suite.ContextSuite`_.
"""


import sys

assert sys.version >= '2', "Python 2 or greater is supported"

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
__all__ = ["PSProfile" ]

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

name = 'psprofile'

class PSProfile(Plugin):
	# http://nose.readthedocs.org/en/latest/plugins/interface.html
	# http://nose.readthedocs.org/en/latest/plugins/writing.html
	# http://nose.readthedocs.org/en/latest/plugins/testid.html
	# http://community.activestate.com/impatient-developers-guide-writing-python-nose-plugins

	name = 'psprofile'
	score = 1
		
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
		self.__profile_data = {}
		if not self.enabled:
			return

	def prepareTestCase(self, test):
		pid = os.getpid()
		self.testname = test.test._testMethodName
		self.__profiler = PSProfileThread(pid)
		logger.debug("prepareTestCase(self, test):... %s [%s]" % (self.testname, pid))

	def startTest(self, test):
		logger.debug("startTest(self, test):... %s" % self.testname)
		self.__profiler.start_profiler()

	def stopTest(self, test):
		logger.debug("stopTest(self, test):... %s" % self.testname)
		self.__profiler.stop_profiler()
		self.__profile_data[self.testname] = self.__profiler.profile_data()

	def report(self, stream):
		logger.debug("report(self, stream):...")
		json_report = json.dumps(self.__profile_data)
		if self.conf.verbosity > 0:
			stream.writeln(str(json_report))

	def finalize(self, result):
		logger.debug("finalize(self, result):...")

class PSProfileThread(threading.Thread):

	def __init__(self, pid, interval = 0.5):
		super(PSProfileThread, self).__init__()
		self.__pid = pid
		self.__interval = interval
		self.__stop = threading.Event()
		self.__cpu = []
		self.__ioc = []
		self.__fds = []
		self.__mem = []
		self.__time = []

	def start_profiler(self):
		self.__ps = psutil.Process(self.__pid)
		self.__stop.clear()
		self.start()	

	def stop_profiler(self):
		self.__stop.set()

	def gather_data(self):
		try:
			logger.debug("getting data...")
			self.__cpu.append(self.__ps.cpu_percent(interval = self.__interval))
			self.__ioc.append(self.__ps.io_counters())
			self.__fds.append(self.__ps.num_fds())
			self.__mem.append(self.__ps.memory_info())
			self.__time.append(time.time())
		except:
			logger.debug("problem gathering data...")
			self.stop_profiler()

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
			#if self.__ps.status():
			self.gather_data()
			#else:
			#	self.stop_profiler()

if __name__ == "__main__":
	# Note to be deleted:
	# /usr/lib/python2.6/site-packages/psutil-2.1.3-py2.6-linux-x86_64.egg
	# e.g.: /usr/lib/python2.6/site-packages/psutil-2.1.3-py2.6-linux-x86_64.egg/psutil
    profiler = PSProfileThread(int(sys.argv[1]))
    profiler.start_profiler()
    profiler.join()
    print json.dumps(profiler.profile_data())