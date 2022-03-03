from numpy import *
from ovito.io import import_file
from auxiliary_functions import compute_sop, compute_cf
import sys

# Input parameters.
in_dir = sys.argv[1] # Input directory.
out_dir = sys.argv[2] # Output directory.
fname = sys.argv[3] # File name.
feature_flag = sys.argv[4] # Flag to compute features.
coherence_flag = sys.argv[5] # Flag to compute features.

# Load simulation snapshot.
pipeline = import_file(in_dir)
data = pipeline.compute()

################################################################################
# Compute features.                                                            #
################################################################################

if feature_flag == 'True':
  # Input parameters for feature calculation.
  l = arange(1,15+1) # Range of spherical harmonics orders.
  
  # Compute Steinhardt.
  for Nneigh in range(2,16+1):
    if 'X' in locals():
      X = column_stack((X,compute_sop(data,l,Nneigh)))
    else:
      X = compute_sop(data,l,Nneigh)
  
  # Save concatenated features.
  savetxt(out_dir+'X_'+fname+'.dat', X, fmt='%.8e', 
          header='one example with %d features per row' % X.shape[1])

################################################################################
# Compute coherence factor.                                                   #
################################################################################

if coherence_flag == 'True':
  # Input parameters for coherence-factor calculation.
  l = array([4,6,8,12]) # Range of spherical harmonic orders.
  Nneigh = 16 # Number of neighbors used to compute coherence factor.
  
  # Compute and save coherence factor.
  alpha = compute_cf(data,l,Nneigh)
  savetxt(out_dir+"alpha_"+fname+'.dat', alpha, fmt='%.6f')

################################################################################
