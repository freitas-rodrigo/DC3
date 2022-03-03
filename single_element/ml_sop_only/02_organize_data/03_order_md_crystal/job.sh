#!/bin/bash
#SBATCH --account=sua183
#SBATCH --partition=shared
#SBATCH --output=../data/logs/job_out_md_crystal.log
#SBATCH --error=../data/logs/job_err_md_crystal.log
#SBATCH --job-name=order_md_crystal
#SBATCH --ntasks-per-node=100
#SBATCH --nodes=1
#SBATCH --time=05:00:00

date
for ilatt in `seq 0 9`
do
  python3 01_cat_steps.py ${ilatt} &
done
wait

for ilatt in `seq 0 9`
do
  python3 02_cat_temperatures.py ${ilatt} &
done
wait

python3 03_cat_lattices.py
date
