from numpy import *
from scipy.integrate import cumtrapz

################################################################################
# Setup.                                                                       #
################################################################################

lattices = ['fcc', 'bcc', 'hcp', 'cd', 'hd', 'sc', 'fcc_2', 'bcc_2', 'hcp_2', 'cd_2']

# Dictionary of PTM lattice labels in Ovito.
lattice_to_y = {'other':0, 'fcc':1, 'hcp':2, 'bcc':3, 'sc':5, 'cd':6, 'hd':7, 'fcc_2':1, 'hcp_2':2, 'bcc_2':3, 'cd_2':6}

################################################################################
# Compute maximum accuracy for each material.                                  #
################################################################################

max_acc_crystal = zeros(len(lattices))
for n in range(len(lattices)):
  y = loadtxt('data/y/y_%s.dat' % lattices[n])
  max_acc_crystal[n] = sum(y==lattice_to_y[lattices[n]]) / len(y)
savetxt('data/maximum_accuracy_crystal.dat', max_acc_crystal, fmt='%.10f')

################################################################################
# Statistics for the crystal predictions.                                      #
# Compute histogram of RMSD for correctly labeled points. Also computes the    #
# cummulative integral of this histogram, which corresponds to the fraction of #
# the maximum possible accuracy achieved with that RMSD.                       #
################################################################################

for n in range(len(lattices)):
  RMSD = loadtxt('data/RMSD/RMSD_%s.dat' % lattices[n])
  y = loadtxt('data/y/y_%s.dat' % lattices[n])
  RMSD = RMSD[y==lattice_to_y[lattices[n]]]
  h, x = histogram(RMSD,bins=200,range=[0,0.6],density=True)  
  x = x[:-1] + (x[1]-x[0])/2
  cumm_distribution = cumtrapz(h,x,initial=0)
  accuracy = cumm_distribution * max_acc_crystal[n]
  savetxt('data/statistics/%s.dat' % lattices[n], column_stack((x,h,accuracy)), fmt='%.10f %13.10f %.10f', header='RMSD | histogram | PTM accuracy')

################################################################################
# Compute minimum accuracy for each material' liquid phase.                    #
################################################################################

min_acc_liquid = zeros(len(lattices))
for n in range(len(lattices)):
  y = loadtxt('data/y/y_%s_liquid.dat' % lattices[n])
  min_acc_liquid[n] = sum(y==lattice_to_y['other']) / len(y)
savetxt('data/minimum_accuracy_liquid.dat', min_acc_liquid, fmt='%.10f')

################################################################################
# Statistics for the liquid predictions.                                       #
# Compute histogram of RMSD for incorrectly labeled points. Also computes the  #
# cummulative integral of this histogram, which corresponds to the fraction of #
# the remaning accuracy (i.e. 1 - minimum liquid accuracy) achieved with that  #
# RMSD.                                                                        #
################################################################################

for n in range(len(lattices)):
  RMSD = loadtxt('data/RMSD/RMSD_%s_liquid.dat' % lattices[n])
  y = loadtxt('data/y/y_%s_liquid.dat' % lattices[n])
  RMSD = RMSD[y!=lattice_to_y['other']]
  h, x = histogram(RMSD,bins=200,range=[0,0.6],density=True)  
  x = x[:-1] + (x[1]-x[0])/2
  cumm_distribution = cumtrapz(h,x,initial=0)
  accuracy = min_acc_liquid[n] + (1-cumm_distribution) * (1-min_acc_liquid[n])
  savetxt('data/statistics/%s_liquid.dat' % lattices[n], column_stack((x,h,accuracy)), fmt='%.10f %13.10f %.10f', header='RMSD | histogram | PTM accuracy')

################################################################################
# Computes optimal RMSD cutoff.                                                #
################################################################################

RMSD_cutoff = zeros(len(lattices))
for n in range(len(lattices)):
  RMSD, acc_crystal = loadtxt('data/statistics/%s.dat' % lattices[n], unpack=True, usecols=[0,2])
  RMSD, acc_liquid = loadtxt('data/statistics/%s_liquid.dat' % lattices[n], unpack=True, usecols=[0,2])
  mean_accuracy = (acc_crystal+acc_liquid)/2
  RMSD_cutoff[n] = RMSD[mean_accuracy == max(mean_accuracy)][0]
savetxt('data/RMSD_cutoff.dat', RMSD_cutoff, fmt='%.5f', header='RMSD | histogram | PTM accuracy')

################################################################################
# Computes PTM crystal and liquid accuracies with optimal RMSD cutoff.         #
################################################################################

opt_acc_crystal = zeros(len(lattices))
opt_acc_liquid = zeros(len(lattices))
for n in range(len(lattices)):
  RMSD, acc_crystal = loadtxt('data/statistics/%s.dat' % lattices[n], unpack=True, usecols=[0,2])
  RMSD, acc_liquid = loadtxt('data/statistics/%s_liquid.dat' % lattices[n], unpack=True, usecols=[0,2])
  opt_acc_crystal[n] = acc_crystal[RMSD==RMSD_cutoff[n]]
  opt_acc_liquid[n] = acc_liquid[RMSD==RMSD_cutoff[n]]
savetxt('data/optimal_accuracies.dat', column_stack((opt_acc_crystal,opt_acc_liquid)), header='Optimal accuracy crystal | Optimal accuracy liquid', fmt='%.5f %.5f')

################################################################################
