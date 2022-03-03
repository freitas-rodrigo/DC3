from numpy import *
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier

import sys
sys.path.append('/home/users/freitas/structure_prediction/ml/09_nn_stein_rsf_concat_all/util')
from constants import lattices
from read_functions import read

################################################################################
# Input parameters and setup.                                                  #
################################################################################

max_layers = 2
max_width = 10
delta_width = 2

# Create list of nn topologies.
topology = []
for n in range(1,max_layers+1):
  x = ones((10,n),dtype=int)
  for i in range(delta_width,max_width+1,delta_width):
    x[i-1] *= i
    topology.append(x[i-1])
parameter_grid = [{'hidden_layer_sizes': topology}] 
print(topology)

# Load data set.
X_train = read('../../03_order_features/data/synthetic/X_train.dat')
y_train = read('../../03_order_features/data/synthetic/y_train.dat')

################################################################################
# Compute.                                                                     #
################################################################################

# Perform grid search.
clf = GridSearchCV(MLPClassifier(tol=0,max_iter=5,early_stopping=True), parameter_grid, cv=5, n_jobs=-1, return_train_score=True)
clf.fit(X_train,y_train)

# Save best parameters.
with open('data/best_parameters.dat', 'w') as f:
  f.write('Best parameters: %r\n' % clf.best_params_)
  f.write('Accuracy: %.5f' % clf.best_score_)

print(clf.cv_results_['mean_train_score'])
print(clf.cv_results_['std_train_score'])
print(clf.cv_results_['mean_test_score'])
print(clf.cv_results_['std_test_score'])

for n in range(1,max_layers+1):
  N = int(max_width/delta_width)
  data = zeros((N,5))
  data[0] = arange(delta_width,max_width+1,delta_width)
  for i in range(1,N+1):
    data[1][i] = clf.cv_results_['mean_train_score'][(i-1)*n]
    data[2][i] = clf.cv_results_['std_train_score'][i-1]
    data[3][i] = clf.cv_results_['mean_test_score'][i-1]
    data[4][i] = clf.cv_results_['std_test_score'][i-1]
  savetxt('data/validation_curve_%d_layers.dat' % n, data.T, header=' width | training score | valid score', fmt='%.0e %.5f %.5f %.5f %.5f')

################################################################################
