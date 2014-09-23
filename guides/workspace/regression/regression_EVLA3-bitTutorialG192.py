#!/usr/bin/env python

# This is a generated module
# all modified changes will be lost in the next code generation

# Defined keyword-phrases 
# keyword-phrase: "initial data split" 
# keyword-phrase: "initial listobs run" 
# keyword-phrase: "creating a plot of the already flagged data" 

import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import unittest

from test.regression.helper import RegressionHelper
from test.regression.helper import RegressionBase

__all__ = ["Test_EVLA3bitTutorialG192"]

class Test_EVLA3bitTutorialG192(RegressionBase):
	""" Testing CASA EVLA3-bitTutorialG192
	"""

	@classmethod
	def setUpClass(class_instance):
		pass

	def setUp(self):
		pass

	def tearDown(self):
		pass

	@classmethod
	def tearDown(class_instance):
		pass

	def test_EVLA3bitTutorialG192_00_initial_data_split(self):
		"""EVLA3-bitTutorialG192 testing keyword-phrase: initial data split
		it will execute the generated cexec_EVLA3bitTutorialG192_00_initial_data_split.py script
		"""
		self.execute("cexec_EVLA3bitTutorialG192_00_initial_data_split")

	def test_EVLA3bitTutorialG192_01_initial_listobs_run(self):
		"""EVLA3-bitTutorialG192 testing keyword-phrase: initial listobs run
		it will execute the generated cexec_EVLA3bitTutorialG192_01_initial_listobs_run.py script
		"""
		self.execute("cexec_EVLA3bitTutorialG192_01_initial_listobs_run")

	def test_EVLA3bitTutorialG192_02_creating_a_plot_of_the_already_flagged_data(self):
		"""EVLA3-bitTutorialG192 testing keyword-phrase: creating a plot of the already flagged data
		it will execute the generated cexec_EVLA3bitTutorialG192_02_creating_a_plot_of_the_already_flagged_data.py script
		"""
		self.execute("cexec_EVLA3bitTutorialG192_02_creating_a_plot_of_the_already_flagged_data")
