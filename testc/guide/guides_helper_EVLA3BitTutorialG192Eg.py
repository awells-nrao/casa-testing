"""
This is a generated helper module for EVLA_3-bit_Tutorial_G192 casa guidemodule
all modified changes will be lost in the next code generation

The method to execute is set in locals() at runtime, is injected
by the regression test executor.

This is an autogenerated class for EVLA_3-bit_Tutorial_G192 guide testing purposes,
all the modified code will be re-written in the next code generation.

The class will help the following keyword-phrases:

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

import sys

# assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"
# assert globals().has_key("IPython"), "IPython environment is needed for this module (%s)" % __file__
# assert globals().has_key("casa"), "CASA environment is needed for this module (%s)" % __file__

import os

from testc.regression.helper import injectEnv

__test__ = False

@injectEnv
def test_00_splitting_fields_for_analysis():
	""" "splitting fields for analysis"
	"""
	split('TVER0004.sb14459364.eb14492359.56295.26287841435.ms', outputvis='G192_6s.ms', \
	      datacolumn='all', field='3,6,7,10', keepflags=False, spw='2~65')

@injectEnv
def test_01_listobs_on_the_initial_data_set():
	""" "listobs on the initial data set"
	"""
	listobs('G192_6s.ms', listfile='G192_listobs.txt')

@injectEnv
def test_02_flag_table_plot():
	""" "flag table plot"
	"""
	flagcmd(vis='G192_6s.ms', inpmode='table', action='plot', tablerows=myrows,
	        useapplied=True, plotfile='PlotG192_flagcmd_4.1.png')

@injectEnv
def test_03_bandpass_calibrator_analysis_flagging():
	""" "bandpass calibrator analysis flagging"
	"""
	flaglist = ['antenna="ea01,ea10,ea19,ea13"',
	            'antenna="ea24" spw="40,47~48"',
	            'antenna="ea18" spw="16~31"']
	flagcmd(vis='G192_6s.ms', inpmode='list', inpfile=flaglist, \
	        action='apply', flagbackup=True)

@injectEnv
def test_04_rfi_phase_calibrator_flagging():
	""" "RFI phase calibrator flagging"
	"""
	flaglist = ['spw="33:124,37:91,38:66~67;75~77,46:126,48:0"', \
	            'spw="53:68~69,63:80,10:26,15:127,27:62,27:64"']
	flagcmd(vis='G192_6s.ms', inpmode='list', inpfile=flaglist, \
	        action='apply', flagbackup=True)

@injectEnv
def test_05_splitting_good_and_bad_data():
	""" "splitting good and bad data"
	"""
	# Remove any existing split data, otherwise split will not happen
	os.system('rm -rf G192_flagged_6s.ms')
	split(vis='G192_6s.ms', outputvis='G192_flagged_6s.ms', \
	      datacolumn='data', keepflags=False)

@injectEnv
def test_06_split_and_flagged_listobs():
	""" "split and flagged listobs"
	"""
	listobs('G192_flagged_6s.ms', listfile='G192_flagged_listobs.txt')

@injectEnv
def test_07_model_for_the_flux_calibrator():
	""" "model for the flux calibrator"
	"""
	setjy(vis='G192_flagged_6s.ms', field='0', scalebychan=True, \
	      model='3C147_A.im')

@injectEnv
def test_08_determining_antenna_position_corrections():
	""" "determining antenna position corrections"
	"""
	gencal('G192_flagged_6s.ms', caltable='calG192.antpos', \
	       caltype='antpos', antenna='')

@injectEnv
def test_09_generating_gaincurve_calibration():
	""" "generating gaincurve calibration"
	"""
	gencal('G192_flagged_6s.ms', caltable='calG192.gaincurve', \
	       caltype='gc')

@injectEnv
def test_10_generate_atmospheric_opacity_calibration():
	""" "generate atmospheric opacity calibration"
	"""
	SPWs = []
	for window in range(0,64):
		SPWs.append(str(window))
		spwString = ','.join(SPWs)
	gencal(vis='G192_flagged_6s.ms', caltable='calG192.opacity',
	       caltype='opac', spw=spwString, parameter=myTau)

@injectEnv
def test_11_generate_requantizer_gains_corrections():
	""" "generate requantizer gains corrections"
	"""
	gencal('G192_flagged_6s.ms', caltable='calG192.requantizer', \
	       caltype='rq')

@injectEnv
def test_12_phase_only_calibration():
	""" "phase only calibration"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G0', \
	        field='3', spw='*:60~68', \
	        gaintable=['calG192.antpos','calG192.gaincurve', \
	                   'calG192.requantizer','calG192.opacity'], \
	        gaintype='G', refant='ea05', calmode='p', \
	        solint='int', minsnr=3)

@injectEnv
def test_13_residual_delays():
	""" "residual delays"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.K0', \
	        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
	                   'calG192.opacity', 'calG192.G0'], \
	        field='3', spw='*:5~122', gaintype='K', \
	        refant='ea05', solint='inf', minsnr=3)

@injectEnv
def test_14_antenna_bandpasses():
	""" "antenna bandpasses"
	"""
	bandpass(vis='G192_flagged_6s.ms', caltable='calG192.B0', \
	         gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
	                    'calG192.opacity', 'calG192.G0', 'calG192.K0'], \
	         field='3', refant='ea05', solnorm=False, \
	         bandtype='B', solint='inf')

@injectEnv
def test_15_flux_and_bandpass_calibrators_gain():
	""" "flux and bandpass calibrators gain"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1', field='0,3', \
	        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
	                   'calG192.opacity', 'calG192.K0', \
	                   'calG192.B0'], \
	        gaintype='G', refant='ea05', calmode='ap', solint='30s', minsnr=3)

@injectEnv
def test_16_bandpass_calibrator_gain_amplitudes_scaling():
	""" "bandpass calibrator gain amplitudes scaling"
	"""
	flux1 = fluxscale(vis='G192_flagged_6s.ms', caltable='calG192.G1', \
	                  fluxtable='calG192.F1', reference='0', \
	                  transfer='3', listfile='3C84.fluxinfo', fitorder=1)

@injectEnv
def test_17_spectral_information():
	""" "spectral information"
	"""
	setjy(vis='G192_flagged_6s.ms', field='3', scalebychan=True, \
	      fluxdensity=[29.8756, 0, 0, 0], spix=-0.598929, \
	      reffreq='32.4488GHz')

@injectEnv
def test_18_phase_only_recalibration():
	""" "phase only recalibration"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G0.b', \
	        field='3', spw='*:60~68', \
	        gaintable=['calG192.antpos', 'calG192.gaincurve', \
	                   'calG192.requantizer', 'calG192.opacity'], \
	        gaintype='G', refant='ea05', calmode='p', \
	        solint='int', minsnr=3)

@injectEnv
def test_19_residual_delays_recalibration():
	""" "residual delays recalibration"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.K0.b', \
	        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
	                  'calG192.opacity', 'calG192.G0.b'], \
	        field='3', spw='*:5~122', gaintype='K', \
	        refant='ea05', solint='inf', minsnr=3)

@injectEnv
def test_20_antenna_bandpasses_recalibration():
	""" "antenna bandpasses recalibration"
	"""
	bandpass(vis='G192_flagged_6s.ms', caltable='calG192.B0.b', \
	         gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
	                    'calG192.opacity', 'calG192.G0.b', 'calG192.K0.b'], \
	         field='3', refant='ea05', solnorm=False, \
	         bandtype='B', solint='inf')

@injectEnv
def test_21_compute_gain_phases_using_3c147():
	""" "compute gain phases using 3C147"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int', \
	        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
	                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b'], \
	        field='0', refant='ea05', solnorm=F, \
	        solint='int', gaintype='G', calmode='p')

@injectEnv
def test_22_compute_gain_phases_using_j0603_174():
	""" "compute gain phases using J0603+174"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int', \
	        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
	                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b'], \
	        field='1', refant='ea05', solnorm=F, \
	        solint='12s', gaintype='G', calmode='p', append=True)

@injectEnv
def test_23_compute_gain_phases_using_3c84():
	""" "compute gain phases using 3C84"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int', \
	        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
	                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b'], \
	        field='3', refant='ea05', solnorm=F, \
	        solint='int', gaintype='G', calmode='p', append=True)

@injectEnv
def test_24_applying_phase_calibration():
	""" "applying phase calibration"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.inf', \
	        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
	                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b'], \
	        field='1', refant='ea05', solnorm=F, \
	        solint='inf', gaintype='G', calmode='p')

@injectEnv
def test_25_3c147_scan_solving_amplitudes():
	""" "3C147 scan solving amplitudes"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2', \
	        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
	                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', 'calG192.G1.int'], \
	        gainfield=['', '', '', '', '3', '3', '0'], \
	        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
	        field='0', refant='ea05', solnorm=F, \
	        solint='inf', gaintype='G', calmode='a')

@injectEnv
def test_26_j0603_174__scan_solving_amplitudes():
	""" "J0603+174  scan solving amplitudes"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2', \
	        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
	                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', 'calG192.G1.int'], \
	        gainfield=['', '', '', '', '3', '3', '1'], \
	        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
	        field='1', refant='ea05', solnorm=F, \
	        solint='inf', gaintype='G', calmode='a', append=True)

@injectEnv
def test_27_3c84_scan_solving_amplitudes():
	""" "3C84 scan solving amplitudes"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2', \
	        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer', \
	                   'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', 'calG192.G1.int'], \
	        gainfield=['', '', '', '', '3', '3', '3'], \
	        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
	        field='3', refant='ea05', solnorm=F, \
	        solint='inf', gaintype='G', calmode='a', append=True)
	#

@injectEnv
def test_28_using_fluxscale_to_transfer_the_amplitude_solutions():
	""" "using fluxscale to transfer the amplitude solutions"
	"""
	flux2 = fluxscale(vis='G192_flagged_6s.ms', caltable='calG192.G2', \
	                  fluxtable='calG192.F2', reference='0')

@injectEnv
def test_29_3c147_accumulated_calibration():
	""" "3C147 accumulated calibration"
	"""
	applycal(vis='G192_flagged_6s.ms', field='0', \
	         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
	                    'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', \
	                    'calG192.G1.int', 'calG192.G2'], \
	         gainfield=['', '', '', '', '', '', '0', '0'],
	         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)

@injectEnv
def test_30_gain_accumulated_calibration():
	""" "gain accumulated calibration"
	"""
	applycal(vis='G192_flagged_6s.ms', field='1', \
	         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
	                    'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', \
	                    'calG192.G1.int', 'calG192.F2'], \
	         gainfield=['', '', '', '', '', '', '1', '1'],
	         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)

@injectEnv
def test_31_g192_accumulated_calibration():
	""" "G192 accumulated calibration"
	"""
	applycal(vis='G192_flagged_6s.ms', field='2', \
	         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
	                    'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b',\
	                    'calG192.G1.inf', 'calG192.F2'], \
	         gainfield=['', '', '', '', '', '', '1', '1'],
	         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'linear'], calwt=False)

@injectEnv
def test_32_3c84_accumulated_calibration():
	""" "3C84 accumulated calibration"
	"""
	applycal(vis='G192_flagged_6s.ms', field='3', \
	         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
	                    'calG192.opacity', 'calG192.K0.b', 'calG192.B0.b', \
	                    'calG192.G1.int', 'calG192.F2'], \
	         gainfield=['', '', '', '', '', '', '3', '3'],
	         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)

@injectEnv
def test_33_flagging_isolated_rfi():
	""" "flagging isolated RFI"
	"""
	flagdata(vis='G192_flagged_6s.ms', field='0', \
	         spw='29', timerange='6:35:00~6:36:40')

@injectEnv
def test_34_baseline_flagging():
	""" "baseline flagging"
	"""
	flagdata(vis='G192_flagged_6s.ms', antenna='ea03&ea07')

@injectEnv
def test_35_3c147_density_model():
	""" "3C147 density model"
	"""
	setjy(vis='G192_flagged_6s.ms', field='0', scalebychan=True, \
	      model='3C147_A.im')

@injectEnv
def test_36_3c84_spectral_information_column():
	""" "3C84 spectral information column"
	"""
	setjy(vis='G192_flagged_6s.ms', field='3', scalebychan=True, \
	      fluxdensity=[29.8756, 0, 0, 0], spix=-0.598929, \
	      reffreq='32.4488GHz')

@injectEnv
def test_37_initial_phase_calibration():
	""" "initial phase calibration"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G0.b.2', field='3', spw='*:60~68',\
	        gaintable=['calG192.antpos', 'calG192.gaincurve', \
	                  'calG192.requantizer', 'calG192.opacity'], \
	        gaintype='G', refant='ea05', calmode='p', solint='int', minsnr=3)

@injectEnv
def test_38_delay_calibration():
	""" "delay calibration"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.K0.b.2', \
	        field='3', spw='*:5~122', gaintype='K', \
	        gaintable=['calG192.antpos', 'calG192.gaincurve', \
	                  'calG192.requantizer', 'calG192.opacity','calG192.G0.b.2'], \
	        refant='ea05', solint='inf', minsnr=3)

@injectEnv
def test_39_bandpass_calibration():
	""" "bandpass calibration"
	"""
	bandpass(vis='G192_flagged_6s.ms', caltable='calG192.B0.b.2', \
	         field='3', refant='ea05', solnorm=False, \
	        gaintable=['calG192.antpos', 'calG192.gaincurve', 'calG192.requantizer',\
	                   'calG192.opacity','calG192.G0.b.2', 'calG192.K0.b.2'], \
	         bandtype='B', solint='inf')

@injectEnv
def test_40_phase_gain_calibration_field_0():
	""" "phase gain calibration field 0"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int.2', \
	        field='0', refant='ea05', solnorm=F, \
	        gaintable=['calG192.antpos', 'calG192.requantizer','calG192.gaincurve', \
	                   'calG192.opacity', 'calG192.K0.b.2','calG192.B0.b.2'], \
	        solint='int', gaintype='G', calmode='p')

@injectEnv
def test_41_phase_gain_calibration_field_1():
	""" "phase gain calibration field 1"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int.2', \
	        field='1', refant='ea05', solnorm=F, \
	        gaintable=['calG192.antpos', 'calG192.requantizer','calG192.gaincurve', \
	                   'calG192.opacity', 'calG192.K0.b.2','calG192.B0.b.2'], \
	        solint='12s', gaintype='G', calmode='p', append=True)

@injectEnv
def test_42_phase_gain_calibration_field_3():
	""" "phase gain calibration field 3"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.int.2', \
	        field='3', refant='ea05', solnorm=F, \
	        gaintable=['calG192.antpos', 'calG192.requantizer','calG192.gaincurve', \
	                   'calG192.opacity', 'calG192.K0.b.2','calG192.B0.b.2'], \
	        solint='int', gaintype='G', calmode='p', append=True)

@injectEnv
def test_43_phase_gain_calibration_infinite_solution_interval():
	""" "phase gain calibration infinite solution interval"
	"""
	# (Note: we will apply this table to our science target at the applycal stage.)
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G1.inf.2', \
	        field='1', refant='ea05', solnorm=F, \
	        gaintable=['calG192.antpos', 'calG192.requantizer','calG192.gaincurve', \
	                   'calG192.opacity', 'calG192.K0.b.2','calG192.B0.b.2'], \
	        solint='inf', gaintype='G', calmode='p')

@injectEnv
def test_44_amplitude_calibration_solutions_field_0():
	""" "amplitude calibration solutions field 0"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2.2', \
	        field='0', refant='ea05', solnorm=F, \
	        gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
	                   'calG192.opacity', 'calG192.K0.b.2', \
	                   'calG192.B0.b.2', 'calG192.G1.int.2'], \
	        gainfield=['', '', '', '', '3', '3', '0'], \
	        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
	        solint='inf', gaintype='G', calmode='a')

@injectEnv
def test_45_amplitude_calibration_solutions_field_1():
	""" "amplitude calibration solutions field 1"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2.2', \
	        field='1', refant='ea05', solnorm=F, \
	        gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
	                   'calG192.opacity', 'calG192.K0.b.2', \
	                   'calG192.B0.b.2', 'calG192.G1.int.2'], \
	        gainfield=['', '', '', '', '3', '3', '1'], \
	        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
	        solint='inf', gaintype='G', calmode='a', append=True)

@injectEnv
def test_46_amplitude_calibration_solutions_field_3():
	""" "amplitude calibration solutions field 3"
	"""
	gaincal(vis='G192_flagged_6s.ms', caltable='calG192.G2.2', \
	        field='3', refant='ea05', solnorm=F, \
	        gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', \
	                   'calG192.opacity', 'calG192.K0.b.2', \
	                   'calG192.B0.b.2', 'calG192.G1.int.2'], \
	        gainfield=['', '', '', '', '3', '3', '3'], \
	        interp=['', '', '', '', 'nearest', 'nearest', 'nearest'], \
	        solint='inf', gaintype='G', calmode='a', append=True)

@injectEnv
def test_47_flux_calibration_solutions():
	""" "flux calibration solutions"
	"""
	flux3 = fluxscale(vis='G192_flagged_6s.ms', caltable='calG192.G2.2', \
	                  fluxtable='calG192.F2.2', reference='0')

@injectEnv
def test_48_apply_calibration_tables_field_0():
	""" "apply calibration tables field 0"
	"""
	applycal(vis='G192_flagged_6s.ms', field='0', \
	         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', 'calG192.opacity',\
	                    'calG192.K0.b.2', 'calG192.B0.b.2', 'calG192.G1.int.2', 'calG192.G2.2'], \
	         gainfield=['', '', '', '', '', '', '0', '0'], \
	         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)

@injectEnv
def test_49_apply_calibration_tables_field_1():
	""" "apply calibration tables field 1"
	"""
	applycal(vis='G192_flagged_6s.ms', field='1', \
	         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', 'calG192.opacity',\
	                    'calG192.K0.b.2', 'calG192.B0.b.2', 'calG192.G1.int.2', 'calG192.F2.2'], \
	         gainfield=['', '', '', '', '', '', '1', '1'], \
	         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)

@injectEnv
def test_50_apply_calibration_tables_field_2():
	""" "apply calibration tables field 2"
	"""
	applycal(vis='G192_flagged_6s.ms', field='2', \
	         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', 'calG192.opacity',\
	                    'calG192.K0.b.2', 'calG192.B0.b.2', 'calG192.G1.inf.2', 'calG192.F2.2'], \
	         gainfield=['', '', '', '', '', '', '1', '1'], \
	         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'linear'], calwt=False)

@injectEnv
def test_51_apply_calibration_tables_field_3():
	""" "apply calibration tables field 3"
	"""
	applycal(vis='G192_flagged_6s.ms', field='3', \
	         gaintable=['calG192.antpos', 'calG192.requantizer', 'calG192.gaincurve', 'calG192.opacity',\
	                    'calG192.K0.b.2', 'calG192.B0.b.2', 'calG192.G1.int.2', 'calG192.F2.2'], \
	         gainfield=['', '', '', '', '', '', '3', '3'], \
	         interp=['', '', '', '', 'nearest', 'nearest', 'linear', 'nearest'], calwt=False)

@injectEnv
def test_52_splitting_calibrated_data_3c147():
	""" "splitting calibrated data 3C147"
	"""
	os.system('rm -rf 3C147_split_6s.ms')
	split(vis='G192_flagged_6s.ms', outputvis='3C147_split_6s.ms', \
	      datacolumn='corrected', field='0')
	#

@injectEnv
def test_53_splitting_calibrated_data_j0603_174():
	""" "splitting calibrated data J0603+174"
	"""
	os.system('rm -rf J0603_split_6s.ms')
	split(vis='G192_flagged_6s.ms', outputvis='J0603_split_6s.ms', \
	      datacolumn='corrected', field='1')
	#

@injectEnv
def test_54_splitting_calibrated_data_g192():
	""" "splitting calibrated data G192"
	"""
	os.system('rm -rf G192_split_6s.ms')
	split(vis='G192_flagged_6s.ms', outputvis='G192_split_6s.ms', \
	      datacolumn='corrected', field='2')
	#

@injectEnv
def test_55_splitting_calibrated_data_3c84():
	""" "splitting calibrated data 3C84"
	"""
	os.system('rm -rf 3C84_split_6s.ms')
	split(vis='G192_flagged_6s.ms', outputvis='3C84_split_6s.ms', \
	      datacolumn='corrected', field='3')

@injectEnv
def test_56_single_spectral_window_cleaning():
	""" "single spectral window cleaning"
	"""
	clean(vis='G192_split_6s.ms', spw='48:5~122', \
	      imagename='imgG192_6s_spw48', \
	      mode='mfs', nterms=1, niter=10000, \
	      imsize=[1280], cell=['0.015arcsec'], \
	      imagermode='csclean', cyclefactor=1.5, \
	      weighting='briggs', robust=0.5, \
	      interactive=True)

@injectEnv
def test_57_lower_frequency_baseband_cleaning():
	""" "lower frequency baseband cleaning"
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

@injectEnv
def test_58_upper_frequency_baseband_cleaning():
	""" "upper frequency baseband cleaning"
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

@injectEnv
def test_59_basebands_mfs_taylor_cleaning():
	""" "basebands mfs taylor cleaning"
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

@injectEnv
def test_60_spectral_index_image_filtering():
	""" "spectral index image filtering"
	"""
	immath(imagename=['imgG192_6s_spw0-63_mfs2.image.alpha',
	                  'imgG192_6s_spw0-63_mfs2.image.tt0'],
	       mode='evalexpr',
	       expr='IM0[IM1>2.0E-4]',
	       outfile='imgG192_6s_spw0-63_mfs2.image.alpha.filtered')

@injectEnv
def test_61_spectral_index_probable_errors_filtering():
	""" "spectral index probable errors filtering"
	"""
	immath(imagename=['imgG192_6s_spw0-63_mfs2.image.alpha.error',
	                  'imgG192_6s_spw0-63_mfs2.image.tt0'],
	       mode='evalexpr',
	       expr='IM0[IM1>2E-4]',
	       outfile='imgG192_6s_spw0-63_mfs2.image.alpha.error.filtered')

@injectEnv
def test_62_intensity_weighted_mean_spectral_analysis():
	""" "intensity weighted mean spectral analysis"
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