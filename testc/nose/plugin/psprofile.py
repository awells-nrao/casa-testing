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
from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import Manager

import psutil

import nose
from nose.plugins import Plugin

__test__ = False
__all__ = ["PSProfile" ]

#logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

name = 'psprofile'

class PSProfile(Plugin):

	name = 'psprofile'
	score = 1
		
	def options(self, parser, env = os.environ):
		logger.debug("options(self, parser, env = os.environ):...")
		
		parser.add_option(
			"--psprofile-file", 
			action = "store", 
			default = env.get("NOSE_PSP_FILE", "psprofile.json"), 
			dest = "psp_file", 
			metavar="FILE",
			help = "By Default a psprofile.json is generated in the current working directory")

		parser.add_option(
			"--psprofile-margin", 
			action = "store", 
			default = env.get("NOSE_PSP_MARGIN", 2), 
			dest = "psp_margin", 
			metavar="FILE",
			help = "A marging of time after execute the test")

		Plugin.options(self, parser, env)

	def configure(self, options, conf):
		logger.debug("configure(self, options, conf):...")
		super(PSProfile, self).configure(options, conf)
		
		if not self.enabled:
			logger.debug("plugin not enabled")
			return
		
		self.__profile_data = {}
		self.__psp_report = options.psp_file
		self.__psp_margin = options.psp_margin

	def prepareTestCase(self, test):
		pid = os.getpid()
		self.testname = test.test._testMethodName
		self.__profiler = PSProfileThread(pid)
		self.__profiler.setDaemon(True)
		logger.debug("prepareTestCase(self, test):... %s [%s]" % (self.testname, pid))
		
		# setup the multiprocessing stuff

		self.__process_manager = Manager()
		self.__process_event = self.__process_manager.Event()
		self.__process_data = self.__process_manager.dict()

		self.__process_data['ioc'] = []
		self.__process_data['fds'] = []
		self.__process_data['mem'] = []
		self.__process_data['time'] = []
		self.__process_data['cpu'] = []

		self.__process = Process(target=PSProfile.profile, args=(pid, self.__process_data, self.__process_event))

	def startTest(self, test):
		self.__process_event.clear()
		self.__process.start()
		logger.debug("startTest(self, test):... %s" % self.testname)
		
	def stopTest(self, test):
		logger.debug("stopTest(self, test):... %s" % self.testname)
		time.sleep(int(self.__psp_margin))
		self.__process_event.set()
		self.__process.join()
		self.__profile_data[self.testname] = dict(self.__process_data)

	def report(self, stream):
		"""
		self.__profile_data DictProxy object is not JSON serializable
		"""
		logger.debug("report(self, stream):...")
		json_report = json.dumps(self.__profile_data)
		
		self.write_report(json_report)

		if self.conf.verbosity > 4:
			stream.writeln(str(json_report))

	def write_report(self, json_report):
		# nice validator http://jsonformatter.curiousconcept.com/
		report_file_path = "%s/%s" % (os.getcwd(), self.__psp_report)
		with open(report_file_path, 'w') as report_file:
			report_file.write(json_report)
		print "PROFILE: %s" % self.__psp_report

	def finalize(self, result):
		logger.debug("finalize(self, result):...")

	# multiprocessing stuff

	@staticmethod
	def profile(pid, data, event, interval = 1):
		"""
		data is a DictProxy
		"""

		# this method is awfully coded, DictProxy isn't
		# very flexible

		ps = psutil.Process(pid)

		ioc = []
		fds = []
		mem = []
		stamp = []
		cpu = []

		while not event.is_set():
			ioc.append(ps.io_counters())
			fds.append(ps.num_fds())
			mem.append(ps.memory_info())
			stamp.append(time.time())
			cpu.append(ps.cpu_percent(interval = interval))

		data['ioc'] = ioc
		data['fds'] = fds
		data['mem'] = mem
		data['time'] = stamp
		data['cpu'] = cpu
			

class PSProfileThread(threading.Thread):

	def __init__(self, pid, interval = 1):
		super(PSProfileThread, self).__init__()

		self.__pid = pid
		self.__interval = interval
		self.__cpu = []
		self.__ioc = []
		self.__fds = []
		self.__mem = []
		self.__time = []
		self.__ps = psutil.Process(self.__pid)
		self.__stop_profiler = threading.Event()
				
	def join(self, timeout=None):
		self.stop_profiler.set()
		super(PSProfileThread, self).join(timeout)

	def __gather_data(self):
		try:
			logger.debug("getting data...")
			self.__ioc.append(self.__ps.io_counters())
			self.__fds.append(self.__ps.num_fds())
			self.__mem.append(self.__ps.memory_info())
			self.__time.append(time.time())
			self.__cpu.append(self.__ps.cpu_percent(interval = self.__interval))
		except:
			logger.debug("problem gathering data...")
			self.__stop_profiler.set()

	def profile_data(self):
		return { 
			"cpu"  : self.__cpu,
			"ioc"  : self.__ioc,
			"fds"  : self.__fds,
			"mem"  : self.__mem,
			"time" : self.__time
			}

	def run(self):
		while not self.__stop_profiler.isSet():
			if self.__ps.status():
				self.__gather_data()
			else:
				logger.debug("process [%s] is not alive" % self.__pid)
				self.__stop_profiler.set()

if __name__ == "__main__":
	# Note to be deleted:
	# /usr/lib/python2.6/site-packages/psutil-2.1.3-py2.6-linux-x86_64.egg
	# e.g.: /usr/lib/python2.6/site-packages/psutil-2.1.3-py2.6-linux-x86_64.egg/psutil
    profiler = PSProfileThread(int(sys.argv[1]))
    profiler.start_profiler()
    profiler.join()
    print json.dumps(profiler.profile_data())