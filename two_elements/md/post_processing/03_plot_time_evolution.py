import matplotlib.pyplot as plt                 
from numpy import *
import sys
cm = plt.get_cmap('gist_rainbow')

################################################################################
# Load and process data.                                                       #
################################################################################

n = int(sys.argv[1]) # Lattice directory number.
lattice = sys.argv[2] # Lattice name.
T_ml = loadtxt('data/crystals_metastability_limit.dat', unpack=True, usecols=[1])[n-1]

# Load temperature range.
T = loadtxt('data/averages/%s.dat' % lattice, unpack=True, usecols=[0])

################################################################################
# Plot lattice parameter vs temperature.                                       #
################################################################################

# Start figure.
fig = plt.figure()
ax  = fig.add_axes([0.15, 0.15, 0.80, 0.80])

# Plot.
for i in range(len(T)):
  step, a, pe = loadtxt('../%02d_%s/data/thermo/thermo_%.2f.dat' % (n,lattice,T[i]), unpack=True)
  t = step * 0.001
  if isclose(T[i],T_ml):
    ax.plot(t, a, '-', c='k', label='%.2f' % T[i])
  else:
    ax.plot(t, a, '-', c=cm(i/(len(T)-1)), label='%.2f' % T[i])
 
# Add details and save figure.
ax.set_xlabel(r'Time [ps]')
ax.set_ylabel(r'Lattice parameter $[\mathring{A}]$')
ax.set_xlim(0,100)
ax.legend(fontsize=8,ncol=2)

# Save figure.
fig.savefig("figures/fig_%s_a_vs_t.png" % lattice, dpi=400)
plt.close()

################################################################################
# Plot lattice parameter vs temperature.                                       #
################################################################################

# Start figure.
fig = plt.figure()
ax  = fig.add_axes([0.16, 0.15, 0.80, 0.80])

# Plot.
for i in range(len(T)):
  step, a, pe = loadtxt('../%02d_%s/data/thermo/thermo_%.2f.dat' % (n,lattice,T[i]), unpack=True)
  t = step * 0.001
  if isclose(T[i],T_ml):
    ax.plot(t, pe, '-', c='k', label='%.2f' % T[i])
  else:
    ax.plot(t, pe, '-', c=cm(i/(len(T)-1)), label='%.2f' % T[i])
 
# Add details and save figure.
ax.set_xlabel(r'Time [ps]')
ax.set_ylabel(r'Lattice parameter $[\mathring{A}]$')
ax.set_xlim(0,100)
ax.legend(fontsize=6,ncol=2)

# Save figure.
fig.savefig("figures/fig_%s_pe_vs_t.png" % lattice, dpi=400)
plt.close()

################################################################################
