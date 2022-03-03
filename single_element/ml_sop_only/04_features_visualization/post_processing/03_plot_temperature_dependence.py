import matplotlib.pyplot as plt                 
import matplotlib as mpl
cm = plt.get_cmap('viridis')
from numpy import *

# Import my own modules.
import sys
sys.path.append('/home/freitas/dc3/single_element/ml_sop_only/util')
from read_functions import read

################################################################################
# Load and process data.                                                       #
################################################################################

perplexity_list = [5,10,25,50,100,200,500,1000]

################################################################################
# Plot.                                                                        #
################################################################################

for perplexity in perplexity_list:
  # Load results.
  X = read('../data/X_tSNE_temperature_dependence_%d.dat' % perplexity)
  yT = read('../data/yT_tSNE_%d.dat' % perplexity)

  # Start figure.
  fig = plt.figure()
  ax  = fig.add_axes([0.05, 0.06, 0.85, 0.90])
  
  # Plot.
  color = cm(yT/max(yT))
  ax.scatter(X[1:,0], X[1:,1], marker='^', alpha=0.3, color=color, lw=0, s=40)
  ax.plot(X[0,0], X[0,1], 'C3o', zorder=100, markersize=9)
   
  # Add details.
  ax.set_xlabel(r'First tSNE dimension', fontsize=18)
  ax.set_ylabel(r'Second tSNE dimension', fontsize=18)
  ax.set_xticks([])
  ax.set_yticks([])

  # Setup colorbar.
  ax_bar = fig.add_axes([0.92,0.05,0.015,0.90])
  norm = mpl.colors.Normalize(vmin=0, vmax=max(yT))
  cb = mpl.colorbar.ColorbarBase(ax_bar, cmap=cm, norm=norm, orientation='vertical', spacing='proportional')
  cb.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, max(yT)])
  cb.set_ticklabels(['0.0', '0.2', '0.4', '0.6', '0.8', '1.0', '%.2f' % max(yT)])
  cb.ax.tick_params(labelsize=10)
  cb.ax.set_title('$T/T_\mathrm{m}$', fontsize=12)
  
  # Save figure.
  fig.savefig("figures/fig_tSNE_temperature_dependence_perplexity_%d.pdf" % perplexity)
  plt.close()

################################################################################
