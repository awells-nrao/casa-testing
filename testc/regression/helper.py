#!/usr/bin/env python
"""
This module is the core module of the testing 'framework'.

Exported classes:

RegressionBase -- Inherits from unittest.TestCase, this class is the base testing class for the regression test classes,
the class defines helper methods to be used within the class, e.g.: the execute method will execute a casapy executable
python script.

RegressionHelper -- Defines static helper methods to be used, e.g.: data management.

regressionLogger -- A python logger

RegressionRunner -- Class to locate and execute the testing classes by using nose, within casa:
> from regression_utils import RegressionRunner
> RegressionRunner.execute_regression("regression_b0319")
"""

import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import string
import importlib
import inspect
import shutil
import logging
import hashlib
import threading
import imp

import unittest
import nose

from testc.nose.plugin import psprofile
from testc import regression

__test__ = False
__all__ = ["RegressionHelper", "RegressionBase", "RegressionRunner", "RegressionInject", "regressionLogger"]

regressionLogger = logging.getLogger("RegressionLogger")

class RegressionInject(object):

	def __init__(self, arg0, arg1 = None):
		self.__module_name = arg0
		self.__method_name = arg1
		self.__module = None
		self.__method = None

	def __call__(self, func):
		def decorated(*args):
			file, path, desc = imp.find_module(self.__module_name, sys.path[1:])
			assert file, "No module %s found" % self.__module_name

			regressionLogger.debug("No module %s found" % self.__module_name)

			RegressionHelper.inject_casac_globals()
			regressionLogger.debug("CASA globals 'injected'")

			self.__module = imp.load_module(self.__module_name, file, path, desc)

			if self.__method:
				self.__method = getattr(self.__module, self.__method)
				self.__method()
			
			return func

		return decorated


class RegressionHelper():

	def __init__(self):
		raise NotImplementedError("This class only implements static methods")

	@staticmethod
	def casapath():
		return os.environ.get("CASAPATH", "unset").split()[0]

	@staticmethod
	def assert_file(file):
		assert os.access(file, os.F_OK), "%s not exists" % file
		
	@staticmethod
	def assert_files(files, basepath = ""):
		for file in files:
			RegressionHelper.assert_file("%s/%s" % (basepath, file))
		
	@staticmethod
	def locate_data(file):
		# module_path =  RegressionHelper.base_path(importlib.import_module(self.__module__).__file__)
		# index_file = file if file else 
		pass
	
	# deprecated
	@staticmethod
	def base_path(file):
		return os.path.dirname(file)

	@staticmethod
	def data_copy(array_path, destination = os.getcwd()):
		"""Given an array of paths, it will iterate and copy all to the
		current working directory, which is where casapy is executed
		"""
		for data_path in array_path:
			RegressionHelper.assert_file(data_path)
			if os.path.isdir(data_path):
				shutil.copytree(data_path, destination)
			else:
				shutil.copy(data_path, destination)

	@staticmethod
	def data_remove(array_path):
		"""Given an array of paths, it will iterate and delete them
		"""
		for data_path in array_path:
			RegressionHelper.assert_file(data_path)
			regressionLogger.debug("data_remove %s" % data_path)
			if os.path.isdir(data_path):
				shutil.rmtree(data_path, True)
			else:
				os.remove(data_path)

	@staticmethod
	def md5sum(objinst, on_memory = False):
		"""Whatever fits in the current rss memory, bigger files
		should be read in chunks of 129KB (to be implemented) if is
		needed
		"""
		digest = None

		if not on_memory:
			RegressionHelper.assert_file(objinst)
			with open(objinst, 'r') as to_hash:
				digest = hashlib.md5(to_hash.read()).hexdigest()
		else:
			digest = hashlib.md5(objinst).hexdigest()

		return digest

	@staticmethod
	def inject_casac_globals(module):
		casac_globals = RegressionHelper.casa_console_globals()
		for item in casac_globals.items():
			globals()[item[0]] = item[1]

	@staticmethod
	def casa_console_globals():
		"""Return the CASA globals of the ipython console frame stack
		"""
		_stack = inspect.stack()
		_stack_flag = -1
		_stack_frame = None
		_stack_frame_globals = None

		for _stack_level in _stack:
			_stack_flag += 1
			if(string.find(_stack_level[1], "ipython console")):
				_stack_frame = sys._getframe(_stack_flag)
				_stack_frame_globals = _stack_frame.f_globals

		assert _stack_frame_globals, "No ipython console globals defined"
		return _stack_frame_globals

class RegressionBase(unittest.TestCase):

	def setUp(self):
		"""All the custom setup should be implemented by the developer
		"""
		self.casapy_script = None

	def tearDown(self):
		pass

	def __script_path(self, script_module_path, script):
		"""Return the absolute path of the script
		"""
		RegressionHelper.assert_file(script_module_path)
		path_script = "%s/%s.py" % (script_module_path, script)
		RegressionHelper.assert_file(path_script)
		return path_script

	def __class_module_path(self):
		"""Return the class module path (where is located), this method
		is intended to be used by child classes to resolve where
		the class extended is locate, will return the base path
		"""
		module_path =  os.path.dirname(importlib.import_module(self.__module__).__file__)
		RegressionHelper.assert_file(module_path)
		return module_path

	def __console_globals(self):
		"""Return the globals of the ipython console frame stack
		"""
		_stack = inspect.stack()
		_stack_flag = -1
		_stack_frame = None
		_stack_frame_globals = None

		for _stack_level in _stack:
			_stack_flag += 1
			if(string.find(_stack_level[1], "ipython console")):
				_stack_frame = sys._getframe(_stack_flag)
				_stack_frame_globals = _stack_frame.f_globals

		assert _stack_frame_globals, "No ipython console globals defined"
		return _stack_frame_globals

	def execute(self, casapy_script, import_module = False, custom_globals = None):

		if import_module:
			importlib.import_module("%s" % casapy_script)
		else:
			console_frame_globals = self.__console_globals()
			console_frame_globals = dict(console_frame_globals.items() + custom_globals.items()) if custom_globals else console_frame_globals
			cexec_script = self.__script_path(self.__class_module_path(), casapy_script)
			execfile(cexec_script, console_frame_globals)

	@classmethod
	def setUpClass(cls):
		pass

	@classmethod
	def tearDownClass(cls):
		pass

class RegressionRunner:
	"""This class only implements static methods, intented to be used as
	a regression test runner
	"""

	def __init__(self):
		raise NotImplementedError("This class only implements static methods")

	@staticmethod
	def execute(test, custom_argv = None, guide = False, verbosity = 2):
		"""Execute the regression test by using nose with the nose arguments
		and with -d -s -v and --with-xunit (xml generation)
		"""
		# use imp instead of fixed package uri? not sure yet - atejeda
		test_package = "testc.regression" if not guide else "testc.guide"
		test_module_uri = "%s.%s" % (test_package, test)
		test_module = importlib.import_module(test_module_uri)
		test_module_path = os.path.dirname(test_module.__file__)

		default_argv = [	test_module_path,
							test_module_uri,
							"-d",
							"-s",
							"--verbosity=%s" % verbosity,
							"--with-xunit",
							"--xunit-file=%s.xml" % test,
							"--with-psprofile",
							"--psprofile-file=%s.json" % test
						]

		test_argv = custom_argv if custom_argv else default_argv

		nose.run(argv = test_argv, addplugins = [psprofile.PSProfile()])		

		del test_module

if __name__ == "__main__":
	assert sys.argv[1], "an argument is needed, e.g.: regression_3c129_tutorial"
	RegressionRunner.execute(sys.argv[1])