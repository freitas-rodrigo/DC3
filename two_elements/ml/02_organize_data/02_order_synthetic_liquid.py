from numpy import *
from sklearn.utils import shuffle
import joblib

import sys
sys.path.append('/home/freitas/dc3/two_elements/ml/util')
from constants import lattices
from read_functions import read

# Concatenate coherence factor into a single file.
for m in range(1,10+1):
  alpha_tmp = read('../01_compute_features_and_coherence/data/synthetic_liquid/alpha_%d.dat' % m)
  if m == 1:
    alpha = alpha_tmp
  else:
    alpha = concatenate((alpha,alpha_tmp))
alpha = shuffle(alpha)
savetxt('data/synthetic_liquid/alpha.dat', alpha, fmt='%.6f')
