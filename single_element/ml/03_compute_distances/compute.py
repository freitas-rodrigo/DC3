from numpy import *

import sys
sys.path.append('/home/freitas/dc3/single_element/ml/util')
from constants import N_feat
from read_functions import read, read_partial
from dc3 import compute_distance

# Compute distances for synthetic crystal data.
X = read('../02_organize_data/data/synthetic_crystal/X.dat')
y = read('../02_organize_data/data/synthetic_crystal/y.dat')
d = compute_distance(X,y)
savetxt('data/distances_synthetic_crystal.dat', d, fmt='%9.6f')

# Compute distances for MD crystal data.
X = read_partial('../02_organize_data/data/md_crystal/X.dat',len(d),N_feat)
y = read_partial('../02_organize_data/data/md_crystal/y.dat',len(d),1)
d = compute_distance(X,abs(y))
savetxt('data/distances_md_crystal.dat', d, fmt='%9.6f')
