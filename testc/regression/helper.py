#!/usr/bin/env python

import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import importlib
import inspect
import string
import shutil
#from enum import Enum

import unittest
import nose

from testc import regression

__all__ = ["RegressionHelper", "RegressionBase", "RegressionRunner"]

class RegressionHelper():

	def __init__(self):
		raise NotImplementedError("This class only implements static methods")

	@staticmethod
	def __is_gnulinux():
		pass

	@staticmethod
	def working_dir(working_dir = None):
		pass

	@staticmethod
	def casapath():
		return os.environ.get("CASAPATH", "unset").split()[0]

	@staticmethod
	def regression_data():
		return os.environ.get("CASA_REGRESSION_DATA", "unset")

	@staticmethod
	def assert_file(file):
		assert os.access(file, os.F_OK), "%s not exists" % file

	@staticmethod
	def data_copy(array_path):
		"""Given an array of paths, it will iterate and copy all to the
		current workind directory, which is where casapy is executed
		"""
		destination = os.getcwd()
		
		for data_path in array_path:
			
			RegressionHelper.assert_file(data_path)

			if os.path.isdir(data_path):
				shutil.copytree(data_path, destination)
			else:
				shutil.copy(data_path, destination)

	@staticmethod
	def data_remove(array_path):
		pass

class RegressionBase(unittest.TestCase):

	def setUp(self):
		"""All the custom setup should be implemented by the developer
		"""
		self.casapy_script = None

	def tearDown(self):
		pass

	def assert_regression(self):
		"""A lazy method to assert the output if this method
		is not implementd in the child class.
		"""
		assert 1 > 2, "assertion failed..."

	def base_path(self, file):
		return "/".join(file.split("/")[:-1])

	def __script_path(self, script_module_path, script):
		"""Returnt the absolute path of the script
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
		module_path =  self.base_path(importlib.import_module(self.__module__).__file__)
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

	def execute(self, script = None, test_assert = False, import_module = False):
		"""Documentation, to be done
		2. will execute the casapy script (located in the same path where the test class module is)
		"""
		casapy_script = script if script else self.casapy_script

		if import_module:
			importlib.import_module("%s" % casapy_script)
		else:
			console_frame_globals = self.__console_globals()
			cexec_script = self.__script_path(self.__class_module_path(), casapy_script) # 
			execfile(cexec_script, console_frame_globals)

		if test_assert:
			self.assert_regression()

	@classmethod
	def setUpClass(class_instance):
		pass

	@classmethod
	def tearDownClass(class_instance):
		pass

class RegressionRunner:
	"""This class only implements static methods, intented to be used as
	a regression test runner
	"""

	def __init__(self):
		raise NotImplementedError("This class only implements static methods")

	@staticmethod
	def execute(test, nose_argv = None, guide = False):
		"""Execute the regression test by using nose with the nose arguments
		and with -d -s -v" and --with-xunit (xml generated)
		"""
		test_module_uri = "testc.regression" if not guide else "testc.guide"
		test_module = importlib.import_module("%s.%s" % (test_module_uri, test))

		

		if test_module.__dict__.has_key("__all__"):

			for test_class in test_module.__all__:
				test_object = getattr(test_module, test_module.__all__[0])
				test_suite = unittest.TestLoader().loadTestsFromTestCase(test_object)

				if nose_argv:
					test_argv = nose_argv
				else:
					test_argv = [
						test_module.__name__.lower(), 
						"-d",
						"-s",
						"-v",
						#"--processes=-1"
						"--with-xunit",
						"--xunit-file=%s.xml" % test_object.__name__.lower()
					]
				
				print nose.run(argv = test_argv, suite = test_suite)

		del test_module

#
# Within casa:
# from regression_utils import RegressionRunner
# RegressionRunner.execute_regression("regression_b0319")
#
if __name__ == "__main__":
	RegressionRunner.execute("regression_3c129_tutorial")