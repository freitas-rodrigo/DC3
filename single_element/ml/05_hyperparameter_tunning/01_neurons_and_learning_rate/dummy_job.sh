#!/bin/bash
#SBATCH --account=sua183
#SBATCH --partition=shared
#SBATCH --output=../data/logs/job_out_neurons_VAR_I_VAR_J.log
#SBATCH --error=../data/logs/job_err_neurons_VAR_I_VAR_J.log
#SBATCH --job-name=VAR_I_VAR_J
#SBATCH --ntasks-per-node=20
#SBATCH --nodes=1
#SBATCH --time=01:00:00

date
python3 compute.py VAR_I VAR_J
date
