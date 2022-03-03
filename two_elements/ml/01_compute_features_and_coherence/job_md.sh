#!/bin/bash

# Loop over temperature range.
for n in `seq 1 40`
do
  # Create job submission script, submit it, and clean.
  cmd=`sed dummy_job_md.sh -e "s/VAR_n/${n}/"`
  printf "$cmd" > __job.sh
  sbatch __job.sh
  rm __job.sh
done
