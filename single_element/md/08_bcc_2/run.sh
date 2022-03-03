#!/bin/bash

for m in `seq 2 1 40`
do
  # Homologous temperature.
  Th=$(python <<< "print('%.2f' % (0.04*${m}))")

  # Create job submission script.
  cmd=`sed dummy_job.sh -e "s/VAR_Th/${Th}/"`

  # Run job and clean.
  printf "$cmd" > __job.sh
  sbatch __job.sh
  rm __job.sh
  printf "Th = ${Th}\n"
done

