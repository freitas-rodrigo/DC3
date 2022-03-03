from numpy import *
from scipy.linalg import norm
import joblib

from read_functions import read
from constants import y_lattices

# Data-Centric Classifier (DC3).
# For each example in X this function returns the predicted label.
def dc3(X,alpha):
  # Load coherence factor cutoff. 
  alpha_cut = read('../02_organize_data/data/post_processed/alpha_cutoff.dat')
  # Load neural network.
  NN = joblib.load('../06_evaluate_model/data/neural_network.pkl')
  # Load cutoff distance to perfect lattices.
  d_cut = read('../03_compute_distances/data/post_processed/distance_cutoff_vs_lattice.dat')
  y = NN.predict(X) # Load neural-network prediction.
  d = compute_distance(X,y) # Compute distance vector to ideal lattice points.

  # DC3 logics.
  for n in range(len(alpha)):
    if alpha[n] >= alpha_cut: # If crystalline.
      if d[n] <= d_cut[y_lattices==y[n]]: # Distance to predicted lattice
        continue # NN label is correct: known crystal.
      else:
        y[n] = -1 # Unknown crystal.
        continue 
    else:
      y[n] = 0 # Liquid or amorphous.
  return y # Return predicted labels.

# Compute distance from all examples in X to their ideal lattices.
def compute_distance(X,y):
  X0 = read('../02_organize_data/data/perfect_lattices/X.dat')
  d = zeros(len(y))
  for i in range(len(y_lattices)):
    mask = (y==y_lattices[i])
    d[mask] = norm(X[mask]-X0[i],axis=1)
  return d
