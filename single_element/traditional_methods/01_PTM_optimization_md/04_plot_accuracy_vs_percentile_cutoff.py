import matplotlib.pyplot as plt                 
from numpy import *

################################################################################
# Things I'm reusing.                                                          #
################################################################################

materials = ['Al', 'Fe', 'Ti', 'Si', 'H$_2$O', 'NaCl', 'Ar', 'Li', 'Mg', 'Ge']
potentials = ['EAM', 'EAM', 'MEAM', 'EDIP', 'Stillinger-Weber', 'Tosi-Fumi', 'Lennard-Jones', 'SNAP', 'EAM', 'Tersoff']
structures = ['fcc', 'bcc', 'hcp', 'cd', 'hd', 'sc', 'fcc', 'bcc', 'hcp', 'cd']

lattices = ['fcc', 'bcc', 'hcp', 'cd', 'hd', 'sc', 'fcc_2', 'bcc_2', 'hcp_2',   'cd_2']

################################################################################
# Plot.                                                                        #
################################################################################

# Start figure.
fig = plt.figure(figsize=(10,10))

# Loop over all materials.
for j in range(2):
  for i in range(int(len(lattices)/2)):
    n = i + j*int(len(lattices)/2) 
    ax = fig.add_axes([0.08+j*0.47, 0.06+i*0.19, 0.43, 0.17])

    # Plot crystal distribution.
    x, acc_crystal = loadtxt('data/statistics/%s.dat' % lattices[n], unpack=True, usecols=[0,2])
    ax.plot(x, 100*acc_crystal, '-', lw=3, c='C3')

    # Plot liquid distribution.
    x, acc_liquid = loadtxt('data/statistics/%s_liquid.dat' % lattices[n], unpack=True, usecols=[0,2])
    ax.plot(x, 100*acc_liquid, '-', lw=3, c='C0')

    # Plot mean distribution.
    acc = (acc_liquid+acc_crystal)/2
    ax.plot(x, 100*acc, '-', lw=3, c='k')

    # Plot RMSD cutoff.
    RMSD_cutoff = loadtxt('data/RMSD_cutoff.dat')[n]
    plt.axvline(RMSD_cutoff, ls='-', c='C2', lw=2)

    # Write material and lattice.
    ax.text(0.988, 0.97, '%s (%s)' % (materials[n],structures[n].upper()), fontsize=15, horizontalalignment='right', verticalalignment='top', transform=ax.transAxes)

    # Axis labels.
    if i == 0: 
      ax.set_xlabel(r'RMSD cutoff',fontsize=18, fontweight='bold')
      ax.annotate(r'PTM accuracy (%)', xy=(0.01,0.4), xycoords='figure fraction', fontweight='bold', fontsize=22, rotation=90)
     
    # Control axes.
    ax.set_ylim(50,100)
    ax.set_xlim(0,0.6)
    if i != 0: ax.set_xticks([])

    # Set vertical dashed lines to align plots.
    for x in arange(0.10,0.60+0.01,0.10):
      plt.axvline(x=x, ls='--', c='k', lw=0.5)
fig.savefig("figures/fig_PTM_accuracy_vs_RMSD.png", dpi=400)
fig.savefig("figures/fig_PTM_accuracy_vs_RMSD.pdf")
plt.close()

################################################################################
