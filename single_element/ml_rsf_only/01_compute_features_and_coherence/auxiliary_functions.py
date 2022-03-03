from numpy import *
from scipy.linalg import norm
from scipy.special import sph_harm
from ovito.data import NearestNeighborFinder, CutoffNeighborFinder

# Compute radial symmetry functions for all atoms in data.
def compute_rsf(data,f_mu,f_sigma,N_neigh):
  natoms = data.particles.count # Number of atoms.
  N_rsf = len(f_mu) # Number of rsf parameters.
  rsf = zeros((natoms,N_rsf)) # rsf function for each atom.

  # Loop over atoms to compute mu.
  mu = zeros(natoms) # Mean distance of N_neigh first neighbors.
  finder = NearestNeighborFinder(N_neigh,data) # Computes atom neighbor lists.
  for iatom in range(natoms):
    # Compute neighbor distances.
    r = zeros(N_neigh,dtype=float64) # Distance to neighbors.
    ineigh = 0 # Neighbor counter.
    for neigh in finder.find(iatom):
      r[ineigh] = neigh.distance
      ineigh += 1
    mu[iatom] = r.mean()

  # Loop over atoms to compute rsfs.
  r_cut = max(mu)*(1+4*f_sigma)
  finder = CutoffNeighborFinder(r_cut,data)
  for iatom in range(natoms):
    # Compute total number of neighbors within cutoff.
    N_neigh = 0
    for neigh in finder.find(iatom):
      N_neigh += 1
    # Find neighbor distances.
    r = zeros(N_neigh,dtype=float64) # Distance to neighbors.
    ineigh = 0 # Neighbor counter.
    for neigh in finder.find(iatom):
      r[ineigh] = neigh.distance
      ineigh += 1
    # Compute RSF.
    for i in range(N_rsf):
      rsf[iatom,i] = sum(G(r,f_mu[i]*mu[iatom],f_sigma*mu[iatom]))
  return rsf

# Compute coherence factor for all atoms in data.
def compute_cf(data,l,N_neigh):
  natoms = data.particles.count # Number of atoms.
  cf = zeros(natoms) # Coherence factor.
  finder = NearestNeighborFinder(N_neigh,data) # Computes atom neighbor lists.
  # Compute q_lm.
  q = zeros((natoms,sum(2*l+1)), dtype=complex) # Steinhardt vector.
  for iatom in range(natoms):
    for neigh in finder.find(iatom):
      phi = arctan2(neigh.delta[1],neigh.delta[0])
      theta = arccos(neigh.delta[2]/neigh.distance)
      Nl = 0
      for i in range(len(l)):
        q[iatom,Nl:Nl+2*l[i]+1] += sph_harm(range(-l[i],l[i]+1),l[i],phi,theta)
        Nl += 2*l[i]+1
    q[iatom] /= N_neigh
  # Compute dot product of q_lm vectors.
  for iatom in range(natoms):
    for neigh in finder.find(iatom):
      v = q[iatom] / norm(q[iatom])
      u = q[neigh.index] / norm(q[neigh.index])
      cf[iatom] += dot(v,conjugate(u)).real # Imaginary part = 0, always.
    cf[iatom] /= N_neigh
  return cf

# Radial symmetry function given distance d.
def G(x, mu, sigma):
  return exp(-(x-mu)**2/(2*sigma**2))
