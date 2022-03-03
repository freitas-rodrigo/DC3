from numpy import *
from sklearn.utils import shuffle
import joblib

import sys
sys.path.append('/home/freitas/dc3/two_elements/ml/util')
from constants import md_lattices, n_md_lattices, y_md_lattices
from read_functions import read

################################################################################
# Setup.                                                                       #
################################################################################

# Input data.
steps = arange(10000,100000+1,10000) # Step range.
N = 17000 # Number of examples to collect per lattice.

################################################################################
# Concatenate data from different steps into one file per lattice.             #
################################################################################

for i in range(n_md_lattices):
  if md_lattices[i] == 'zincblende': continue # SNAP InP doesn't have a stable liquid phase.
  for step in steps:
    X_tmp = read('../01_compute_features_and_coherence/data/md/X_%s_1.60_%d.dat' % (md_lattices[i],step))
    alpha_tmp = read('../01_compute_features_and_coherence/data/md/alpha_%s_1.60_%d.dat' % (md_lattices[i],step))
    if step == steps[0]:
      X = X_tmp
      alpha = alpha_tmp
    else:
      X = row_stack((X,X_tmp))
      alpha = concatenate((alpha,alpha_tmp))
  X, alpha = shuffle(X,alpha)
  X = X[:N]
  alpha = alpha[:N]
  scaler = joblib.load('data/synthetic_crystal/scaler.pkl')
  X = scaler.transform(X)
  savetxt('data/tmp/X_md_liquid_%s.dat' % md_lattices[i],X,fmt='%.8e')
  savetxt('data/tmp/alpha_md_liquid_%s.dat' % md_lattices[i],alpha,fmt='%.6f')

################################################################################
# Collect all data in one file.                                                #
################################################################################

del X
for i in range(n_md_lattices):
  if md_lattices[i] == 'zincblende': continue # SNAP InP doesn't have a stable liquid phase.
  X_tmp = read('data/tmp/X_md_liquid_%s.dat' % md_lattices[i])
  y_tmp = y_md_lattices[i]*ones(X_tmp.shape[0])
  alpha_tmp = read('data/tmp/alpha_md_liquid_%s.dat' % md_lattices[i])
  if 'X' in locals():
    X = row_stack((X,X_tmp))
    y = concatenate((y,y_tmp))
    alpha = concatenate((alpha,alpha_tmp))
  else:
    X = X_tmp
    y = y_tmp
    alpha = alpha_tmp
X,y,alpha = shuffle(X,y,alpha)
savetxt('data/md_liquid/X.dat',X,fmt='%.8e')
savetxt('data/md_liquid/y.dat',y,fmt='%d')
savetxt('data/md_liquid/alpha.dat',alpha,fmt='%.6f')

################################################################################
