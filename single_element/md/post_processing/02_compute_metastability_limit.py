from numpy import *

lattices = ['fcc', 'bcc', 'hcp', 'cd', 'hd', 'sc', 'fcc_2', 'bcc_2', 'hcp_2', 'cd_2']

# Estimate the metastability limit of the crystal by finding the point along the
# potential energy vs temperature curve where the change in potential energy to
# the next temperrature is at least 2x as large as the change from the previous
# temperature.
T_ml = zeros(len(lattices))
for i in range(len(lattices)):
  T, pe = loadtxt('data/averages/%s.dat' % lattices[i], unpack=True, usecols=[0,2])
  dpe = abs(pe[:-1]-pe[1:])
  for j in range(1,len(dpe)):
    if dpe[j] > 2.0*dpe[j-1]:
      T_ml[i] = T[j]
      break
savetxt('data/crystals_metastability_limit.dat', array([arange(1,len(lattices)+1),T_ml]).T, fmt='%d %.2f', header='Structure | Crystal metastability limit temperature [K]')
