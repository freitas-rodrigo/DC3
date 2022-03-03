from numpy import *
from scipy.linalg import norm
from scipy.special import sph_harm
from ovito.data import NearestNeighborFinder, CutoffNeighborFinder

# Compute Steinhardt order-parameter for all atoms in data.
def compute_sop(data,l,N_neigh):
  natoms = data.particles.count # Number of atoms.
  sop = zeros((natoms,len(l)))
  finder = NearestNeighborFinder(N_neigh,data) # Computes atom neighbor lists.
  # Loop over atoms to compute Steinhardt order paramter.
  for iatom in range(natoms):
    # Unroll neighbor distances.
    r = zeros((N_neigh,3),dtype=float64) # Distance vector to neighbors.
    ineigh = 0 # Neighbor counter.  
    for neigh in finder.find(iatom):
      r[ineigh][:] = neigh.delta
      ineigh += 1
    # Compute Steinhardt for current atom.
    sop[iatom] = steinhardt(r,l)
  return sop

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

# Compute Steinhardt parameter for all orders in l using coordinates in r.
def steinhardt(r,l):
  Q = zeros(len(l))
  for i in range(len(l)):
    q = zeros(2*l[i]+1,dtype=complex128)
    for v in r:
      phi = arctan2(v[1],v[0])
      theta = arccos(v[2]/norm(v))
      q += sph_harm(arange(-l[i],l[i]+1),l[i],phi,theta)
    q /= r.shape[0]
    Q[i] = sqrt(real((4*pi/(2*l[i]+1)) * sum(q*conjugate(q))))
  return Q

# Radial symmetry function given distance d.
def G(x, mu, sigma):
  return exp(-(x-mu)**2/(2*sigma**2))
