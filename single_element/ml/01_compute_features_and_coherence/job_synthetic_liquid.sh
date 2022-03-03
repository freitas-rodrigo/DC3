#!/bin/bash
#SBATCH --account=sua183
#SBATCH --partition=shared
#SBATCH --output=data/logs/job_out_synthetic_liquid.log
#SBATCH --error=data/logs/job_err_synthetic_liquid.log
#SBATCH --job-name=X_synthetic_liquid
#SBATCH --ntasks-per-node=10
#SBATCH --nodes=1
#SBATCH --time=00:10:00

# Input parameters.
T=1.60

# Loop over snapshots.
date
for m in `seq 1 10`
do
  in_dir="../../synthetic/03_liquid/data/dump_${m}.gz"
  out_dir="data/synthetic_liquid/"
  fname="${m}"
  python3 compute.py ${in_dir} ${out_dir} ${fname} False True &
done
wait
date
