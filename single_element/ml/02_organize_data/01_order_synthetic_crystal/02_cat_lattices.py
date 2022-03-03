from numpy import *
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import joblib

import sys
sys.path.append('/home/freitas/dc3/single_element/ml/util')
from constants import lattices, n_lattices, y_lattices
from read_functions import read

################################################################################
# Concatenate data with lattice into one file.                                 #
################################################################################

for i in range(n_lattices):
  X_tmp = read('../data/tmp/X_synthetic_crystal_%s.dat' % lattices[i])
  y_tmp = y_lattices[i]*ones(X_tmp.shape[0])
  alpha_tmp = read('../data/tmp/alpha_synthetic_crystal_%s.dat' % lattices[i])
  if 'X' in locals():
    X = row_stack((X,X_tmp))
    y = concatenate((y,y_tmp))
    alpha = concatenate((alpha,alpha_tmp))
  else:
    X = X_tmp
    y = y_tmp
    alpha = alpha_tmp

################################################################################
# Standardize data.                                                            #
################################################################################

X,y,alpha = shuffle(X,y,alpha)
scaler = StandardScaler().fit(X)
X = scaler.transform(X)
joblib.dump(scaler,'../data/synthetic_crystal/scaler.pkl')
savetxt('../data/synthetic_crystal/X.dat', X, fmt='%.8e')
savetxt('../data/synthetic_crystal/y.dat', y, fmt='%d')
savetxt('../data/synthetic_crystal/alpha.dat', alpha, fmt='%.6f')

################################################################################
