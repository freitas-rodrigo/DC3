from numpy import *

import sys
sys.path.append('/home/freitas/dc3/single_element/ml_rsf_only/util')
from dc3 import dc3
from read_functions import read

system = sys.argv[1] # Specify data set.

# Load data set and compute dc3 predictions.
X = read('../02_organize_data/data/%s/X.dat' % system)
alpha = read('../02_organize_data/data/%s/alpha.dat' % system)
y_pred = dc3(X,alpha)

# Save dc3 predictions.
savetxt('data/y_pred_%s.dat' % system, y_pred, fmt='%d')
