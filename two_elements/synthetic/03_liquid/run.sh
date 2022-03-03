#!/bin/bash

lammps="${HOME}/dc3/lammps/src/lmp_serial"
potdir="${HOME}/dc3/potentials"

for n in `seq 1 10`
do
  ${lammps} -in in.lmp \
            -log none \
            -var potdir ${potdir} \
            -var RANDOM ${RANDOM} \
            -var n ${n}
done
