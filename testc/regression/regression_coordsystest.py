import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import unittest

from testc.regression.helper import RegressionHelper
from testc.regression.helper import RegressionBase

# define which classes within the module should be visible for testing
__all__ = ["Coordsystest"]

# in order to skip the test execution
# @unittest.skip("reason")
class Coordsystest(RegressionBase):
		
	# in order to skip the test execution
	#@unittest.skip("reason")
	def test_execution(self):
		#self.execute("exec_coordsystest")
		self.execute("casapy_coordsystest")