from numpy import *

import sys
sys.path.append('/home/freitas/dc3/single_element/ml_sop_only/util')
from constants import lattices, n_lattices, y_lattices
from constants import md_lattices, n_md_lattices, y_md_lattices

# Find 99th percentile of synthetic crystal data.
d_cut = zeros(n_lattices) # 99th percentile cutoff location.
for i in range(n_lattices):
  d, rho = loadtxt('../data/post_processed/histogram_synthetic_crystal_%s.dat' % lattices[i], unpack=True)
  I = cumsum(rho)*(d[1]-d[0])
  arg = argmax(I > 0.99)
  d_cut[i] = d[arg]

# Compute fraction of correctly labeled MD crystal data.
f_mdc = zeros(n_md_lattices) # Fraction of correctly labeled data.
for i in range(n_md_lattices):
  d, rho = loadtxt('../data/post_processed/histogram_md_crystal_%s.dat' % md_lattices[i], unpack=True)
  f_mdc[i] = 1-sum(rho[d>=d_cut[y_lattices==abs(y_md_lattices[i])]])*(d[1]-d[0])
f_mdc *= 100

# Save data.
savetxt('../data/post_processed/accuracy_md_crystal.dat', f_mdc, header=' fraction of correctly identified atoms for each lattice', fmt='%.7f')
savetxt('../data/post_processed/distance_cutoff_vs_lattice.dat', d_cut, header='distance cutoff for each lattice', fmt='%5.2f')
