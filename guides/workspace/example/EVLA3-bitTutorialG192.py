# In CASA: initial data split
split('TVER0004.sb14459364.eb14492359.56295.26287841435.ms', outputvis='G192_6s.ms', \
      datacolumn='all', field='3,6,7,10', keepflags=False, spw='2~65')
# In CASA: initial listobs run
listobs('G192_6s.ms', listfile='G192_listobs.txt')
# In CASA
os.system("cat G192_listobs.txt")
# In CASA
flagcmd(vis='G192_6s.ms', inpmode='table', action='list', \
        useapplied=True)
# In CASA
myrows = range(2868)
flagcmd(vis='G192_6s.ms', inpmode='table', action='plot', \
        useapplied=True, tablerows=myrows)
# In CASA: creating a plot of the already flagged data
flagcmd(vis='G192_6s.ms', inpmode='table', action='plot', tablerows=myrows, 
        useapplied=True, plotfile='PlotG192_flagcmd_4.1.png')
# In CASA
plotants('G192_6s.ms')
print r'''Command: plotants('G192_6s.ms')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
clearstat
# In CASA
# Removing any previous cleaning information
# This assumes you want to start this clean from scratch
# If you want to continue this from a previous clean run, 
# the rm -rf system command should be be skipped
os.system ('rm -rf imgG192_6s_spw0-31*')
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
# In CASA
# Removing any previous cleaning information
# This assumes you want to start this clean from scratch
# If you want to continue this from a previous clean run, 
# the rm -rf system command should be be skipped
os.system ('rm -rf imgG192_6s_spw0-63_mfs2*')
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
# In CASA
viewer('imgG192_6s_spw0-63_mfs2.image.tt0')
print r'''Command: viewer('imgG192_6s_spw0-63_mfs2.image.tt0')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
immath(imagename=['imgG192_6s_spw0-63_mfs2.image.alpha', 
                  'imgG192_6s_spw0-63_mfs2.image.tt0'],
       mode='evalexpr',
       expr='IM0[IM1>2.0E-4]',
       outfile='imgG192_6s_spw0-63_mfs2.image.alpha.filtered')
# In CASA
immath(imagename=['imgG192_6s_spw0-63_mfs2.image.alpha.error', 
                  'imgG192_6s_spw0-63_mfs2.image.tt0'],
       mode='evalexpr',
       expr='IM0[IM1>2E-4]',
       outfile='imgG192_6s_spw0-63_mfs2.image.alpha.error.filtered')
# In CASA
viewer('imgG192_6s_spw0-63_mfs2.image.alpha.filtered')
print r'''Command: viewer('imgG192_6s_spw0-63_mfs2.image.alpha.filtered')'''
user_check=raw_input('When you are done with the window, close it and press enter to continue:')
# In CASA
listobs('G192_split_6s.ms', listunfl=True)
# In CASA
# Removing any file output from previous runs, so immath will proceed
os.system('rm -rf imgG192_6s_spw0-63_mfs2.image.tt1.filtered')
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
# In CASA
mystat = imstat('imgG192_6s_spw0-63_mfs2.image.tt1.filtered',
                region='G192.crtf')
avgtt0alpha = mystat['mean'][0]
#
mystat = imstat('imgG192_6s_spw0-63_mfs2.image.tt0.filtered',
                region='G192.crtf')
avgtt0 = mystat['mean'][0]
avgalpha = avgtt0alpha / avgtt0
print 'G192 intensity-weighted alpha = ' + str(avgalpha)
