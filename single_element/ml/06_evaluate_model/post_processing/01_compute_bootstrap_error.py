from numpy import *
from numpy.random import choice

import sys
sys.path.append('/home/freitas/dc3/single_element/ml/util')
from constants import md_lattices, n_md_lattices, y_md_lattices
from read_functions import read

################################################################################
# Setup.                                                                       #
################################################################################

M = 200 # Boostrap instances.

# Compute 95% confidence interval using boostrap.
def bootstrap(y,y_true):
  acc_avg = sum(y==y_true)/len(y)
  acc = zeros(M)
  for m in range(M):
    new_y = choice(y,len(y))
    acc[m] = sum(new_y==y_true)/len(y)
  acc = sort(acc)
  acc = acc[int(0.025*M):int(0.975*M)]
  return 100*acc_avg, 100*(acc.max()-acc.min())/2

################################################################################
# Compute confidence interval for MD liquid.                                   #
################################################################################

y_pred = read('../data/y_pred_md_liquid.dat')
acc_avg, acc_err = bootstrap(y_pred,0)

# Save average and confidence intervals.
savetxt('../data/post_processed/accuracy_liquid.dat', array([[acc_avg,acc_err]]), fmt='%.3f %.3f', header='Accuracy | 95% CI')

################################################################################
# Compute confidence interval for each temperature separately.                 #
################################################################################

# Crystal structure metastability limit.
T_ml = loadtxt('../../../md/post_processing/data/crystals_metastability_limit.dat', unpack=True, usecols=[1])

# Load labels.
y_true = read('../../02_organize_data/data/md_crystal/y.dat')
yT = read('../../02_organize_data/data/md_crystal/yT.dat')
y_pred = read('../data/y_pred_md_crystal.dat')

# Loop over each lattice and temperature to compute confidence intervals.
for i in range(n_md_lattices):
  T = arange(0.04,T_ml[i]+0.01,0.04)
  acc_avg = zeros(len(T))
  acc_err = zeros(len(T))
  for j in range(len(T)):
    cond = isclose(yT,T[j],atol=0.001)*(y_true==y_md_lattices[i])
    acc_avg[j], acc_err[j] = bootstrap(y_pred[cond],abs(y_md_lattices[i]))
  savetxt('../data/post_processed/accuracy_vs_temperature_%s.dat' % md_lattices[i], array([T,acc_avg,acc_err]).T, fmt='%.2f %.3f %.3f', header='homologous temperature | accuracy | 95% CI')

################################################################################
