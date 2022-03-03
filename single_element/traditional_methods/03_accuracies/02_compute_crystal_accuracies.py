from numpy import *
from numpy.random import choice
import sys

################################################################################
# Load and process data.                                                       #
################################################################################

#method = sys.argv[1]
method = "PTM_synthetic"

# Crystal structure metastability limit temperature.
T_ml = loadtxt('../../md/post_processing/data/crystals_metastability_limit.dat', unpack=True, usecols=[1])
md_lattices = array(['fcc', 'bcc', 'hcp', 'cd', 'hd', 'sc', 'fcc_2', 'bcc_2', 'hcp_2', 'cd_2'])

M = 200 # Number of batches during bootstrap.

# Compute 95% confidence interval using boostrap.
def bootstrap(y,y_true):
  acc_avg = sum(y==y_true)/len(y)
  acc = zeros(M)
  for m in range(M):
    new_y = choice(y,len(y))
    acc[m] = sum(new_y==y_true)/len(y)
  acc = sort(acc)
  acc = acc[int(0.025*M):int(0.975*M)]
  return 100*acc_avg, 100*(acc.max()-acc.min())/2

# Loop over lattices and temperatures.
def loop_lattice_temperature(method,lattices,lattice_to_y):
  for i in range(len(lattices)):
    T = arange(0.04,T_ml[md_lattices==lattices[i]]+0.01,0.04)
    acc_avg = zeros(len(T))
    acc_err = zeros(len(T))
    for j in range(len(T)):
      y = loadtxt('data/y/%s_%s_%.2f.dat' % (method,lattices[i],T[j]))
      acc_avg[j], acc_err[j] = bootstrap(y,lattice_to_y[lattices[i]])
    savetxt('data/accuracies/%s_%s.dat' % (method,lattices[i]), array([T,acc_avg, acc_err]).T, fmt='%.2f %.4f %.4f', header='T | accuracy | 95% confidence interval')

################################################################################
# Compute accuracies for all methods.                                          #
################################################################################

# PTM (optimized using MD data set).
if method == 'PTM':
  lattices = ['fcc', 'bcc', 'hcp', 'cd', 'hd', 'sc', 'fcc_2', 'bcc_2', 'hcp_2', 'cd_2']
  lattice_to_y = {'fcc':1, 'hcp':2, 'bcc':3, 'sc':5, 'cd':6, 'hd':7, 'fcc_2':1, 'hcp_2':2, 'bcc_2':3, 'cd_2':6}
  loop_lattice_temperature(method,lattices,lattice_to_y)

# PTM (optimized using synthetic data set).
if method == 'PTM_synthetic':
  lattices = ['fcc', 'bcc', 'hcp', 'cd', 'hd', 'sc', 'fcc_2', 'bcc_2', 'hcp_2', 'cd_2']
  lattice_to_y = {'fcc':1, 'hcp':2, 'bcc':3, 'sc':5, 'cd':6, 'hd':7, 'fcc_2':1, 'hcp_2':2, 'bcc_2':3, 'cd_2':6}
  loop_lattice_temperature(method,lattices,lattice_to_y)

# CNA
if method == 'CNA':
  lattices = ['fcc', 'bcc', 'hcp', 'cd', 'hd', 'fcc_2', 'bcc_2', 'hcp_2', 'cd_2']
  lattice_to_y = {'fcc':1, 'hcp':2, 'bcc':3, 'cd':1, 'hd':4, 'fcc_2':1, 'hcp_2':2, 'bcc_2':3, 'cd_2':1}
  loop_lattice_temperature(method,lattices,lattice_to_y)

# iCNA
if method == 'iCNA':
  lattices = ['fcc', 'bcc', 'hcp', 'fcc_2', 'bcc_2', 'hcp_2']
  lattice_to_y = {'fcc':1, 'hcp':2, 'bcc':3, 'fcc_2':1, 'hcp_2':2, 'bcc_2':3}
  loop_lattice_temperature(method,lattices,lattice_to_y)

# AJA
if method == 'AJA':
  lattices = ['fcc', 'bcc', 'hcp', 'fcc_2', 'bcc_2', 'hcp_2']
  lattice_to_y = {'fcc':1, 'hcp':2, 'bcc':3, 'fcc_2':1, 'hcp_2':2, 'bcc_2':3}
  loop_lattice_temperature(method,lattices,lattice_to_y)
     
# VoroTop (ignoring the counting the FCC/HCP as correct: 50/50 split).
if method == 'VTM':
  lattices = ['fcc', 'bcc', 'hcp', 'fcc_2', 'bcc_2', 'hcp_2']
  lattice_to_y = {'fcc':1, 'hcp':5, 'bcc':2, 'fcc_2':1, 'hcp_2':5, 'bcc_2':2}
  loop_lattice_temperature(method,lattices,lattice_to_y)

# Chil+
if method == 'CPA':
  lattices = ['cd', 'hd', 'cd_2']
  lattice_to_y = {'cd':2, 'hd':1, 'cd_2':2}
  loop_lattice_temperature(method,lattices,lattice_to_y)

################################################################################
