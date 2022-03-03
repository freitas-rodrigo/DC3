import matplotlib.pyplot as plt
cmap= plt.get_cmap('Blues')
from numpy import *

import sys
sys.path.append('/home/freitas/dc3/single_element/ml_rsf_only/util')
from constants import lattices

################################################################################
# Setup.                                                                       #
################################################################################

# Load confusion matrix and labels.
cm = loadtxt('../data/post_processed/confusion_matrix.dat')
true_labels = ['fcc (Al)', 'fcc (Ar)', 'bcc (Fe)', 'bcc (Li)', 'hcp (Ti)', 'hcp (Mg)', 'cd (Si)', 'cd (Ge)', 'hd (H$_2$O)', 'sc (NaCl)', 'liquid']
predicted_labels = ['fcc', 'bcc', 'hcp', 'cd', 'hd', 'sc', 'liquid', 'unknown\ncrystal']

# Round confusion matrix accuracy to one decimal place.
cm = around(cm,1)
for i in range(cm.shape[1]):
  cm[i] *= 100/sum(cm[i])

################################################################################
# Plot.                                                                        #
################################################################################

# Start figure.
fig = plt.figure()
ax = fig.add_axes([0.18, 0.05, 0.80, 0.80])

# Color matrix.
for j in range(cm.shape[1]):
  for i in range(cm.shape[0]):
    if around(cm[i,j],1) < 0.1:
      color = 0
    else:
      color = 0.18 + cm[i,j]/30
    ax.fill_between([j-0.5,j+0.5], i-0.5,i+0.5, color=cmap(color), lw=0)

# Plot lines.
for i in range(cm.shape[0]):
  plt.axhline(i-0.5,ls='-', c='k', lw=0.5)
for i in range(cm.shape[1]):
  plt.axvline(i-0.5,ls='-', c='k', lw=0.5)
plt.axvline(5.5,ls='-', c='k', lw=0.5)

# Write percentages.
for j in range(cm.shape[1]):
  for i in range(cm.shape[0]):
    ax.text(j,i, '%.1f%%' % cm[i,j], fontsize=10, horizontalalignment='center', verticalalignment='center')

# Add details.
ax.set_ylabel(r'True label',fontsize=17,labelpad=10)
ax.xaxis.tick_top()
ax.set_xlabel(r'Predicted label',fontsize=17,labelpad=5)
ax.xaxis.set_label_position('top')
ax.set_xticks(arange(cm.shape[1]))
ax.set_yticks(arange(cm.shape[0]))
ax.set_xticklabels(predicted_labels)
ax.set_yticklabels(true_labels)
ax.tick_params(axis='both', which='major', length=0)
ax.set_ylim(cm.shape[0]-0.5,-0.5)
ax.set_xlim(-0.5,cm.shape[1]-0.5)

# Save figure.
fig.savefig('figures/fig_confusion_matrix.pdf')
plt.close()

################################################################################

