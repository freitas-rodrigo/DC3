import matplotlib.pyplot as plt
from numpy import *

import sys
sys.path.append('/home/freitas/dc3/single_element/ml_rsf_only/util')
from constants import lattices, md_lattices, y_lattices, y_md_lattices

################################################################################
# Setup.                                                                       #
################################################################################

# Load 99% percentile cutoff.
d_cut = loadtxt('../data/post_processed/distance_cutoff_vs_lattice.dat')

lattice_name = ['face-centered cubic', 'body-centered cubic', 'hexagonal close- packed', 'cubic diamond', 'hexagonal diamond', 'simple cubic', 'face-centered cubic', 'body-centered cubic', 'hexagonal close-packed', 'cubic diamond']
potential_material = ['Al - EAM', 'Fe - EAM', 'Ti - MEAM', 'Si - EDIP', 'H$_2$O - Stillinger-Weber', 'NaCl - Tosi-Fumi', 'Ar - Lennard-Jones', 'Li - SNAP', 'Mg - EAM', 'Ge - Tersoff']
material = ['Al', 'Fe', 'Ti', 'Si', 'H$_2$O', 'NaCl', 'Ar', 'Li', 'Mg', 'Ge']

################################################################################
# Plot.                                                                        #
################################################################################

for i in range(len(md_lattices)):
  # Find argument of lattices with the same structure as md_lattices.
  arg = argwhere(y_lattices==abs(y_md_lattices[i]))[0][0]

  # Start figure.
  fig = plt.figure()
  ax = fig.add_axes([0.15, 0.15, 0.80, 0.80])

  # Plot MD.
  x, rho = loadtxt('../data/post_processed/histogram_md_crystal_%s.dat' % md_lattices[i], unpack=True)
  ax.plot(x, rho, 'C7-', label='Molecular Dynamics (%s)' % material[i], lw=3)

  # Plot synthetic.
  x, rho = loadtxt('../data/post_processed/histogram_synthetic_crystal_%s.dat' % lattices[arg], unpack=True)
  ax.plot(x, rho, 'C0-', label='Synthetic data set', lw=3, zorder=2)
  plt.axvline(d_cut[arg], ls='--', c='C0', lw=1, label='99th percentile')

  # Add details.
  ax.set_xlabel(r'Distance $\delta(\mathbf{x},\mathbf{x}^*({y}))$', fontsize=18)
  ax.set_ylabel(r'Density distribution', fontsize=18)
  ax.set_xlim(0,60)
  ax.set_ylim(0)
  lg = ax.legend(fontsize=10, title='%s structure'%lattices[arg], framealpha=1)
  lg.get_title().set_fontsize(12)
  lg.get_title().set_fontweight('bold')
  ax.tick_params(axis='both', which='major', labelsize=12)
  
  # Save figure.
  fig.savefig("figures/fig_distance_histogram_%s.pdf" % md_lattices[i])
  plt.close()

################################################################################
