import matplotlib.pyplot as plt
from numpy import *

# Import my own modules.
import sys
sys.path.append('/home/users/freitas/structure_prediction/ml/09_nn_stein_rsf_concat_all/util')
from constants import lattices, n_lattices

################################################################################
# Plot.                                                                        #
################################################################################

# Start figure.
fig = plt.figure()
ax  = fig.add_axes([0.15, 0.15, 0.80, 0.80])

# Plot.
for ilatt in range(n_lattices):
  C, acc_train_avg, acc_train_std, acc_valid_avg, acc_valid_std = loadtxt('../data/validation_curve_C_%s.dat' % lattices[ilatt], unpack=True)
  ax.plot(C, acc_train_avg, 'C%d-' % ilatt, lw=2, label='%s training set' % lattices[ilatt])
  ax.fill_between(C, acc_train_avg-acc_train_std, acc_train_avg+acc_train_std, alpha=0.2, color='C%d' % ilatt, lw=0)
  ax.plot(C, acc_valid_avg, 'C%d--o' % ilatt, lw=2, label='%s validation set' % lattices[ilatt])
  ax.fill_between(C, acc_valid_avg-acc_valid_std, acc_valid_avg+acc_valid_std, alpha=0.2, color='C%d' % ilatt, lw=0)
   
# Add details.
ax.set_xlabel(r'C')
ax.set_ylabel(r'Accuracy')
ax.set_xscale('log')
ax.set_xlim(C.min(),C.max())
ax.set_ylim(0.80,1)
ax.legend(fontsize=8,ncol=2)

# Save figure.
fig.savefig("fig_validation_curve_C.png", dpi=400)
plt.close()

################################################################################
