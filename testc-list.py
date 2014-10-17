import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"
assert globals().has_key("IPython"), "IPython environment is needed for this module (%s)" % __file__
assert globals().has_key("casa"), "CASA environment is needed for this module (%s)" % __file__

import os

# to use psutil for nose psutil pluging
sys.path.append("/usr/lib/python2.6/site-packages/psutil-2.1.3-py2.6-linux-x86_64.egg")

from testc.regression.helper import RegressionRunner

# configure regression tests to execute
regressions = []

# configure guides tests to execute
guides = []
guides.append("regression_EVLA3BitTutorialG192Eg")

# test the regression
for test in regressions:
	RegressionRunner.execute(test)

# test the guides
for test in guides:
	RegressionRunner.execute(test, guide = True)

