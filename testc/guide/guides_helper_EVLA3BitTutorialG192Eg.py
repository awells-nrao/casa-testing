"""
This is a generated module
all modified changes will be lost in the next code generation

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

__test__ = False
__all__ = ["Helper_Test_EVLA3BitTutorialG192Eg"]

class Helper_Test_EVLA3BitTutorialG192Eg():
	"""Helper class for EVLA_3-bit_Tutorial_G192 casa guide

	This is an autogenerated class for EVLA_3-bit_Tutorial_G192 guide testing purposes,
	all the modified code will be re-written in the next code generation.

	The class will help the following phrases:

	test_00 "splitting fields for analysis"
	test_01 "listobs on the initial data set"
	test_02 "flag table plot"
	test_03 "bandpass calibrator analysis flagging"
	test_04 "RFI phase calibrator flagging"
	test_05 "splitting good and bad data"
	test_06 "split and flagged listobs"
	test_07 "model for the flux calibrator"
	test_08 "determining antenna position corrections"
	test_09 "generating gaincurve calibration"
	test_10 "generate atmospheric opacity calibration"
	test_11 "generate requantizer gains corrections"
	test_12 "phase only calibration"
	test_13 "residual delays"
	test_14 "antenna bandpasses"
	test_15 "flux and bandpass calibrators gain"
	test_16 "bandpass calibrator gain amplitudes scaling"
	test_17 "spectral information"
	test_18 "phase only recalibration"
	test_19 "residual delays recalibration"
	test_20 "antenna bandpasses recalibration"
	test_21 "compute gain phases using 3C147"
	test_22 "compute gain phases using J0603+174"
	test_23 "compute gain phases using 3C84"
	test_24 "applying phase calibration"
	test_25 "3C147 scan solving amplitudes"
	test_26 "J0603+174  scan solving amplitudes"
	test_27 "3C84 scan solving amplitudes"
	test_28 "using fluxscale to transfer the amplitude solutions"
	test_29 "3C147 accumulated calibration"
	test_30 "gain accumulated calibration"
	test_31 "G192 accumulated calibration"
	test_32 "3C84 accumulated calibration"
	test_33 "flagging isolated RFI"
	test_34 "baseline flagging"
	test_35 "3C147 density model"
	test_36 "3C84 spectral information column"
	test_37 "initial phase calibration"
	test_38 "delay calibration"
	test_39 "bandpass calibration"
	test_40 "phase gain calibration field 0"
	test_41 "phase gain calibration field 1"
	test_42 "phase gain calibration field 3"
	test_43 "phase gain calibration infinite solution interval"
	test_44 "amplitude calibration solutions field 0"
	test_45 "amplitude calibration solutions field 1"
	test_46 "amplitude calibration solutions field 3"
	test_47 "flux calibration solutions"
	test_48 "apply calibration tables field 0"
	test_49 "apply calibration tables field 1"
	test_50 "apply calibration tables field 2"
	test_51 "apply calibration tables field 3"
	test_52 "splitting calibrated data 3C147"
	test_53 "splitting calibrated data J0603+174"
	test_54 "splitting calibrated data G192"
	test_55 "splitting calibrated data 3C84"
	test_56 "single spectral window cleaning"
	test_57 "lower frequency baseband cleaning"
	test_58 "upper frequency baseband cleaning"
	test_59 "basebands mfs taylor cleaning"
	test_60 "spectral index image filtering"
	test_61 "spectral index probable errors filtering"
	test_62 "intensity weighted mean spectral analysis"
	"""

	def exec_method(self, method_name):
		"""Execute a method from this object instance
		"""
		regressionLogger.debug("exec_method(self, %s):..." % method_name)
		getattr(self, method_name)()

	def helper_00(self): 
		""" helper method for "splitting fields for analysis"
		"""
		split('TVER0004.sb14459364.eb14492359.56295.26287841435.ms', outputvis='G192_6s.ms', \
		      datacolumn='all', field='3,6,7,10', keepflags=False, spw='2~65')

	def helper_01(self): 
		""" helper method for "listobs on the initial data set"
		"""
		listobs('G192_6s.ms', listfile='G192_listobs.txt')

	def helper_02(self): 
		""" helper method for "flag table plot"
		"""
		myrows = range(2868)
		flagcmd(vis='G192_6s.ms', inpmode='table', action='plot', tablerows=myrows,
		        useapplied=True, plotfile='PlotG192_flagcmd_4.1.png')

	def helper_03(self): 
		""" helper method for "bandpass calibrator analysis flagging"
		"""
		flaglist = ['antenna="ea01,ea10,ea19,ea13"',
		            'antenna="ea24" spw="40,47~48"',
		            'antenna="ea18" spw="16~31"']
		flagcmd(vis='G192_6s.ms', inpmode='list', inpfile=flaglist, \
		        action='apply', flagbackup=True)

	def helper_04(self): 
		""" helper method for "RFI phase calibrator flagging"
		"""
		flaglist = ['spw="33:124,37:91,38:66~67;75~77,46:126,48:0"', \
		            'spw="53:68~69,63:80,10:26,15:127,27:62,27:64"']
		flagcmd(vis='G192_6s.ms', inpmode='list', inpfile=flaglist, \
		        action='apply', flagbackup=True)

	def helper_05(self): 
		""" helper method for "splitting good and bad data"
		"""
		# Remove any existing split data, otherwise split will not happen
		os.system('rm -rf G192_flagged_6s.ms')
		split(vis='G192_6s.ms', outputvis='G192_flagged_6s.ms', \
		      datacolumn='data', keepflags=False)

	def helper_06(self): 
		""" helper method for "split and flagged listobs"
		"""
		listobs('G192_flagged_6s.ms', listfile='G192_flagged_listobs.txt')

	def helper_07(self): 
		""" helper method for "model for the flux calibrator"
		"""
		setjy(vis='G192_flagged_6s.ms', field='0', scalebychan=True, \
		      model='3C147_A.im')

	def helper_08(self): 
		""" helper method for "determining antenna position corrections"
		"""
		gencal('G192_flagged_6s.ms', caltable='calG192.antpos', \
		       caltype='antpos', antenna='')

	def helper_09(self): 
		""" helper method for "generating gaincurve calibration"
		"""
		gencal('G192_flagged_6s.ms', caltable='calG192.gaincurve', \
		       caltype='gc')

	def helper_10(self): 
		""" helper method for "generate atmospheric opacity calibration"
		"""
		myTau = plotweather(vis='G192_flagged_6s.ms', doPlot=T)
		SPWs = []
		for window in range(0,64):
			SPWs.append(str(window))
		spwString = ','.join(SPWs)
		gencal(vis='G192_flagged_6s.ms', caltable='calG192.opacity',
		       caltype='opac', spw=spwString, parameter=myTau)

	def helper_11(self): 
		""" helper method for "generate requantizer gains corrections"
		"""
		gencal('G192_flagged_6s.ms', caltable='calG192.requantizer', \
		       caltype='rq')

	def helper_12(self): 
		""" helper method for "phase only calibration"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G0', \
		        field='3', spw='*:60~68', \
		        gaintable=['calG192.antpos','calG192.gaincurve', \
		                   'calG192.requantizer','calG192.opacity'], \
		        gaintype='G', refant='ea05', calmode='p', \
		        solint='int', minsnr=3)

	def helper_13(self): 
		""" helper method for "residual delays"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.K0', \
		        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
		                   'calG192.opacity', 'calG192.G0'], \
		        field='3', spw='*:5~122', gaintype='K', \
		        refant='ea05', solint='inf', minsnr=3)

	def helper_14(self): 
		""" helper method for "antenna bandpasses"
		"""
		bandpass(vis='G192_flagged_6s.ms', caltable='calG192.B0', \
		         gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
		                    'calG192.opacity', 'calG192.G0', 'calG192.K0'], \
		         field='3', refant='ea05', solnorm=False, \
		         bandtype='B', solint='inf')

	def helper_15(self): 
		""" helper method for "flux and bandpass calibrators gain"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1', field='0,3', \
		        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
		                   'calG192.opacity', 'calG192.K0', \
		                   'calG192.B0'], \
		        gaintype='G', refant='ea05', calmode='ap', solint='30s', minsnr=3)

	def helper_16(self): 
		""" helper method for "bandpass calibrator gain amplitudes scaling"
		"""
		flux1 = fluxscale(vis='G192_flagged_6s.ms', caltable='calG192.G1', \
		                  fluxtable='calG192.F1', reference='0', \
		                  transfer='3', listfile='3C84.fluxinfo', fitorder=1)

	def helper_17(self): 
		""" helper method for "spectral information"
		"""
		setjy(vis='G192_flagged_6s.ms', field='3', scalebychan=True, \
		      fluxdensity=[29.8756, 0, 0, 0], spix=-0.598929, \
		      reffreq='32.4488GHz')

	def helper_18(self): 
		""" helper method for "phase only recalibration"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G0.b', \
		        field='3', spw='*:60~68', \
		        gaintable=['calG192.antpos', 'calG192.gaincurve', \
		                   'calG192.requantizer', 'calG192.opacity'], \
		        gaintype='G', refant='ea05', calmode='p', \
		        solint='int', minsnr=3)

	def helper_19(self): 
		""" helper method for "residual delays recalibration"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.K0.b', \
		        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
		                  'calG192.opacity', 'calG192.G0.b'], \
		        field='3', spw='*:5~122', gaintype='K', \
		        refant='ea05', solint='inf', minsnr=3)

	def helper_20(self): 
		""" helper method for "antenna bandpasses recalibration"
		"""
		bandpass(vis='G192_flagged_6s.ms', caltable='calG192.B0.b', \
		         gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
		                    'calG192.opacity', 'calG192.G0.b', 'calG192.K0.b'], \
		         field='3', refant='ea05', solnorm=False, \
		         bandtype='B', solint='inf')

	def helper_21(self): 
		""" helper method for "compute gain phases using 3C147"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int', \
		        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
		                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b'], \
		        field='0', refant='ea05', solnorm=F, \
		        solint='int', gaintype='G', calmode='p')

	def helper_22(self): 
		""" helper method for "compute gain phases using J0603+174"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int', \
		        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
		                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b'], \
		        field='1', refant='ea05', solnorm=F, \
		        solint='12s', gaintype='G', calmode='p', append=True)

	def helper_23(self): 
		""" helper method for "compute gain phases using 3C84"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int', \
		        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
		                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b'], \
		        field='3', refant='ea05', solnorm=F, \
		        solint='int', gaintype='G', calmode='p', append=True)

	def helper_24(self): 
		""" helper method for "applying phase calibration"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.inf', \
		        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
		                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b'], \
		        field='1', refant='ea05', solnorm=F, \
		        solint='inf', gaintype='G', calmode='p')

	def helper_25(self): 
		""" helper method for "3C147 scan solving amplitudes"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2', \
		        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
		                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', 'calG192.G1.int'], \
		        gainfield=['', '', '', '', '3', '3', '0'], \
		        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
		        field='0', refant='ea05', solnorm=F, \
		        solint='inf', gaintype='G', calmode='a')

	def helper_26(self): 
		""" helper method for "J0603+174  scan solving amplitudes"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2', \
		        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
		                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', 'calG192.G1.int'], \
		        gainfield=['', '', '', '', '3', '3', '1'], \
		        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
		        field='1', refant='ea05', solnorm=F, \
		        solint='inf', gaintype='G', calmode='a', append=True)

	def helper_27(self): 
		""" helper method for "3C84 scan solving amplitudes"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2', \
		        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
		                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', 'calG192.G1.int'], \
		        gainfield=['', '', '', '', '3', '3', '3'], \
		        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
		        field='3', refant='ea05', solnorm=F, \
		        solint='inf', gaintype='G', calmode='a', append=True)
		#

	def helper_28(self): 
		""" helper method for "using fluxscale to transfer the amplitude solutions"
		"""
		flux2 = fluxscale(vis='G192_flagged_6s.ms', caltable='calG192.G2', \
		                  fluxtable='calG192.F2', reference='0')

	def helper_29(self): 
		""" helper method for "3C147 accumulated calibration"
		"""
		applycal(vis='G192_flagged_6s.ms', field='0', \
		         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
		                    'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', \
		                    'calG192.G1.int', 'calG192.G2'], \
		         gainfield=['', '', '', '', '', '', '0', '0'],
		         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)

	def helper_30(self): 
		""" helper method for "gain accumulated calibration"
		"""
		applycal(vis='G192_flagged_6s.ms', field='1', \
		         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
		                    'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', \
		                    'calG192.G1.int', 'calG192.F2'], \
		         gainfield=['', '', '', '', '', '', '1', '1'],
		         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)

	def helper_31(self): 
		""" helper method for "G192 accumulated calibration"
		"""
		applycal(vis='G192_flagged_6s.ms', field='2', \
		         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
		                    'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b',\
		                    'calG192.G1.inf', 'calG192.F2'], \
		         gainfield=['', '', '', '', '', '', '1', '1'],
		         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'linear'], calwt=False)

	def helper_32(self): 
		""" helper method for "3C84 accumulated calibration"
		"""
		applycal(vis='G192_flagged_6s.ms', field='3', \
		         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
		                    'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', \
		                    'calG192.G1.int', 'calG192.F2'], \
		         gainfield=['', '', '', '', '', '', '3', '3'],
		         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)

	def helper_33(self): 
		""" helper method for "flagging isolated RFI"
		"""
		flagdata(vis='G192_flagged_6s.ms', field='0', \
		         spw='29', timerange='6:35:00~6:36:40')

	def helper_34(self): 
		""" helper method for "baseline flagging"
		"""
		flagdata(vis='G192_flagged_6s.ms', antenna='ea03&ea07')

	def helper_35(self): 
		""" helper method for "3C147 density model"
		"""
		setjy(vis='G192_flagged_6s.ms', field='0', scalebychan=True, \
		      model='3C147_A.im')

	def helper_36(self): 
		""" helper method for "3C84 spectral information column"
		"""
		setjy(vis='G192_flagged_6s.ms', field='3', scalebychan=True, \
		      fluxdensity=[29.8756, 0, 0, 0], spix=-0.598929, \
		      reffreq='32.4488GHz')

	def helper_37(self): 
		""" helper method for "initial phase calibration"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G0.b.2', field='3', spw='*:60~68',\
		        gaintable=['calG192.antpos', 'calG192.gaincurve', \
		                  'calG192.requantizer', 'calG192.opacity'], \
		        gaintype='G', refant='ea05', calmode='p', solint='int', minsnr=3)

	def helper_38(self): 
		""" helper method for "delay calibration"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.K0.b.2', \
		        field='3', spw='*:5~122', gaintype='K', \
		        gaintable=['calG192.antpos', 'calG192.gaincurve', \
		                  'calG192.requantizer', 'calG192.opacity','calG192.G0.b.2'], \
		        refant='ea05', solint='inf', minsnr=3)

	def helper_39(self): 
		""" helper method for "bandpass calibration"
		"""
		bandpass(vis='G192_flagged_6s.ms', caltable='calG192.B0.b.2', \
		         field='3', refant='ea05', solnorm=False, \
		        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer',\
		                   'calG192.opacity','calG192.G0.b.2', 'calG192.K0.b.2'], \
		         bandtype='B', solint='inf')

	def helper_40(self): 
		""" helper method for "phase gain calibration field 0"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int.2', \
		        field='0', refant='ea05', solnorm=F, \
		        gaintable=['calG192.antpos', 'calG192.requantizer','calG192.gaincurve', \
		                   'calG192.opacity', 'calG192.K0.b.2','calG192.B0.b.2'], \
		        solint='int', gaintype='G', calmode='p')

	def helper_41(self): 
		""" helper method for "phase gain calibration field 1"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int.2', \
		        field='1', refant='ea05', solnorm=F, \
		        gaintable=['calG192.antpos', 'calG192.requantizer','calG192.gaincurve', \
		                   'calG192.opacity', 'calG192.K0.b.2','calG192.B0.b.2'], \
		        solint='12s', gaintype='G', calmode='p', append=True)

	def helper_42(self): 
		""" helper method for "phase gain calibration field 3"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int.2', \
		        field='3', refant='ea05', solnorm=F, \
		        gaintable=['calG192.antpos', 'calG192.requantizer','calG192.gaincurve', \
		                   'calG192.opacity', 'calG192.K0.b.2','calG192.B0.b.2'], \
		        solint='int', gaintype='G', calmode='p', append=True)

	def helper_43(self): 
		""" helper method for "phase gain calibration infinite solution interval"
		"""
		# (Note: we will apply this table to our science target at the applycal stage.)
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.inf.2', \
		        field='1', refant='ea05', solnorm=F, \
		        gaintable=['calG192.antpos', 'calG192.requantizer','calG192.gaincurve', \
		                   'calG192.opacity', 'calG192.K0.b.2','calG192.B0.b.2'], \
		        solint='inf', gaintype='G', calmode='p')

	def helper_44(self): 
		""" helper method for "amplitude calibration solutions field 0"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2.2', \
		        field='0', refant='ea05', solnorm=F, \
		        gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
		                   'calG192.opacity', 'calG192.K0.b.2', \
		                   'calG192.B0.b.2', 'calG192.G1.int.2'], \
		        gainfield=['', '', '', '', '3', '3', '0'], \
		        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
		        solint='inf', gaintype='G', calmode='a')

	def helper_45(self): 
		""" helper method for "amplitude calibration solutions field 1"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2.2', \
		        field='1', refant='ea05', solnorm=F, \
		        gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
		                   'calG192.opacity', 'calG192.K0.b.2', \
		                   'calG192.B0.b.2', 'calG192.G1.int.2'], \
		        gainfield=['', '', '', '', '3', '3', '1'], \
		        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
		        solint='inf', gaintype='G', calmode='a', append=True)

	def helper_46(self): 
		""" helper method for "amplitude calibration solutions field 3"
		"""
		gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2.2', \
		        field='3', refant='ea05', solnorm=F, \
		        gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
		                   'calG192.opacity', 'calG192.K0.b.2', \
		                   'calG192.B0.b.2', 'calG192.G1.int.2'], \
		        gainfield=['', '', '', '', '3', '3', '3'], \
		        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
		        solint='inf', gaintype='G', calmode='a', append=True)

	def helper_47(self): 
		""" helper method for "flux calibration solutions"
		"""
		flux3 = fluxscale(vis='G192_flagged_6s.ms', caltable='calG192.G2.2', \
		                  fluxtable='calG192.F2.2', reference='0')

	def helper_48(self): 
		""" helper method for "apply calibration tables field 0"
		"""
		applycal(vis='G192_flagged_6s.ms', field='0', \
		         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', 'calG192.opacity',\
		                    'calG192.K0.b.2', 'calG192.B0.b.2', 'calG192.G1.int.2', 'calG192.G2.2'], \
		         gainfield=['', '', '', '', '', '', '0', '0'], \
		         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)

	def helper_49(self): 
		""" helper method for "apply calibration tables field 1"
		"""
		applycal(vis='G192_flagged_6s.ms', field='1', \
		         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', 'calG192.opacity',\
		                    'calG192.K0.b.2', 'calG192.B0.b.2', 'calG192.G1.int.2', 'calG192.F2.2'], \
		         gainfield=['', '', '', '', '', '', '1', '1'], \
		         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)

	def helper_50(self): 
		""" helper method for "apply calibration tables field 2"
		"""
		applycal(vis='G192_flagged_6s.ms', field='2', \
		         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', 'calG192.opacity',\
		                    'calG192.K0.b.2', 'calG192.B0.b.2', 'calG192.G1.inf.2', 'calG192.F2.2'], \
		         gainfield=['', '', '', '', '', '', '1', '1'], \
		         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'linear'], calwt=False)

	def helper_51(self): 
		""" helper method for "apply calibration tables field 3"
		"""
		applycal(vis='G192_flagged_6s.ms', field='3', \
		         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', 'calG192.opacity',\
		                    'calG192.K0.b.2', 'calG192.B0.b.2', 'calG192.G1.int.2', 'calG192.F2.2'], \
		         gainfield=['', '', '', '', '', '', '3', '3'], \
		         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)

	def helper_52(self): 
		""" helper method for "splitting calibrated data 3C147"
		"""
		os.system('rm -rf 3C147_split_6s.ms')
		split(vis='G192_flagged_6s.ms', outputvis='3C147_split_6s.ms', \
		      datacolumn='corrected', field='0')
		#

	def helper_53(self): 
		""" helper method for "splitting calibrated data J0603+174"
		"""
		os.system('rm -rf J0603_split_6s.ms')
		split(vis='G192_flagged_6s.ms', outputvis='J0603_split_6s.ms', \
		      datacolumn='corrected', field='1')
		#

	def helper_54(self): 
		""" helper method for "splitting calibrated data G192"
		"""
		os.system('rm -rf G192_split_6s.ms')
		split(vis='G192_flagged_6s.ms', outputvis='G192_split_6s.ms', \
		      datacolumn='corrected', field='2')
		#

	def helper_55(self): 
		""" helper method for "splitting calibrated data 3C84"
		"""
		os.system('rm -rf 3C84_split_6s.ms')
		split(vis='G192_flagged_6s.ms', outputvis='3C84_split_6s.ms', \
		      datacolumn='corrected', field='3')

	def helper_56(self): 
		""" helper method for "single spectral window cleaning"
		"""
		clean(vis='G192_split_6s.ms', spw='48:5~122', \
		      imagename='imgG192_6s_spw48', \
		      mode='mfs', nterms=1, niter=10000, \
		      imsize=[1280], cell=['0.015arcsec'], \
		      imagermode='csclean', cyclefactor=1.5, \
		      weighting='briggs', robust=0.5, \
		      interactive=True)

	def helper_57(self): 
		""" helper method for "lower frequency baseband cleaning"
		"""
		clean(vis='G192_split_6s.ms', spw='32~63:5~122', \
		      imagename='imgG192_6s_spw32-63', \
		      mode='mfs', nterms=1, niter=10000, \
		      imsize=[1280], cell=['0.015arcsec'], \
		      imagermode='csclean', cyclefactor=1.5, \
		      weighting='briggs', robust=0.5, \
		      interactive=True)
		#
		viewer('imgG192_6s_spw32-63.image')
		print r'''Command: viewer('imgG192_6s_spw32-63.image')'''
		user_check=raw_input('When you are done with the window, close it and press enter to continue:')
		mystat = imstat('imgG192_6s_spw32-63.residual')
		print 'Residual standard deviation = '+str(mystat['sigma'][0]) + ' Jy'

	def helper_58(self): 
		""" helper method for "upper frequency baseband cleaning"
		"""
		clean(vis='G192_split_6s.ms', spw='0~31:5~122', \
		      imagename='imgG192_6s_spw0-31', \
		      mode='mfs', nterms=1, niter=10000, \
		      imsize=[1280], cell=['0.015arcsec'], \
		      imagermode='csclean', cyclefactor=1.5, \
		      weighting='briggs', robust=0.5, \
		      interactive=True)
		#
		viewer('imgG192_6s_spw0-31.image')
		print r'''Command: viewer('imgG192_6s_spw0-31.image')'''
		user_check=raw_input('When you are done with the window, close it and press enter to continue:')
		mystat = imstat('imgG192_6s_spw0-31.residual')
		print 'Residual standard deviation = '+str(mystat['sigma'][0]) + ' Jy'
		myfit = imfit('imgG192_6s_spw0-31.image', region='G192.crtf')
		print 'Source flux = '+str(myfit['results']['component0']['flux']['value'][0])+'+/-'+str(myfit['results']['component0']['flux']['error'][0]) + ' Jy'

	def helper_59(self): 
		""" helper method for "basebands mfs taylor cleaning"
		"""
		clean(vis='G192_split_6s.ms', spw='0~63:5~122', \
		      imagename='imgG192_6s_spw0-63_mfs2', \
		      mode='mfs', nterms=2, niter=10000, gain=0.1, \
		      threshold='0.0mJy', psfmode='clark', imsize=[1280], \
		      cell=['0.015arcsec'], \
		      weighting='briggs', robust=0.5, interactive=True)
		#
		mystat = imstat('imgG192_6s_spw0-63_mfs2.residual.tt0') + ' Jy'
		print 'Residual standard deviation = '+str(mystat['sigma'][0])
		myfit = imfit('imgG192_6s_spw0-63_mfs2.image.tt0', region='G192.crtf') + ' Jy'
		print 'Source flux = '+str(myfit['results']['component0']['flux']['value'][0])+'+/-'+str(myfit['results']['component0']['flux']['error'][0])

	def helper_60(self): 
		""" helper method for "spectral index image filtering"
		"""
		immath(imagename=['imgG192_6s_spw0-63_mfs2.image.alpha',
		                  'imgG192_6s_spw0-63_mfs2.image.tt0'],
		       mode='evalexpr',
		       expr='IM0[IM1>2.0E-4]',
		       outfile='imgG192_6s_spw0-63_mfs2.image.alpha.filtered')

	def helper_61(self): 
		""" helper method for "spectral index probable errors filtering"
		"""
		immath(imagename=['imgG192_6s_spw0-63_mfs2.image.alpha.error',
		                  'imgG192_6s_spw0-63_mfs2.image.tt0'],
		       mode='evalexpr',
		       expr='IM0[IM1>2E-4]',
		       outfile='imgG192_6s_spw0-63_mfs2.image.alpha.error.filtered')

	def helper_62(self): 
		""" helper method for "intensity weighted mean spectral analysis"
		"""
		immath(imagename=['imgG192_6s_spw0-63_mfs2.image.tt1',
		                  'imgG192_6s_spw0-63_mfs2.image.tt0'],
		       mode='evalexpr',
		       expr='IM0[IM1>2E-4]',
		       outfile='imgG192_6s_spw0-63_mfs2.image.tt1.filtered')
		#
		# Removing any file output from previous runs, so immath will proceed
		os.system('rm -rf imgG192_6s_spw0-63_mfs2.image.tt0.filtered')
		immath(imagename=['imgG192_6s_spw0-63_mfs2.image.tt0'],
		       mode='evalexpr',
		       expr='IM0[IM0>2E-4]',
		       outfile='imgG192_6s_spw0-63_mfs2.image.tt0.filtered')

if __name__ == "__main__":
	method_name = globals()["exec_method"]
	assert len(method_name), "method name not defined"
	helper_instance = Helper_Test_EVLA3BitTutorialG192Eg()
	helper_instance.exec_method(method_name)
