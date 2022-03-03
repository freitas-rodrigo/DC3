#!/bin/bash

lammps="${HOME}/dc3/lammps/src/lmp_serial"

for lattice in 'fcc' 'bcc' 'hcp' 'cd' 'hd' 'sc'
do
  ${lammps} -in in_${lattice}.lmp -log none
done
