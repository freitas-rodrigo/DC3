from numpy import *
from numpy.random import choice
import sys

################################################################################
# Load and process data.                                                       #
################################################################################

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
def liquid_accuracy(method,lattices):
  for i in range(len(lattices)):
    if i == 0:
      y = loadtxt('data/y/%s_%s_1.60.dat' % (method,lattices[i]))
    else:
      y = concatenate((y,loadtxt('data/y/%s_%s_1.60.dat' % (method,lattices[i]))))
  acc_avg, acc_err = bootstrap(y,0)
  return acc_avg, acc_err

################################################################################
# Compute accuracies for all methods.                                          #
################################################################################

with open('data/accuracies/liquid.dat', 'w') as f:
  f.write('# method | accuracy | 95% confidence interval\n')
  # PTM (optimized using MD data set).
  lattices = ['fcc', 'bcc', 'hcp', 'cd', 'hd', 'sc', 'fcc_2', 'bcc_2', 'hcp_2', 'cd_2']
  f.write(' PTM %.2f %.2f\n' % (liquid_accuracy('PTM',lattices)))

  # PTM (optimized using synthetic data set).
  lattices = ['fcc', 'bcc', 'hcp', 'cd', 'hd', 'sc', 'fcc_2', 'bcc_2', 'hcp_2', 'cd_2']
  f.write(' PTM_synthetic %.2f %.2f\n' % (liquid_accuracy('PTM_synthetic',lattices)))
  
  # CNA
  lattices = ['fcc', 'bcc', 'hcp', 'cd', 'hd', 'fcc_2', 'bcc_2', 'hcp_2', 'cd_2']
  liquid_accuracy('CNA',lattices)
  f.write(' CNA %.2f %.2f\n' % (liquid_accuracy('CNA',lattices)))
  
  # iCNA
  lattices = ['fcc', 'bcc', 'hcp', 'fcc_2', 'bcc_2', 'hcp_2']
  liquid_accuracy('iCNA',lattices)
  f.write('iCNA %.2f %.2f\n' % (liquid_accuracy('iCNA',lattices)))
  
  # AJA
  lattices = ['fcc', 'bcc', 'hcp', 'fcc_2', 'bcc_2', 'hcp_2']
  liquid_accuracy('AJA',lattices)
  f.write(' AJA %.2f %.2f\n' % (liquid_accuracy('AJA',lattices)))
       
  # VoroTop (ignoring the counting the FCC/HCP as correct: 50/50 split).
  lattices = ['fcc', 'bcc', 'hcp', 'fcc_2', 'bcc_2', 'hcp_2']
  liquid_accuracy('VTM',lattices)
  f.write(' VTM %.2f %.2f\n' % (liquid_accuracy('VTM',lattices)))
  
  # Chil+
  lattices = ['cd', 'hd', 'cd_2']
  liquid_accuracy('CPA',lattices)
  f.write(' CPA %.2f %.2f\n' % (liquid_accuracy('CPA',lattices)))

################################################################################
