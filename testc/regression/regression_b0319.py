import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import unittest

from testc.regression.helper import RegressionHelper
from testc.regression.helper import RegressionBase

from casac import casac
from taskinit import casalog
from imageTest import * 
from visTest import * 
from testbase import *
from tableMaker import *

# define which classes within the module should be visible for testing
__all__ = ["B0319"]

# in order to skip the test execution
# @unittest.skip("reason")
class B0319(RegressionBase):

	def setUpRegression(self):
		self.casapy_script = "casapy_b0319"
		
	# in order to skip the test execution
	#@unittest.skip("reason")
	def test_execution(self):
		#self.execute("exec_coordsystest")
		self.execute()