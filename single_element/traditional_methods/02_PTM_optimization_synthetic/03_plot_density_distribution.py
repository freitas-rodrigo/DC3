import matplotlib.pyplot as plt                 
from numpy import *

################################################################################
# Setup.                                                                       #
################################################################################

lattices = ['fcc', 'bcc', 'hcp', 'cd', 'hd', 'sc']

################################################################################
# Plot.                                                                        #
################################################################################

# Start figure.
fig = plt.figure(figsize=(10,7))

# Loop over all lattices.
for j in range(2):
  for i in range(int(len(lattices)/2)):
    n = i + j*int(len(lattices)/2) 
    ax = fig.add_axes([0.08+j*0.47, 0.08+i*0.31, 0.43, 0.27])

    # Plot crystal distribution.
    x, h = loadtxt('data/statistics/%s.dat' % lattices[n], unpack=True, usecols=[0,1])
    ax.plot(x, h, '-', lw=3, c='C3')

    # Plot liquid distribution.
    x, h = loadtxt('data/statistics/liquid.dat' , unpack=True, usecols=[0,1])
    ax.plot(x, h, '-', lw=3, c='C0')

    # Plot RMSD cutoff.
    RMSD_cutoff = loadtxt('data/RMSD_cutoff.dat')[n]
    plt.axvline(RMSD_cutoff, ls='-', c='C2', lw=2)

    # Write lattice name.
    ax.text(0.988, 0.97, '%s' % (lattices[n].upper()), fontsize=15, horizontalalignment='right', verticalalignment='top', transform=ax.transAxes)

    # Axis labels.
    if i == 0: 
      ax.set_xlabel(r'RMSD',fontsize=18, fontweight='bold')
      ax.annotate(r'Density distribution', xy=(0.01,0.4), xycoords='figure fraction', fontweight='bold', fontsize=22, rotation=90)
     
    # Control axes.
    ax.set_ylim(0)
    ax.set_xlim(0,0.6)
    if i != 0: ax.set_xticks([])

    # Set vertical dashed lines to align plots.
    for x in arange(0.10,0.60+0.01,0.10):
      plt.axvline(x=x, ls='--', c='k', lw=0.5)
fig.savefig("figures/fig_RMSD_density_distribution.png", dpi=400)
fig.savefig("figures/fig_RMSD_density_distribution.pdf")
plt.close()

################################################################################
