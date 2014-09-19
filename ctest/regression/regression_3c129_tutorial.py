import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import unittest

from regression_utils import RegressionHelper
from regression_utils import RegressionBase

# define which classes within the module should be visible for testing
__all__ = ["Tutorial3c219"]

# in order to skip the test execution
# @unittest.skip("reason")
class Tutorial3c219(RegressionBase):

	def setUp(self):
		self.cexec_module = "cexec_3c129_tutorial"
		
	# in order to skip the test execution
	#@unittest.skip("reason")
	def test_execution(self):
		self.execute()