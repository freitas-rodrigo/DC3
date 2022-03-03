from numpy import *
from MulticoreTSNE import MulticoreTSNE as TSNE
import joblib

import sys
sys.path.append('/home/freitas/dc3/two_elements/ml/util')
from constants import N_feat
from read_functions import read, read_partial

################################################################################
# Input parameters and setup.                                                  #
################################################################################

perplexity = int(sys.argv[1])

M = 10000 # Number of data points used in tSNE.
N_var_99 = 138 # Number of PCA components to explain 99% of the variance.

# Load MD crystal data for B2 structure.
X = read_partial('../02_organize_data/data/md_crystal/X.dat',10*M,N_feat)
y = read_partial('../02_organize_data/data/md_crystal/y.dat',10*M,1)
yT = read_partial('../02_organize_data/data/md_crystal/yT.dat',10*M,1)
X = X[y==3][:M]
yT = yT[y==3][:M]

# Add perfect structure points to the data set.
X_tmp = read('../02_organize_data/data/perfect_lattices/X.dat')
y_tmp = read('../02_organize_data/data/perfect_lattices/y.dat')
X = row_stack((X_tmp[y_tmp==3],X))

# Save labels used in tSNE.
savetxt('data/yT_tSNE_%d.dat' % perplexity, yT)

################################################################################
# Compute tSNE.                                                                #
################################################################################

pca = joblib.load('data/pca.pkl')
X_PCA = pca.transform(X)[:,:N_var_99]
X_tsne = TSNE(perplexity=perplexity,n_jobs=8).fit_transform(X_PCA)
savetxt('data/X_tSNE_temperature_dependence_%d.dat' % perplexity, X_tsne)

################################################################################
