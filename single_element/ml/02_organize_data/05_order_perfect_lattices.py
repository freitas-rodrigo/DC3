from numpy import *
import joblib

import sys
sys.path.append('/home/freitas/dc3/single_element/ml/util')
from constants import lattices, n_lattices, y_lattices, N_feat
from read_functions import read

# Compute the average feature vector for the perfect lattice.
X = zeros((6,N_feat))
for i in range(n_lattices):
  X_tmp = read('../01_compute_features_and_coherence/data/perfect_lattices/X_%s.dat' % lattices[i])
  X[i] = X_tmp.mean(axis=0)

# Scale and save data.
scaler = joblib.load('data/synthetic_crystal/scaler.pkl')
X = scaler.transform(X)
savetxt('data/perfect_lattices/X.dat', X, fmt='%.8e')
savetxt('data/perfect_lattices/y.dat', y_lattices, fmt='%d')
