from numpy import *
from sklearn.utils import shuffle
import joblib

import sys
sys.path.append('/home/freitas/dc3/single_element/ml_sop_only/util')
from constants import md_lattices
from read_functions import read

################################################################################
# Setup.                                                                       #
################################################################################

# Input data.
steps = arange(10000,100000+1,10000) # Step range.
N = 17000 # Number of examples to collect per lattice per temperature.
i = int(sys.argv[1]) # Crystal lattice.

# Crystal structure metastability limit.
T_ml = loadtxt('../../../md/post_processing/data/crystals_metastability_limit.dat', unpack=True, usecols=[1])

################################################################################
# Concatenate all timesteps into one file per temperature and lattice.         #
################################################################################

for T in arange(0.04,T_ml[i]+0.01,0.04):
  for step in steps:
    X_tmp = read('../../01_compute_features_and_coherence/data/md/X_%s_%.2f_%d.dat' % (md_lattices[i],T,step))
    alpha_tmp = read('../../01_compute_features_and_coherence/data/md/alpha_%s_%.2f_%d.dat' % (md_lattices[i],T,step))
    if step == steps[0]:
      X = X_tmp
      alpha = alpha_tmp
    else:
      X = row_stack((X,X_tmp))
      alpha = concatenate((alpha,alpha_tmp))
  # Shuffle, scale/normalize, and save.
  X, alpha = shuffle(X,alpha)
  X = X[:N]
  alpha = alpha[:N]
  scaler = joblib.load('../data/synthetic_crystal/scaler.pkl')
  X = scaler.transform(X)
  savetxt('../data/tmp/X_md_crystal_%s_%.2f.dat' % (md_lattices[i],T),X,fmt='%.8e')
  savetxt('../data/tmp/alpha_md_crystal_%s_%.2f.dat' % (md_lattices[i],T),alpha,fmt='%.6f')

################################################################################
