######this is code from colossus#####


from __future__ import print_function 
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
from colossus.cosmology import cosmology
cosmology.setCosmology('planck18');

from colossus.halo import concentration

cluster='A1664'

#cluster data
d1=pd.DataFrame.from_dict({
'A2142'  : [36.14E14,2.22,0.0909],
'A2744'  : [28.83E14,1.72,0.3080],
'A2199'  : [14.91E14,8.42,0.0302],
'A119'   : [30.2E14,5.59,0.0440],
'A478'   : [28.72E14,6.01,0.0880],
'A2029'  : [39.52E14,9.21,0.0767],
'A4038'  : [9.62E14,12.46,0.0282],
'A1758'  : [1.71E14 ,3.91,0.2790],
'A1664'  : [26.68E14 ,9.38,0.1280]},
orient='index',columns=['mvir','cvir','z'])

#cluster mvir-cvir and redshift
Mvir = d1.loc[cluster,'mvir']
#cvir = d1.loc[cluster,'cvir']
z = d1.loc[cluster,'z']

p=concentration.concentration(Mvir,'vir', z, model = 'ishiyama21')

print(p)
