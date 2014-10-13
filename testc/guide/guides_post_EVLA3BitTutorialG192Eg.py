"""
This is NOT a generated module
all modified changes will be kept.

The module provide to execute a method of the helper class by using the value
of "exec_method" key inserted at runtime in the globals map
"""

import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"
assert globals().has_key("IPython"), "IPython environment is needed for this module (%s)" % __file__
assert globals().has_key("casa"), "CASA environment is needed for this module (%s)" % __file__

import os

from testc.regression.helper import RegressionHelper
from testc.regression.helper import regressionLogger

import time

__test__ = False
__all__ = ["Post_Test_EVLA3BitTutorialG192Eg"]

class Post_Test_EVLA3BitTutorialG192Eg():
	"""Post class for EVLA_3-bit_Tutorial_G192 casa guide

	This is NOT an autogenerated class for EVLA_3-bit_Tutorial_G192 guide testing purposes,
	all the modified code will be kept.
	"""

	def exec_method(self, method_name):
		"""Execute a method from this object instance
		"""
		regressionLogger.debug("exec_method(self, %s):... sleeping 2 seconds" % method_name)
		# add a sleep of 2 seconds, for a visible separation for the ploting profile, this
		# should be improved
		time.sleep(2)
		getattr(self, method_name)()

	def post_00(self):
		"""post method for "splitting fields for analysis"
		"""
		RegressionHelper.assert_file("%s/G192_6s.ms" % os.getcwd())

	def post_01(self):
		"""post method for "listobs on the initial data set"
		"""
		listobs_md5sum0 = "8a17e860a4938774a652cbe6900c26c5"
		listobs_md5sum1 = RegressionHelper.md5sum("%s/G192_listobs.txt" % os.getcwd())

		# this should be done by the test class at @tearDownClass
		remove = []
		remove.append("%s/G192_listobs.txt" % os.getcwd())
		remove.append("%s/listobs.last" % os.getcwd())
		RegressionHelper.data_remove(remove)

		assert listobs_md5sum0 == listobs_md5sum1, "%s/G192_listobs.txt doesn't have the same content" % os.getcwd()
		
	def post_02(self):
		"""post method for "flag table plot"
		"""
		RegressionHelper.assert_file("%s/PlotG192_flagcmd_4.1.png" % os.getcwd())

	def post_03(self):
		"""post method for "bandpass calibrator analysis flagging"
		"""
		# file list and the content of the md5hash 
		flagcmd_files = {}
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_3/table.f1"] = "6eb9c409ecb931d6b84bab2c979219d8"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_3/table.info"] = "59a97223a30348c9f24282ec64cd9579"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_3/table.lock"] = "273a9ed34e8383bbc1d0405057bd6148"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_3/table.dat"] = "63109749c5ae002ba20f0759d99408e7"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_3/table.f0_TSM1"] = "7135e97ebfbf7cdf7f561be2e0823e84"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_3/table.f0"] = "600e8ee15675fbb651222b61526c4e3a"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_2/table.f1"] = "6eb9c409ecb931d6b84bab2c979219d8"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_2/table.info"] = "59a97223a30348c9f24282ec64cd9579"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_2/table.lock"] = "273a9ed34e8383bbc1d0405057bd6148"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_2/table.dat"] = "ee65b3885258c03e4bc76a81da77b8e0"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_2/table.f0_TSM1"] = "7135e97ebfbf7cdf7f561be2e0823e84"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_2/table.f0"] = "600e8ee15675fbb651222b61526c4e3a"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_5/table.f1"] = "6eb9c409ecb931d6b84bab2c979219d8"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_5/table.info"] = "59a97223a30348c9f24282ec64cd9579"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_5/table.lock"] = "273a9ed34e8383bbc1d0405057bd6148"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_5/table.dat"] = "d06ca8cde7edbfa688e1484de0b1d8b5"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_5/table.f0_TSM1"] = "7135e97ebfbf7cdf7f561be2e0823e84"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_5/table.f0"] = "600e8ee15675fbb651222b61526c4e3a"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_1/table.f1"] = "ffe1a7c00314babd5372f64100098a4b"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_1/table.info"] = "59a97223a30348c9f24282ec64cd9579"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_1/table.lock"] = "273a9ed34e8383bbc1d0405057bd6148"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_1/table.dat"] = "f3c62d5a3b5336d417fe5d95ff7e6831"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_1/table.f0_TSM1"] = "358d71f5dd5ae6692617cecd0f56b865"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_1/table.f0"] = "600e8ee15675fbb651222b61526c4e3a"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_4/table.f1"] = "6eb9c409ecb931d6b84bab2c979219d8"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_4/table.info"] = "59a97223a30348c9f24282ec64cd9579"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_4/table.lock"] = "273a9ed34e8383bbc1d0405057bd6148"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_4/table.dat"] = "a59e31add290ddfea0a75727a892792c"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_4/table.f0_TSM1"] = "7135e97ebfbf7cdf7f561be2e0823e84"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_4/table.f0"] = "600e8ee15675fbb651222b61526c4e3a"
		# FLAG_VERSION_LIST includes a timestamp written at runtime
		flagcmd_files["G192_6s.ms.flagversions/FLAG_VERSION_LIST"] = None

		# assert that all output files exist
		for output_file in flagcmd_files.keys():
			RegressionHelper.assert_file("%s/%s" % (os.getcwd(), output_file))

		# the approach is to compare the md5check sum, different content, different checksum
		for items in flagcmd_files.items():
			if items[1]:
				item_file = "%s/%s" % (os.getcwd(), items[0])
				item_md5sum = RegressionHelper.md5sum(item_file)
				assert items[1] == item_md5sum, "%s doesn't have the same content" % (item_file)

		# this should be done by the test class at @tearDownClass
		remove = []
		remove.append("%s/G192_6s.ms.flagversions" % os.getcwd())
		RegressionHelper.data_remove(remove)

	def post_04(self):
		"""post method for "RFI phase calibrator flagging"
		"""
		# file list and the content of the md5hash 
		flagcmd_files = {}
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_1/table.f1"] = "6eb9c409ecb931d6b84bab2c979219d8"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_1/table.info"] = "59a97223a30348c9f24282ec64cd9579"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_1/table.lock"] = "273a9ed34e8383bbc1d0405057bd6148"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_1/table.dat"] = "f3c62d5a3b5336d417fe5d95ff7e6831"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_1/table.f0_TSM1"] = "3544a1521b82ce73ab6c42426b8e143d"
		flagcmd_files["G192_6s.ms.flagversions/flags.flagcmd_1/table.f0"] = "600e8ee15675fbb651222b61526c4e3a"
		# FLAG_VERSION_LIST includes a timestamp written at runtime
		flagcmd_files["G192_6s.ms.flagversions/FLAG_VERSION_LIST"] = None

		

	def post_05(self):
		"""post method for "splitting good and bad data"
		"""
		assert True, "dummy assert"

	def post_06(self):
		"""post method for "split and flagged listobs"
		"""
		assert True, "dummy assert"

	def post_07(self):
		"""post method for "model for the flux calibrator"
		"""
		assert True, "dummy assert"

	def post_08(self):
		"""post method for "determining antenna position corrections"
		"""
		assert True, "dummy assert"

	def post_09(self):
		"""post method for "generating gaincurve calibration"
		"""
		assert True, "dummy assert"

	def post_10(self):
		"""post method for "generate atmospheric opacity calibration"
		"""
		assert True, "dummy assert"

	def post_11(self):
		"""post method for "generate requantizer gains corrections"
		"""
		assert True, "dummy assert"

	def post_12(self):
		"""post method for "phase only calibration"
		"""
		assert True, "dummy assert"

	def post_13(self):
		"""post method for "residual delays"
		"""
		assert True, "dummy assert"

	def post_14(self):
		"""post method for "antenna bandpasses"
		"""
		assert True, "dummy assert"

	def post_15(self):
		"""post method for "flux and bandpass calibrators gain"
		"""
		assert True, "dummy assert"

	def post_16(self):
		"""post method for "bandpass calibrator gain amplitudes scaling"
		"""
		assert True, "dummy assert"

	def post_17(self):
		"""post method for "spectral information"
		"""
		assert True, "dummy assert"

	def post_18(self):
		"""post method for "phase only recalibration"
		"""
		assert True, "dummy assert"

	def post_19(self):
		"""post method for "residual delays recalibration"
		"""
		assert True, "dummy assert"

	def post_20(self):
		"""post method for "antenna bandpasses recalibration"
		"""
		assert True, "dummy assert"

	def post_21(self):
		"""post method for "compute gain phases using 3C147"
		"""
		assert True, "dummy assert"

	def post_22(self):
		"""post method for "compute gain phases using J0603+174"
		"""
		assert True, "dummy assert"

	def post_23(self):
		"""post method for "compute gain phases using 3C84"
		"""
		assert True, "dummy assert"

	def post_24(self):
		"""post method for "applying phase calibration"
		"""
		assert True, "dummy assert"

	def post_25(self):
		"""post method for "3C147 scan solving amplitudes"
		"""
		assert True, "dummy assert"

	def post_26(self):
		"""post method for "J0603+174  scan solving amplitudes"
		"""
		assert True, "dummy assert"

	def post_27(self):
		"""post method for "3C84 scan solving amplitudes"
		"""
		assert True, "dummy assert"

	def post_28(self):
		"""post method for "using fluxscale to transfer the amplitude solutions"
		"""
		assert True, "dummy assert"

	def post_29(self):
		"""post method for "3C147 accumulated calibration"
		"""
		assert True, "dummy assert"

	def post_30(self):
		"""post method for "gain accumulated calibration"
		"""
		assert True, "dummy assert"

	def post_31(self):
		"""post method for "G192 accumulated calibration"
		"""
		assert True, "dummy assert"

	def post_32(self):
		"""post method for "3C84 accumulated calibration"
		"""
		assert True, "dummy assert"

	def post_33(self):
		"""post method for "flagging isolated RFI"
		"""
		assert True, "dummy assert"

	def post_34(self):
		"""post method for "baseline flagging"
		"""
		assert True, "dummy assert"

	def post_35(self):
		"""post method for "3C147 density model"
		"""
		assert True, "dummy assert"

	def post_36(self):
		"""post method for "3C84 spectral information column"
		"""
		assert True, "dummy assert"

	def post_37(self):
		"""post method for "initial phase calibration"
		"""
		assert True, "dummy assert"

	def post_38(self):
		"""post method for "delay calibration"
		"""
		assert True, "dummy assert"

	def post_39(self):
		"""post method for "bandpass calibration"
		"""
		assert True, "dummy assert"

	def post_40(self):
		"""post method for "phase gain calibration field 0"
		"""
		assert True, "dummy assert"

	def post_41(self):
		"""post method for "phase gain calibration field 1"
		"""
		assert True, "dummy assert"

	def post_42(self):
		"""post method for "phase gain calibration field 3"
		"""
		assert True, "dummy assert"

	def post_43(self):
		"""post method for "phase gain calibration infinite solution interval"
		"""
		assert True, "dummy assert"

	def post_44(self):
		"""post method for "amplitude calibration solutions field 0"
		"""
		assert True, "dummy assert"

	def post_45(self):
		"""post method for "amplitude calibration solutions field 1"
		"""
		assert True, "dummy assert"

	def post_46(self):
		"""post method for "amplitude calibration solutions field 3"
		"""
		assert True, "dummy assert"

	def post_47(self):
		"""post method for "flux calibration solutions"
		"""
		assert True, "dummy assert"

	def post_48(self):
		"""post method for "apply calibration tables field 0"
		"""
		assert True, "dummy assert"

	def post_49(self):
		"""post method for "apply calibration tables field 1"
		"""
		assert True, "dummy assert"

	def post_50(self):
		"""post method for "apply calibration tables field 2"
		"""
		assert True, "dummy assert"

	def post_51(self):
		"""post method for "apply calibration tables field 3"
		"""
		assert True, "dummy assert"

	def post_52(self):
		"""post method for "splitting calibrated data 3C147"
		"""
		assert True, "dummy assert"

	def post_53(self):
		"""post method for "splitting calibrated data J0603+174"
		"""
		assert True, "dummy assert"

	def post_54(self):
		"""post method for "splitting calibrated data G192"
		"""
		assert True, "dummy assert"

	def post_55(self):
		"""post method for "splitting calibrated data 3C84"
		"""
		assert True, "dummy assert"

	def post_56(self):
		"""post method for "single spectral window cleaning"
		"""
		assert True, "dummy assert"

	def post_57(self):
		"""post method for "lower frequency baseband cleaning"
		"""
		assert True, "dummy assert"

	def post_58(self):
		"""post method for "upper frequency baseband cleaning"
		"""
		assert True, "dummy assert"

	def post_59(self):
		"""post method for "basebands mfs taylor cleaning"
		"""
		assert True, "dummy assert"

	def post_60(self):
		"""post method for "spectral index image filtering"
		"""
		assert True, "dummy assert"

	def post_61(self):
		"""post method for "spectral index probable errors filtering"
		"""
		assert True, "dummy assert"

	def post_62(self):
		"""post method for "intensity weighted mean spectral analysis"
		"""
		assert True, "dummy assert"	

if __name__ == "__main__":
	method_name = globals()["exec_method"]
	assert len(method_name), "method name not defined"
	helper_instance = Post_Test_EVLA3BitTutorialG192Eg()
	helper_instance.exec_method(method_name)