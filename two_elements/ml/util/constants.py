from numpy import *

# Information about lattices in the synthetic data set.
lattices = array(['L1_0', 'L1_2', 'B2', 'zincblende', 'rocksalt', 'wurtzite'])
n_lattices = len(lattices)
y_lattices = array([1,2,3,4,5,6])

# Information about lattices in MD simulations.
md_lattices = array(['L1_0', 'L1_2', 'B2', 'zincblende', 'rocksalt', 'wurtzite'])
n_md_lattices = len(md_lattices)
y_md_lattices = array([1,2,3,4,5,6])

# Number of features employed.
N_feat = 660
