from numpy import *
from numpy.random import *
from ovito.io import import_file, export_file
from ovito.data import NearestNeighborFinder

lattices = ['L1_0', 'L1_2', 'B2', 'zincblende', 'rocksalt', 'wurtzite']

# Define range of displacements as a fraction of nearest neighbor distance.
n_alpha = 40
alpha_range = linspace(0.01,0.25,n_alpha)
with open('data/n_cells_created.dat','w') as f: 
  f.write('%d' % n_alpha)

for lattice in lattices:
  # Load snapshot.
  pipeline = import_file('../01_perfect_lattices/data/dump_%s.gz' % lattice)
  data = pipeline.compute()

  # Find nearest-neighbor distance of perfect lattice.
  for neigh in NearestNeighborFinder(1,data).find(0):
    d = neigh.distance

  # Create random displacement and save data.
  natoms = data.particles.count
  for n,alpha in enumerate(alpha_range):
    data_tmp = data.clone()
    # Sample displacements uniformly inside a sphere.
    phi = 2*pi*random(natoms)
    theta = arccos(-1 + 2*random(natoms))
    R = alpha * d * cbrt(random(natoms))
    r = zeros((natoms,3))
    r[:,0] = R * sin(theta) * cos(phi)
    r[:,1] = R * sin(theta) * sin(phi)
    r[:,2] = R * cos(theta)
    data_tmp.particles_.positions_ += r
    # Save configuration.
    export_file(data_tmp, "data/dump/dump_%s_%d.gz" % (lattice,n), "lammps/dump", columns = ["Particle Identifier", "Particle Type", "Position.X", "Position.Y", "Position.Z"])
