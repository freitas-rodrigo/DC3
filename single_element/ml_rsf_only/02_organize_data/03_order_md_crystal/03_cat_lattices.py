from numpy import *
from sklearn.utils import shuffle

import sys
sys.path.append('/home/freitas/dc3/single_element/ml_rsf_only/util')
from constants import md_lattices, n_md_lattices, y_md_lattices
from read_functions import read

################################################################################
# Concatenate all lattices in one file.                                        #
################################################################################

for i in range(n_md_lattices):
  X_tmp = read('../data/tmp/X_md_crystal_%s.dat' % md_lattices[i])
  alpha_tmp = read('../data/tmp/alpha_md_crystal_%s.dat' % md_lattices[i])
  yT_tmp = read('../data/tmp/yT_md_crystal_%s.dat' % md_lattices[i])
  y_tmp = y_md_lattices[i]*ones(X_tmp.shape[0])
  if 'X' in locals():
    X = row_stack((X,X_tmp))
    alpha = concatenate((alpha,alpha_tmp))
    y = concatenate((y,y_tmp))
    yT = concatenate((yT,yT_tmp))
  else:
    X = X_tmp
    y = y_tmp
    yT = yT_tmp
    alpha = alpha_tmp
X, y, yT, alpha = shuffle(X,y,yT,alpha)
savetxt('../data/md_crystal/X.dat',X,fmt='%.8e')
savetxt('../data/md_crystal/alpha.dat',alpha,fmt='%.6f')
savetxt('../data/md_crystal/y.dat',y,fmt='%d')
savetxt('../data/md_crystal/yT.dat',yT,fmt='%.2f')

################################################################################
