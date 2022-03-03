import matplotlib.pyplot as plt
from numpy import *

import sys
sys.path.append('/home/freitas/dc3/two_elements/ml/util')
from constants import lattices, n_lattices, y_lattices
from read_functions import read, read_partial

################################################################################
# Setup.                                                                       #
################################################################################

markers = ['o', 's', '^', 'D', 'v', 'P'] # Markers.
N = 10000 # Number of points per class in plot.
M = 100000 # Number of examples processed in PCA.
lattices_name = ['L1$_0$', 'L1$_2$', 'B2', 'Zincblende', 'Rocksalt', 'Wurtzite']

init = True # Flag to set plot axis limits.
for system in ['synthetic_crystal', 'md_liquid', 'md_crystal']:
  # Load data and set axis limits.
  X = read('../data/X_PCA_%s.dat' % system)
  y = abs(read_partial('../../02_organize_data/data/%s/y.dat' % system, M,1))
  X0 = read('../data/X_PCA_perfect_lattices.dat')
  y0 = read_partial('../../02_organize_data/data/perfect_lattices/y.dat', M,1)
  if init:
    x_lim = [1.1*min(X[:,0]), 1.1*max(X[:,0])]
    y_lim = [1.1*min(X[:,1]), 1.1*max(X[:,1])]
    init = False

################################################################################
# Plot.                                                                        #
################################################################################
  
  # Start figure.
  fig = plt.figure()
  ax = fig.add_axes([0.06, 0.06, 0.90, 0.90])
  
  # Plot.
  for i in range(n_lattices):
    ax.plot(X[y==y_lattices[i],0][:N], X[y==y_lattices[i],1][:N], 'C%d%s' % (i,markers[i]), alpha=0.05, mew=0, zorder=9-i, label=lattices_name[i])
    ax.plot(X0[y0==y_lattices[i],0], X0[y0==y_lattices[i],1], 'k%s' % markers[i], zorder=100)
   
  # Add details.
  ax.set_xlabel(r'First PCA component', fontsize=18)
  ax.set_ylabel(r'Second PCA component', fontsize=18)
  ax.set_xticks([])
  ax.set_yticks([])
  ax.set_xlim(x_lim)
  ax.set_ylim(y_lim)
  legend = plt.legend(handletextpad=0.1, loc='best', ncol=1, frameon=True, fontsize=14)
  for l in legend.legendHandles:
    l._legmarker.set_alpha(1) # Set marker alpha to opaque.
  
  # Save figure.
  fig.savefig("figures/fig_PCA_%s.png" % system, dpi=400)
  plt.close()

################################################################################
