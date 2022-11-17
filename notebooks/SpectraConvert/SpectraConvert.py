# -*- coding: utf-8 -*-
'''
n1680575
converts from spectra to impedance edis
'''

import mtpy.core.edi as mtedi
import os

#location of edis
edipath=r'F:\ClonExtnMT\BoraderSitesPlot\spectraconvert'

#out location
outloc =r'F:\ClonExtnMT\BoraderSitesPlot\spectraconvert\imp'

#Make list with all edi paths in edipath
edilist=[os.path.join(edipath,edi)
    for edi in os.listdir(edipath)
        if edi.find('.edi')>0]

# Run conversion
errcount = 0
for n in edilist:
    filename_noext = os.path.splitext(os.path.basename(n))[0]
    bloc = outpath +'\\'+ filename_noext + '.edi'
    try:
        eo = mtedi.Edi(n)
        eo.write_edi_file(bloc)
    except Exception as e:
        errcount += 1
        print(f'Conversion of {filename_noext+".edi"} failed with error: {repr(e)}')
print(f'Done ({len(edilist)-errcount}/{len(edilist)})')
