#!/bin/bash
#SBATCH --account=sua182
#SBATCH --partition=shared
#SBATCH --output=data/job_out.log
#SBATCH --error=data/job_err.log
#SBATCH --job-name=crystal_accuracy
#SBATCH --ntasks-per-node=100
#SBATCH --nodes=1
#SBATCH --time=00:10:00

date
for n in `seq 1 40`
do
  T=$(echo $n*0.04 | bc | sed 's/^\./0./')
  python3 01_compute_predictions.py ${T} &
done
wait

for method in 'PTM' 'PTM_synthetic' 'iCNA' 'CNA' 'AJA' 'VTM' 'CPA'
do
  python3 02_compute_accuracies.py ${method} &
done
wait

date
