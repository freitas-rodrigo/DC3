from numpy import *

# Compute histograms.
alpha_sc = loadtxt("../data/synthetic_crystal/alpha.dat")
alpha_sl = loadtxt("../data/synthetic_liquid/alpha.dat")
alpha_mdc = loadtxt("../data/md_crystal/alpha.dat")
alpha_mdl = loadtxt("../data/md_liquid/alpha.dat")
rho_sc, x = histogram(alpha_sc,bins=1000,density=True,range=(-1,1))
rho_sl, x = histogram(alpha_sl,bins=1000,density=True,range=(-1,1))
rho_mdc, x = histogram(alpha_mdc,bins=1000,density=True,range=(-1,1))
rho_mdl, x = histogram(alpha_mdl,bins=1000,density=True,range=(-1,1))
x = x[:-1]
dx = x[1]-x[0]
savetxt('../data/post_processed/alpha_histograms.dat', transpose([x,rho_sc,rho_sl,rho_mdc,rho_mdl]), fmt='% .8f', header='bin | synthetic crystal | synthetic liquid | md crystal | md liquid')

# Compute cummulative sums.
f_cum_sc = 1-cumsum(rho_sc)*dx
f_cum_sl = cumsum(rho_sl)*dx
f_cum_mdc = 1-cumsum(rho_mdc)*dx
f_cum_mdl = cumsum(rho_mdl)*dx
f_cum = (f_cum_sc+f_cum_sl)/2
savetxt('../data/post_processed/f_cummulative_distribution.dat', array([x,f_cum_sc, f_cum_sl, f_cum_mdc, f_cum_mdl,f_cum]).T, fmt='% .8f', header='qq | f_cum_sc | f_cum_sl | f_cum_mdc | f_cum_mdl | f_cum')

# Define optimal cutoff as maximum of the mean accuracy.
args = nonzero(f_cum == max(f_cum))
alpha_cut = x[args].mean()

# Compute fractions using optimal cutoff.
f_mdc = f_cum_mdc[args].mean()
f_mdl = f_cum_mdl[args].mean()
with open('../data/post_processed/alpha_accuracy.dat', 'w') as f:
  f.write("alpha_cut: %.4f\n" % alpha_cut)
  f.write("fraction of correctly identified md crystal data: %.3f\n" % f_mdc)
  f.write("fraction of correctly identified md liquid data: %.3f\n" % f_mdl)
with open('../data/post_processed/alpha_cutoff.dat', 'w') as f:
  f.write("%.4f" % alpha_cut)
