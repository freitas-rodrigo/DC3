from numpy import *
from numpy.linalg import norm
import joblib

import sys
sys.path.append('/home/freitas/dc3/two_elements/ml/util')
from constants import lattices, n_lattices, y_lattices, N_feat
from read_functions import read

# For two elements each lattice has two ideal lattice vectors (one for each element). In order to find them we notice that the distance between these two ideal vectors is always larger than 10, while identical vectors computed with different neighbors lead to variations in their distance ranging from 1-5. All it is required then is to compute the distance relative to one of the vectors and screen them according to the distance before averaging the vectors.

# Compute the average feature vector for the perfect lattice.
X = zeros((2*6,N_feat)) 
y = zeros(2*6)
for i in range(n_lattices):
  X_tmp = read('../01_compute_features_and_coherence/data/perfect_lattices/X_%s.dat' % lattices[i])
  d = norm(X_tmp-X_tmp[0],axis=1)
  X[2*i] = X_tmp[d<10].mean(axis=0)
  X[2*i+1] = X_tmp[d>10].mean(axis=0)
  y[2*i] = y_lattices[i]
  y[2*i+1] = y_lattices[i]

# Scale and save data.
scaler = joblib.load('data/synthetic_crystal/scaler.pkl')
X = scaler.transform(X)
savetxt('data/perfect_lattices/X.dat', X, fmt='%.8e')
savetxt('data/perfect_lattices/y.dat', y, fmt='%d')
