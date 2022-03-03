from numpy import *

import sys
sys.path.append('/home/freitas/dc3/two_elements/ml/util')
from constants import lattices, y_lattices, md_lattices, y_md_lattices
from read_functions import read, read_partial

# Compute distance histograms for synthetic crystal data.
y = read('../../02_organize_data/data/synthetic_crystal/y.dat')
d = read('../data/distances_synthetic_crystal.dat')
for i in range(len(lattices)):
  rho, x = histogram(d[y==y_lattices[i]],bins=200,density=True,range=(0,60))
  x = x[:-1]
  savetxt('../data/post_processed/histogram_synthetic_crystal_%s.dat' % lattices[i], row_stack((x,rho)).T, header=' d | density', fmt='%.2f %.7f')

# Compute distance histogram for MD crystal data.
y = read_partial('../../02_organize_data/data/md_crystal/y.dat',len(d),1)
d = read('../data/distances_md_crystal.dat')
for i in range(len(md_lattices)):
  rho, x = histogram(d[y==y_md_lattices[i]],bins=200,density=True,range=(0,60))
  x = x[:-1]
  savetxt('../data/post_processed/histogram_md_crystal_%s.dat' % md_lattices[i], row_stack((x,rho)).T, header=' d | density', fmt='%.2f %.7f')
