import matplotlib.pyplot as plt
from numpy import *

import sys
sys.path.append('/home/freitas/dc3/two_elements/ml/util')
from constants import lattices, n_lattices, y_lattices
from read_functions import read

################################################################################
# Setup.                                                                       #
################################################################################

markers = ['o', 's', '^', 'D', 'v', 'P'] # Markers.
perplexity_list = [5,10,25,50,100,200,500,1000]
lattices_name = ['L1$_0$', 'L1$_2$', 'B2', 'Zincblende', 'Rocksalt', 'Wurtzite']

# Load data and find axis limits
for perplexity in perplexity_list:
  X = read('../data/X_tSNE_synthetic_crystal_%d.dat' % perplexity)
  y = read('../data/y_tSNE_synthetic_crystal_%d.dat' % perplexity)
  X0 = read('../data/X_tSNE_perfect_lattices_%d.dat' % perplexity)
  y0 = read('../data/y_tSNE_perfect_lattices_%d.dat' % perplexity)
  x_lim = 1.1*array([min(X[:,0]), max(X[:,0])])
  y_lim = 1.1*array([min(X[:,1]), max(X[:,1])])

################################################################################
# Plot synthetifc crystal data set.                                            #
################################################################################

  # Start figure.
  fig = plt.figure()
  ax = fig.add_axes([0.06, 0.06, 0.90, 0.90])

  # Plot.
  for i in range(n_lattices):
    ax.plot(X[y==y_lattices[i],0], X[y==y_lattices[i],1], 'C%d%s' % (i,markers[i]), alpha=0.15, mew=0, zorder=9-i, label=lattices_name[i])
    ax.plot(X0[y0==y_lattices[i],0], X0[y0==y_lattices[i],1], 'k%s' % markers[i], zorder=100)

  # Add details.
  ax.set_xlabel(r'First tSNE dimension', fontsize=18)
  ax.set_ylabel(r'Second tSNE dimension', fontsize=18)
  ax.set_xticks([])
  ax.set_yticks([])
  ax.set_xlim(x_lim)
  ax.set_ylim(y_lim)
  legend = plt.legend(handletextpad=0.1, loc='best', ncol=1, frameon=True, fontsize=14)
  for l in legend.legendHandles: 
    l._legmarker.set_alpha(1)

  # Save figure.
  fig.savefig("figures/fig_tSNE_synthetic_crystal_perplexity_%d.png" % perplexity, dpi=400)
  plt.close()

################################################################################
# Plot MD crystal data set.                                                    #
################################################################################

  X = read('../data/X_tSNE_md_crystal_%d.dat' % perplexity)
  y = read('../data/y_tSNE_md_crystal_%d.dat' % perplexity)

  # Start figure.
  fig = plt.figure()
  ax = fig.add_axes([0.06, 0.06, 0.90, 0.90])

  # Plot.
  for i in range(n_lattices):
    ax.plot(X[y==y_lattices[i],0], X[y==y_lattices[i],1], 'C%d%s' % (i,markers[i]), alpha=0.15, mew=0, zorder=9-i, label=lattices_name[i])
    ax.plot(X0[y0==y_lattices[i],0], X0[y0==y_lattices[i],1], 'k%s' % markers[i], zorder=100)

  # Add details.
  ax.set_xlabel(r'First tSNE dimension', fontsize=18)
  ax.set_ylabel(r'Second tSNE dimension', fontsize=18)
  ax.set_xticks([])
  ax.set_yticks([])
  ax.set_xlim(x_lim)
  ax.set_ylim(y_lim)
  legend = plt.legend(handletextpad=0.1, loc='best', ncol=1,frameon=True, fontsize=14)
  for l in legend.legendHandles: 
    l._legmarker.set_alpha(1)

  # Save figure.
  fig.savefig("figures/fig_tSNE_md_crystal_perplexity_%d.png" % perplexity, dpi=400)
  plt.close()

################################################################################
