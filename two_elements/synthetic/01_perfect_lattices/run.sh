#!/bin/bash

lammps="${HOME}/dc3/lammps/src/lmp_serial"
potdir="${HOME}/dc3/potentials"

for lattice in 'L1_0' 'L1_2' 'B2' 'zincblende' 'rocksalt' 'wurtzite'
do
  ${lammps} -in in_${lattice}.lmp \
            -log none \
            -var potdir ${potdir}
done
