from numpy import *
from sklearn.svm import SVC
from sklearn.model_selection import learning_curve

import sys
sys.path.append('/home/users/freitas/structure_prediction/ml/08_stein_rsf_kernel_all_concat/util')
from constants import lattices
from read_functions import read

################################################################################
# Input parameters and setup.                                                  #
################################################################################

# Setup variables.
lattice = sys.argv[1]
y_lattice = argmax(lattices==lattice) # Label of this lattice.

# Load data set.
X_train = read('../../02_order_features/data/synthetic/X_train.dat')
y_train = read('../../02_order_features/data/synthetic/y_train.dat')

# Training one-vs-all for each lattice.
y_train[y_train!=y_lattice] = -1
y_train[y_train==y_lattice] = 1

################################################################################
# Compute.                                                                     #
################################################################################

# Compute learning curve.
train_sizes = [60,100,200,300,400,500,600,700,800,900,1000,1500,2000,5000,7500,10000,15000,20000,25000,30000,35000,40000,48000]
m, acc_train, acc_valid = learning_curve(SVC(C=0.3,tol=1e-3,kernel='rbf',gamma='scale',class_weight='balanced',max_iter=10000), X_train, y_train, train_sizes=train_sizes, cv=5, n_jobs=-1)

# Compute mean and errors.
acc_train_avg = mean(acc_train, axis=1)
acc_train_std = std(acc_train, axis=1)
acc_valid_avg = mean(acc_valid, axis=1)
acc_valid_std = std(acc_valid, axis=1)
data = array([m, acc_train_avg, acc_train_std, acc_valid_avg, acc_valid_std])

# Save results.
savetxt('data/learning_curve_%s.dat' % lattice, data.T, header=' train set size | training score | valid score', fmt='%5d %.5f %.5f %.5f %.5f')

################################################################################
