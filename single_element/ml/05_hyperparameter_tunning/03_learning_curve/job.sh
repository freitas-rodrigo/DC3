#!/bin/bash

# Loop over training set size.
for n in 1 2 3 4 5 6 7 8 9 10
do
    cmd=`sed dummy_job.sh -e "s/VAR_N/${n}/"`
    printf "$cmd" > __job.sh
    sbatch __job.sh
    rm __job.sh
done
