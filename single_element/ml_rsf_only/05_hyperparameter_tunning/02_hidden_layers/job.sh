#!/bin/bash

# Loop over number of hidden layers.
for n in 1 2 3 4 5
do
    cmd=`sed dummy_job.sh -e "s/VAR_N/${n}/"`
    printf "$cmd" > __job.sh
    sbatch __job.sh
    rm __job.sh
done
