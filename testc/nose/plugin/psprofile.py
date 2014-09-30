import sys

assert sys.version >= '2' # and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import time
import psutil
import threading
import logging
import json

__all__ = ["PSProfile", "PSProfileThread"]

logger = logging.getLogger('nose.plugins.psprofile')

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
    profiler = PSProfileThread(int(sys.argv[1]))
    profiler.start_profiler()
    profiler.join()
    print json.dumps(profiler.profile_data())