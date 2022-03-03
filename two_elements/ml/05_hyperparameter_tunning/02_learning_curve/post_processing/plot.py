import matplotlib.pyplot as plt
from numpy import *

# Import my own modules.
import sys
sys.path.append('/home/users/freitas/structure_prediction/ml/08_stein_rsf_kernel_all_concat/util')
from constants import lattices, n_lattices

################################################################################
# Plot.                                                                        #
################################################################################

# Start figure.
fig = plt.figure()
ax  = fig.add_axes([0.15, 0.15, 0.80, 0.80])

# Plot.
for ilatt in range(n_lattices):
  m, acc_train_avg, acc_train_std, acc_valid_avg, acc_valid_std = loadtxt('../data/learning_curve_%s.dat' % lattices[ilatt], unpack=True)
  ax.plot(m, acc_train_avg, 'C%d-' % ilatt, lw=2, label='%s training set' % lattices[ilatt])
  ax.fill_between(m, acc_train_avg-acc_train_std, acc_train_avg+acc_train_std, color='C%d' % ilatt, alpha=0.2, lw=0)
  ax.plot(m, acc_valid_avg, 'C%d--o' % ilatt, lw=2, label='%s validation set' % lattices[ilatt])
  ax.fill_between(m, acc_valid_avg-acc_valid_std, acc_valid_avg+acc_valid_std, color='C%d' % ilatt, alpha=0.2, lw=0)
 
# Add details.
ax.set_xlabel(r'Training set size')
ax.set_ylabel(r'Accuracy')
ax.set_xscale('log')
ax.set_ylim(0.780,1.00)
ax.legend(fontsize=8,ncol=2)

# Save figure.
fig.savefig("fig_learning_curve.png", dpi=400)
plt.close()

################################################################################
