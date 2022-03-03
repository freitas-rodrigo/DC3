from numpy import *
from MulticoreTSNE import MulticoreTSNE as TSNE
import joblib

import sys
sys.path.append('/home/freitas/dc3/single_element/ml/util')
from constants import N_feat
from read_functions import read, read_partial

################################################################################
# Input parameters and setup.                                                  #
################################################################################

perplexity = int(sys.argv[1])

M = 10000 # Number of data points used in tSNE.
N_var_99 = 129 # Number of PCA components to explain 99% of the variance.

# Load MD crystal data for hcp structure.
X = read_partial('../02_organize_data/data/md_crystal/X.dat',10*M,N_feat)
y = read_partial('../02_organize_data/data/md_crystal/y.dat',10*M,1)
yT = read_partial('../02_organize_data/data/md_crystal/yT.dat',10*M,1)
X = X[y==3][:M]
yT = yT[y==3][:M]

# Add perfect structure point to the data set.
X_tmp = read('../02_organize_data/data/perfect_lattices/X.dat')
X = row_stack((X_tmp[2],X))

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
