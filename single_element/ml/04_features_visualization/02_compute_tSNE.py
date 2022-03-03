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

# Load synthetic crystal data.
X = read_partial('../02_organize_data/data/synthetic_crystal/X.dat',M,N_feat)
y = read_partial('../02_organize_data/data/synthetic_crystal/y.dat',M,1)

# Add perfect lattices to the data set.
X_tmp = read('../02_organize_data/data/perfect_lattices/X.dat')
X = row_stack((X_tmp,X))
y = concatenate(([1,2,3,4,5,6],y))

# Load MD crystal data.
X_tmp = read_partial('../02_organize_data/data/md_crystal/X.dat',3*M,N_feat)
y_tmp = read_partial('../02_organize_data/data/md_crystal/y.dat',3*M,1)
X_tmp = X_tmp[y_tmp > 0][:M]
y_tmp = y_tmp[y_tmp > 0][:M]
X = row_stack((X,X_tmp))
y = concatenate((y,y_tmp))

# Save labels used in tSNE.
savetxt('data/y_tSNE_perfect_lattices_%d.dat' % perplexity, y[:6])
savetxt('data/y_tSNE_synthetic_crystal_%d.dat' % perplexity, y[6:M+6])
savetxt('data/y_tSNE_md_crystal_%d.dat' % perplexity, y[M+6:])

################################################################################
# Compute tSNE.                                                                #
################################################################################

pca = joblib.load('data/pca.pkl')
X_PCA = pca.transform(X)[:,:N_var_99]
X_tsne = TSNE(perplexity=perplexity,n_jobs=8).fit_transform(X_PCA)
savetxt('data/X_tSNE_perfect_lattices_%d.dat' % perplexity, X_tsne[:6])
savetxt('data/X_tSNE_synthetic_crystal_%d.dat' % perplexity, X_tsne[6:M+6])
savetxt('data/X_tSNE_md_crystal_%d.dat' % perplexity, X_tsne[M+6:])

################################################################################
