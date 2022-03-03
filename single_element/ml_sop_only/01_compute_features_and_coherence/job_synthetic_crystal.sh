#!/bin/bash

lattices="fcc bcc hcp cd hd sc"

for lattice in ${lattices}
do
  # Create job submission script.
  cmd=`sed dummy_job_synthetic_crystal.sh -e "s/VAR_LATT/${lattice}/"`

  # Run job and clean.
  printf "$cmd" > __job.sh
  sbatch __job.sh
  rm __job.sh
done
