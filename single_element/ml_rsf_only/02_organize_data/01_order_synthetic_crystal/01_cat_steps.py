from numpy import *
from sklearn.utils import shuffle

import sys
sys.path.append('/home/freitas/dc3/single_element/ml_rsf_only/util')
from constants import lattices
from read_functions import read

################################################################################
# Setup.                                                                       #
################################################################################

N = 69000 # Number of examples per lattice.
i = int(sys.argv[1]) # Crystal lattice.

# Number of cells per lattice.
M = int(loadtxt('../../../synthetic/02_crystal/data/n_cells_created.dat'))

################################################################################
# Concatenate data with different displacements in one file per lattice.       #
################################################################################

for m in range(M):
  X_tmp = read('../../01_compute_features_and_coherence/data/synthetic_crystal/X_%s_%d.dat' % (lattices[i],m))
  alpha_tmp = read('../../01_compute_features_and_coherence/data/synthetic_crystal/alpha_%s_%d.dat' % (lattices[i],m))
  if 'X' in locals():
    X = row_stack((X,X_tmp))
    alpha = concatenate((alpha,alpha_tmp))
  else:
    X = X_tmp
    alpha = alpha_tmp
X, alpha = shuffle(X,alpha)
X = X[:N]
alpha = alpha[:N]
savetxt('../data/tmp/X_synthetic_crystal_%s.dat' % lattices[i], X, fmt='%.8e')
savetxt('../data/tmp/alpha_synthetic_crystal_%s.dat' % lattices[i], alpha, fmt='%.6f')

################################################################################
