import matplotlib.pyplot as plt
from numpy import *

import sys
sys.path.append('/home/freitas/dc3/two_elements/ml/util')
from constants import md_lattices, n_md_lattices

################################################################################
# Load and process data.                                                       #
################################################################################

# Crystal structure metastability limit.
T_ml = loadtxt('../../../md/post_processing/data/crystals_metastability_limit.dat', unpack=True, usecols=[1])

# Labels for legends.
legend_labels = ['L1$_0$ (CuNi - EAM)', 'L1$_2$ (CuNi - EAM)', 'B2 (CoAl - EAM)', 'Zincblende (InP - SNAP)', 'Rocksalt (NaCl - Tosi-Fumi)', 'Wurtzite (ZnO - ReaxFF)']

################################################################################
# Plot accuracy vs temperature.                                                #
################################################################################

# Start figure.
fig = plt.figure()
ax  = fig.add_axes([0.15, 0.15, 0.80, 0.80])
  
# Plot dc3 results.
for i in range(n_md_lattices):
  T, acc, acc_err = loadtxt('../data/post_processed/accuracy_vs_temperature_%s.dat' % md_lattices[i],unpack=True)
  ax.plot(T, acc, 'C%d-' % i, label=legend_labels[i], lw=3)
  ax.fill_between(T, acc+acc_err, acc-acc_err, color='C%d' % i, alpha=0.3, lw=0)

# Plot melting temperature line.
plt.axvline(x=1,ls='--', c='k', lw=1.0)

# Add details and save figure.
ax.set_xlabel(r'$T/T_\mathrm{m}$', fontsize=18)
ax.set_ylabel(r'Accuracy (%)', fontsize=18)
ax.set_ylim(85,100.5)
ax.set_xlim(0,max(T_ml))
lg = ax.legend(loc='lower left', fontsize=10, title='Data-Centric Crystal Classifier')
lg.get_title().set_fontsize(10)
lg.get_title().set_fontweight('bold')
ax.tick_params(axis='both', which='major', labelsize=12)

# Save figure.
fig.savefig("figures/fig_accuracy_vs_temperature.png", dpi=400)
fig.savefig("figures/fig_two_elements_accuracy_vs_temperature.pdf")
plt.close()

################################################################################
