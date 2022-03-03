import matplotlib.pyplot as plt
from numpy import *

import sys
sys.path.append('/home/freitas/dc3/single_element/ml_rsf_only/util')
from constants import md_lattices, n_md_lattices

################################################################################
# Load and process data.                                                       #
################################################################################

# Crystal structure metastability limit.
T_ml = loadtxt('../../../md/post_processing/data/crystals_metastability_limit.dat', unpack=True, usecols=[1])

# Labels for legends.
lattice_name = ['face-centered cubic', 'body-centered cubic', 'hexagonal close-packed', 'cubic diamond', 'hexagonal diamond', 'simple cubic', 'face-centered cubic', 'body-centered cubic', 'hexagonal close-packed', 'cubic diamond']
potential_material = ['Al - EAM', 'Fe - EAM', 'Ti - MEAM', 'Si - EDIP', 'H$_2$O - Stillinger-Weber', 'NaCl - Tosi-Fumi', 'Ar - Lennard-Jones', 'Li - SNAP', 'Mg - EAM', 'Ge - Tersoff']

# Traditional methods labels and colors.
methods = [['PTM', 'iCNA', 'CNA', 'AJA', 'VTM'],
           ['PTM', 'iCNA', 'CNA', 'AJA', 'VTM'],
           ['PTM', 'iCNA', 'CNA', 'AJA', 'VTM'],
           ['PTM', 'CNA', 'CPA'],
           ['PTM', 'CNA', 'CPA'],
           ['PTM'],
           ['PTM', 'iCNA', 'CNA', 'AJA', 'VTM'],
           ['PTM', 'iCNA', 'CNA', 'AJA', 'VTM'],
           ['PTM', 'iCNA', 'CNA', 'AJA', 'VTM'],
           ['PTM', 'CNA', 'CPA']]
method_to_color = {'PTM':'C0', 
                   'iCNA':'C1', 
                   'CNA':'C2',
                   'AJA':'C3',
                   'VTM':'C4',
                   'CPA':'C5'}
method_to_name = {'PTM':'Polyhedral Template Matching', 
                  'iCNA':'interval Common Neighbor Analysis', 
                  'CNA':'Common Neighbor Analysis',
                  'AJA':'Ackland-Jones Analysis', 
                  'VTM':'VoroTop Analysis',
                  'CPA':'Chill+'}

################################################################################
# Plot accuracy vs temperature.                                                #
################################################################################

for i in range(n_md_lattices):
  T = arange(0.04,T_ml[i]+0.01,0.04) # Temperature range for current material.

  # Start figure.
  fig = plt.figure()
  ax  = fig.add_axes([0.15, 0.15, 0.80, 0.80])
  
  # Plot traditional methods results.
  for j in range(len(methods[i])):
    if methods[i][j] == 'VTM' and md_lattices[i] == 'fcc': continue
    if methods[i][j] == 'VTM' and md_lattices[i] == 'fcc_2': continue
    if methods[i][j] == 'VTM' and md_lattices[i] == 'hcp': continue
    if methods[i][j] == 'VTM' and md_lattices[i] == 'hcp_2': continue
    T, acc, acc_err = loadtxt('../../../traditional_methods/03_accuracies/data/accuracies/%s_%s.dat' % (methods[i][j],md_lattices[i]), unpack=True)
    ax.plot(T, acc, '-', c=method_to_color[methods[i][j]], label=method_to_name[methods[i][j]], lw=2)
    ax.fill_between(T, acc+acc_err, acc-acc_err, color=method_to_color[methods[i][j]],  alpha=0.3, lw=0)

  # Plot melting temperature line.
  plt.axvline(x=1,ls='--', c='k', lw=1.0)

  # Plot dc3 results.
  T, acc, acc_err = loadtxt('../data/post_processed/accuracy_vs_temperature_%s.dat' % md_lattices[i],unpack=True)
  ax.plot(T, acc, 'k-', label='Data-Centric Crystal Classifier', lw=2)
  ax.fill_between(T, acc+acc_err, acc-acc_err, color='k',  alpha=0.3, lw=0)
   
  # Labels and limits.
  ax.set_xlabel(r'$T/T_\mathrm{m}$', fontsize=18)
  ax.set_ylabel(r'Accuracy (%)', fontsize=18)
  ax.set_ylim(75,100.1)
  ax.set_xlim(0,T_ml[i])

  # Legend.
  lg = ax.legend(loc='lower left', fontsize=10, title=lattice_name[i].capitalize()+' (%s)' % potential_material[i], framealpha=1)
  lg.get_title().set_fontsize(10)
  lg.get_title().set_fontweight('bold')
  ax.tick_params(axis='both', which='major', labelsize=12)

  # Save figure.
  fig.savefig("figures/fig_accuracy_vs_temperature_%s.pdf" % md_lattices[i])
  plt.close()

################################################################################
