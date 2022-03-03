#!/bin/bash

lattices="L1_0 L1_2 B2 zincblende rocksalt wurtzite"

for lattice in ${lattices}
do
  # Create job submission script.
  cmd=`sed dummy_job_synthetic_crystal.sh -e "s/VAR_LATT/${lattice}/"`

  # Run job and clean.
  printf "$cmd" > __job.sh
  sbatch __job.sh
  rm __job.sh
done
