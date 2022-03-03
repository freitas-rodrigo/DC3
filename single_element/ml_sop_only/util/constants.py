from numpy import *

# Information about lattices in the synthetic data set.
lattices = array(['fcc','bcc','hcp','cd','hd','sc'])
n_lattices = len(lattices)
y_lattices = array([1,2,3,4,5,6])

# Information about lattices in MD simulations.
md_lattices = array(['fcc','bcc','hcp','cd','hd','sc','fcc_2','bcc_2','hcp_2','cd_2'])
n_md_lattices = len(md_lattices)
y_md_lattices = array([1,2,3,4,5,6,-1,-2,-3,-4])

# Number of features employed.
N_feat = 225
