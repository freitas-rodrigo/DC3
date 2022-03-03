#!/bin/bash
#SBATCH --account=sua182
#SBATCH --partition=shared
#SBATCH --output=../data/logs/job_out_synthetic_crystal.log
#SBATCH --error=../data/logs/job_err_synthetic_crystal.log
#SBATCH --job-name=order_synthetic_crystal
#SBATCH --ntasks-per-node=100
#SBATCH --nodes=1
#SBATCH --time=05:00:00

date
for i in `seq 0 5`
do
  python3 01_cat_steps.py ${i} &
done
wait

python3 02_cat_lattices.py
date
