#!/bin/bash
#SBATCH --account=sua183
#SBATCH --partition=shared
#SBATCH --output=data/job_out.log
#SBATCH --error=data/job_err.log
#SBATCH --job-name=compute_distances
#SBATCH --ntasks-per-node=10
#SBATCH --nodes=1
#SBATCH --time=01:00:00

date
python3 compute.py
date
