import matplotlib.pyplot as plt                 
from numpy import *

################################################################################
# Load and process data.                                                       #
################################################################################

# Crystal structure metastability limit temperature.
T_ml = loadtxt('../../md/post_processing/data/crystals_metastability_limit.dat', unpack=True, usecols=[1])

lattices = ['fcc', 'bcc', 'hcp', 'cd', 'hd', 'sc', 'fcc_2', 'bcc_2', 'hcp_2', 'cd_2']

methods = [['PTM', 'PTM_synthetic', 'iCNA', 'CNA', 'AJA', 'VTM'],
           ['PTM', 'PTM_synthetic', 'iCNA', 'CNA', 'AJA', 'VTM'],
           ['PTM', 'PTM_synthetic', 'iCNA', 'CNA', 'AJA', 'VTM'],
           ['PTM', 'PTM_synthetic', 'CNA', 'CPA'],
           ['PTM', 'PTM_synthetic', 'CNA', 'CPA'],
           ['PTM', 'PTM_synthetic'],
           ['PTM', 'PTM_synthetic', 'iCNA', 'CNA', 'AJA', 'VTM'],
           ['PTM', 'PTM_synthetic', 'iCNA', 'CNA', 'AJA', 'VTM'],
           ['PTM', 'PTM_synthetic', 'iCNA', 'CNA', 'AJA', 'VTM'],
           ['PTM', 'PTM_synthetic', 'CNA', 'CPA']]

method_to_color = {'PTM':'C0', 
                   'PTM_synthetic':'C1', 
                   'iCNA':'C2', 
                   'CNA':'C3',
                   'AJA':'C4',
                   'VTM':'C5',
                   'CPA':'C6'}

method_to_name = {'PTM':'Polyhedral Template Matching', 
                  'PTM_synthetic':'Polyhedral Template Matching (synthetic)', 
                  'iCNA':'interval Common Neighbor Analysis', 
                  'CNA':'Common Neighbor Analysis',
                  'AJA':'Ackland-Jones Analysis', 
                  'VTM':'VoroTop Analysis',
                  'CPA':'Chill+'}

################################################################################
# Plot.                                                                        #
################################################################################

for i in range(len(lattices)):
  T = arange(0.04,T_ml[i]+0.01,0.04)

  # Start figure.
  fig = plt.figure()
  ax  = fig.add_axes([0.15, 0.15, 0.80, 0.80])
  
  # Plot.
  for j in range(len(methods[i])):
    T, acc_avg, acc_err = loadtxt('data/accuracies/%s_%s.dat' % (methods[i][j],lattices[i]), unpack=True)
    ax.plot(T, acc_avg, '-', c=method_to_color[methods[i][j]], label=method_to_name[methods[i][j]], lw=2)
    ax.fill_between(T, acc_avg-acc_err, acc_avg+acc_err, color=method_to_color[methods[i][j]], alpha=0.3, lw=0)
  plt.axvline(x=1,ls='--', c='k', lw=1.0)

  # Add details and save figure.
  ax.set_xlabel(r'$T/T_\mathrm{m}$')
  ax.set_ylabel(r'Accuracy')
  ax.set_ylim(75,100.1)
  ax.set_xlim(0,T_ml[i])
  ax.legend(loc='lower left', fontsize=8)

  # Save figure.
  fig.savefig("figures/fig_accuracy_vs_temperature_%s.png" % lattices[i], dpi=400)
  plt.close()

################################################################################
