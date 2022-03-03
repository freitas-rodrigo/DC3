import matplotlib.pyplot as plt                 
from numpy import *

################################################################################
# Load and process data.                                                       #
################################################################################

x, rho_sc, rho_sl, rho_mdc, rho_mdl = loadtxt("../data/post_processed/alpha_histograms.dat", unpack=True)

x, f_cum_sc, f_cum_sl, f_cum_mdc, f_cum_mdl, f_cum = loadtxt("../data/post_processed/f_cummulative_distribution.dat", unpack=True)

alpha_cut = loadtxt("../data/post_processed/alpha_cutoff.dat")

################################################################################
# Plot alpha density distribution.                                             #
################################################################################

# Start figure.
fig = plt.figure()
ax  = fig.add_axes([0.15, 0.15, 0.80, 0.80])

# Plot.
ax.plot(x,rho_sc, 'C1-', lw=3, label='Crystal (synthetic)')
ax.plot(x,rho_sl, 'C2-', lw=3, label='Liquid (synthetic)')
ax.plot(x,rho_mdc, 'C3-', lw=1, label='MD crystal')
ax.plot(x,rho_mdl, 'C4-', lw=1, label='MD liquid')
plt.axvline(alpha_cut, ls='--', c='k', lw=0.5)
 
# Add details.
ax.set_xlabel(r'$\alpha$', size=18)
ax.set_ylabel(r'Density distribution', size=18)
ax.set_ylim(0)
ax.set_xlim(-1,1)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.legend()

# Save figure.
fig.savefig("figures/fig_alpha_histogram.pdf")
plt.close()

################################################################################
# Plot alpha cummulative sum.                                                  #
################################################################################

# Start figure.
fig = plt.figure()
ax  = fig.add_axes([0.15, 0.15, 0.80, 0.80])

# Plot.
ax.plot(x, f_cum_sc, 'C1-', lw=3, label='Crystal (synthetic)')
ax.plot(x, f_cum_sl, 'C2-', lw=3, label='Liquid (synthetic)')
ax.plot(x, f_cum_mdc, 'C3-', lw=1, label='MD crystal')
ax.plot(x, f_cum_mdl, 'C4-', lw=1, label='MD liquid')
ax.plot(x, f_cum, 'k-', lw=3, label='Average')
plt.axvline(alpha_cut, ls='--', c='k', lw=0.5)
 
# Add details.
ax.set_xlabel(r'$\alpha_\mathrm{cut}$', size=18)
ax.set_ylabel(r'Fraction of correctly identified atoms', size=17)
ax.set_ylim(0)
ax.set_xlim(-1,1)
ax.legend()

# Save figure.
fig.savefig("figures/fig_alpha_cummulative_distribution.pdf")
plt.close()

################################################################################
