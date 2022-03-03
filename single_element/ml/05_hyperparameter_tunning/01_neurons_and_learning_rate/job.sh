#!/bin/bash

# Loop over number of neurons and learning rate.
for i in `seq 0 4`
do
  for j in `seq 0 4`
  do
    # Create job submission script, submit it, and clean.
    cmd=`sed dummy_job.sh -e "s/VAR_I/${i}/" -e "s/VAR_J/${j}/"`
    printf "$cmd" > __job.sh
    sbatch __job.sh
    rm __job.sh
  done
done
