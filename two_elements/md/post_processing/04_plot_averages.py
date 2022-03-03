import matplotlib.pyplot as plt                 
from numpy import *
import sys

################################################################################
# Load and process data.                                                       #
################################################################################

n = int(sys.argv[1]) # Lattice directory number.
lattice = sys.argv[2] # Lattice name.
T_ml = loadtxt('data/crystals_metastability_limit.dat', unpack=True, usecols=[1])[n-1]
T, a, pe = loadtxt('data/averages/%s.dat' % lattice, unpack=True)

################################################################################
# Plot lattice parameter vs temperature.                                       #
################################################################################

# Start figure.
fig = plt.figure()
ax  = fig.add_axes([0.15, 0.15, 0.80, 0.80])

# Plot.
ax.plot(T, a, 'C0-o')
plt.axvline(x=T_ml, ls='--', c='k', lw=0.5)
 
# Add details and save figure.
ax.set_xlabel(r'$T/T_\mathrm{m}$')
ax.set_ylabel(r'Lattice parameter $[\mathring{A}]$')
ax.set_xlim(0,1.6)

fig.savefig("figures/fig_%s_a_vs_T.png" % lattice, dpi=400)
plt.close()

################################################################################
# Plot lattice parameter vs temperature.                                       #
################################################################################

# Start figure.
fig = plt.figure()
ax  = fig.add_axes([0.15, 0.15, 0.80, 0.80])

# Plot.
ax.plot(T, pe, 'C1-o')
plt.axvline(x=T_ml, ls='--', c='k', lw=0.5)
 
# Add details and save figure.
ax.set_xlabel(r'$T/T_\mathrm{m}$')
ax.set_ylabel(r'Potential energy [eV/atom]')
ax.set_xlim(0,1.6)

fig.savefig("figures/fig_%s_pe_vs_T.png" % lattice, dpi=400)
plt.close()

################################################################################
