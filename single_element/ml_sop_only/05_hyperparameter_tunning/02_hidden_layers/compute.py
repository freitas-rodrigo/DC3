from numpy import *
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_validate

import sys
sys.path.append('/home/freitas/dc3/single_element/ml_sop_only/util')
from read_functions import read

################################################################################
# Input parameters and setup.                                                  #
################################################################################

n = int(sys.argv[1])
hidden_layer_sizes = n*[100]

# Load data set.
X = read('../../02_organize_data/data/synthetic_crystal/X.dat')
y = read('../../02_organize_data/data/synthetic_crystal/y.dat')

################################################################################
# Compute.                                                                     #
################################################################################

cv_results = cross_validate(MLPClassifier(early_stopping=True, hidden_layer_sizes=hidden_layer_sizes, learning_rate_init=0.005), X, y, cv=5, n_jobs=-1)
mean = cv_results['test_score'].mean()
std = cv_results['test_score'].std()
savetxt('../data/scores/hidden_layers_%d.dat' % n, array([mean,std]), header=' mean | std ', fmt='%.4f')

################################################################################
