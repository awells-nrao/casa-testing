import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import unittest

from test.regression.helper import RegressionHelper
from test.regression.helper import RegressionBase

# define which classes within the module should be visible for testing
__all__ = ["Coordsystest"]

# in order to skip the test execution
# @unittest.skip("reason")
class Coordsystest(RegressionBase):

	def setUpRegression(self):
		self.cexec_module = "cexec_coordsystest"
		
	# in order to skip the test execution
	#@unittest.skip("reason")
	def test_execution(self):
		#self.execute("exec_coordsystest")
		self.execute()