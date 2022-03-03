from numpy import *
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_validate

import sys
sys.path.append('/home/freitas/dc3/single_element/ml/util')
from read_functions import read

################################################################################
# Input parameters and setup.                                                  #
################################################################################

f = int(sys.argv[1])/10

# Load data set.
X = read('../../02_organize_data/data/synthetic_crystal/X.dat')
y = read('../../02_organize_data/data/synthetic_crystal/y.dat')
idx = random.choice(arange(len(y)), int(f*len(y)), replace=False)
X = X[idx]
y = y[idx]

################################################################################
# Compute.                                                                     #
################################################################################

cv_results = cross_validate(MLPClassifier(early_stopping=True, hidden_layer_sizes=[100,100,100], learning_rate_init=0.005), X, y, cv=5, n_jobs=-1)
mean = cv_results['test_score'].mean()
std = cv_results['test_score'].std()
savetxt('../data/scores/learning_curve_%.1f.dat' % f, array([mean,std]), header=' mean | std ', fmt='%.4f')

################################################################################
