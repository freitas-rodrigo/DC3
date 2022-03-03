from numpy import *

import sys
sys.path.append('/home/freitas/dc3/single_element/ml/util')
from constants import md_lattices
from read_functions import read

################################################################################
# Setup.                                                                       #
################################################################################

i = int(sys.argv[1]) # Crystal lattice.

# Crystal structure metastability limit.
T_ml = loadtxt('../../../md/post_processing/data/crystals_metastability_limit.dat', unpack=True, usecols=[1])

################################################################################
# Concatenate all temperatures in one file per lattice.                        #
################################################################################

for T in arange(0.04,T_ml[i]+0.01,0.04):
  X_tmp = read('../data/tmp/X_md_crystal_%s_%.2f.dat' % (md_lattices[i],T))
  alpha_tmp = read('../data/tmp/alpha_md_crystal_%s_%.2f.dat' % (md_lattices[i],T))
  yT_tmp = T*ones(X_tmp.shape[0])
  if T == 0.04:
    X = X_tmp
    yT = yT_tmp
    alpha = alpha_tmp
  else:
    X = row_stack((X,X_tmp))
    yT = concatenate((yT,yT_tmp))
    alpha = concatenate((alpha,alpha_tmp))
savetxt('../data/tmp/X_md_crystal_%s.dat' % md_lattices[i],X,fmt='%.8e')
savetxt('../data/tmp/yT_md_crystal_%s.dat' % md_lattices[i],yT,fmt='%.2f')
savetxt('../data/tmp/alpha_md_crystal_%s.dat' % md_lattices[i],alpha,fmt='%.6f')

################################################################################
