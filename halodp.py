######this is code from colossus#####

from __future__ import print_function 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from colossus.cosmology import cosmology
cosmo = cosmology.setCosmology('planck15');

from colossus.halo import profile_nfw
from colossus.halo import profile_einasto
from colossus.halo import profile_dk14
from colossus.halo import profile_hernquist
from colossus.halo import profile_outer


cluster='A2029'

#cluster data
d1=pd.DataFrame.from_dict({
'A2142'  : [36.14E14,2.22,5.37,0.0909],
'A2744'  : [28.83E14,1.72,5.34,0.3080],
'A2199'  : [14.91E14,8.42,4.88,0.0302],
'A119'   : [30.2E14,5.59,5.20,0.0440],
'A478'   : [28.72E14,6.01,5.17,0.0880],
'A2029'  : [39.52E14,9.21,5.45,0.0767],
'A4038'  : [9.62E14,12.46,4.86,0.0282],
'A1758'  : [1.71E14 ,3.91,4.83,0.2790],
'A1664'  : [26.68E14 ,9.38,5.13,0.1280]},
orient='index',columns=['mvir','cvir1','cvir2','z'])

#cluster mvir-cvir and redshift
Mvir = d1.loc[cluster,'mvir']
cvir1 = d1.loc[cluster,'cvir1']
cvir2 = d1.loc[cluster,'cvir2']
z = d1.loc[cluster,'z']

#cluster parameter definitions
p_nfw = profile_nfw.NFWProfile(M = Mvir, c = cvir1, z = z, mdef = 'vir')
p_einasto = profile_einasto.EinastoProfile(M = Mvir, c = cvir2, z = z, mdef = 'vir')
p_dk14 = profile_dk14.DK14Profile(M = Mvir, c = cvir2, z = z, mdef = 'vir')
p_hernquist = profile_hernquist.HernquistProfile(M = Mvir, c = cvir1, z = z , mdef = 'vir')

#density and radius
r = 10**np.arange(0,4,0.02)
rho_m = cosmo.rho_m(z)
rho_nfw = p_nfw.density(r)
rho_einasto = p_einasto.density(r)
rho_dk14 = p_dk14.density(r)
rho_hernquist = p_hernquist.density(r)

#print rhos and rs (alpha for einasto) too
print(p_nfw.par)
print(p_einasto.par)
print(p_dk14.par)
print(p_hernquist.par)
#print(p_dk14.densityOuter(r))

#mass of DM particle (this value needed if you want to know number of DM particle)
m=100

#plot the graph
plt.figure()
plt.loglog()
plt.xlabel('r (kpc/h)')
plt.ylabel(r'$N_\chi(r)$ ($M_{\odot}h^2/kpc^3 GeV$)')
plt.plot(r, (rho_nfw / rho_m), '-', label = 'NFW');
plt.plot(r, (rho_einasto / rho_m), ':', label = 'Einasto');
plt.plot(r, (rho_dk14 / rho_m), '--', label = 'DK14');
plt.plot(r, (rho_hernquist / rho_m), '-.', label = 'hernquist');
plt.ylim(1E0, 1E7)
plt.xlim(1E0, 1E4)
plt.legend();
plt.show()
