# DM-Halos-model

[halodp](halodp.py) calculates scale radius ($r_s$) and scale density ($\rho_s$) of the chosen galaxy cluster

Inputs for this code are redshift ($z$), virial mass ($m_{vir}$)  and virial concentration ($c_{vir}$).

[concentrationdp](concentrationdp.py) calculates $c_{vir}$ using [Ishiyama method](https://ui.adsabs.harvard.edu/abs/2021MNRAS.506.4210I/abstract)

Inputs for this code are redshift ($z$) and virial mass ($m_{vir}$). This is necessary for $c_{vir}$ for Einasto and DK14 profiles.

This code is similar to [Colossus](https://bdiemer.bitbucket.io/colossus/halo.html) however my code already includes the sample clusters and you can find the inputs from literature.


