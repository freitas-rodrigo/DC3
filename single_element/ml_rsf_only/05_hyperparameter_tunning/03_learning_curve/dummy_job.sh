#!/bin/bash
#SBATCH --account=sua183
#SBATCH --partition=shared
#SBATCH --output=../data/logs/job_out_learning_curve_VAR_N.log
#SBATCH --error=../data/logs/job_err_learning_curve_VAR_N.log
#SBATCH --job-name=learning_curve_VAR_N
#SBATCH --ntasks-per-node=20
#SBATCH --nodes=1
#SBATCH --time=01:00:00

date
python3 compute.py VAR_N
date
