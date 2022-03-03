from numpy import *
import sys

n = int(sys.argv[1]) # Lattice directory number.
lattice = sys.argv[2] # Lattice name.
T = arange(0.04,1.61,0.04) # Temperature range.
t0 = 100 # Equilibration period [0.1ps].

a_mean = zeros(len(T))
pe_mean = zeros(len(T))
for i in range(len(T)):
  step, a, pe = loadtxt('../%02d_%s/data/thermo/thermo_%.2f.dat' % (n,lattice,T[i]), unpack=True)
  if len(a) == 1002: # This is only here because SNAP InP liquid is not stable.
    a_mean[i] = a[t0:].mean()
    pe_mean[i] = pe[t0:].mean()
  else:
    a_mean = a_mean[:i]
    pe_mean = pe_mean[:i]
    T = T[:i]
    break

savetxt('data/averages/%s.dat' % lattice, column_stack((T,a_mean,pe_mean)), header=' T | lattice_parameter [A] | potential_energy [eV/atom]', fmt='%.2f %.8f %.8f')

