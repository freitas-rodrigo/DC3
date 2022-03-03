from numpy import *
from sklearn.decomposition import PCA
import joblib

import sys
sys.path.append('/home/freitas/dc3/two_elements/ml/util')
from constants import N_feat
from read_functions import read_partial

################################################################################
# Fit PCA transform and compute variance.                                      #
################################################################################

M = 100000 # Number of data points used in PCA.

# Fit PCA transform.
X = read_partial('../02_organize_data/data/synthetic_crystal/X.dat',M,N_feat)
pca = PCA()
X_pca = pca.fit(X)
joblib.dump(pca,'data/pca.pkl')

# Compute cummulative variance explained by PCA components.
var = pca.explained_variance_ratio_.cumsum()
u = arange(1,len(var)+1)
savetxt('data/variance.dat', transpose([u,var]), fmt='%2d %.5f', header=' n_components | explained variance (cummulative sum)')

################################################################################
# Apply PCA transformation to other data.                                      #
################################################################################

for system in ['synthetic_crystal', 'perfect_lattices', 'md_crystal', 'md_liquid']:
  X = read_partial('../02_organize_data/data/%s/X.dat' % system,M,N_feat)
  X_pca = pca.transform(X)
  savetxt('data/X_PCA_%s.dat' % system, X_pca[:,:2], fmt='%.7f')

################################################################################
