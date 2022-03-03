#!/bin/bash
#SBATCH --account=sua182
#SBATCH --partition=compute
#SBATCH --output=data/job_out.log
#SBATCH --error=data/job_err.log
#SBATCH --job-name=evaluate_model
#SBATCH --ntasks-per-node=128
#SBATCH --nodes=1
#SBATCH --time=01:00:00

date
python3 01_build_classifier.py

for system in "md_crystal" "md_liquid"
do
  python3 02_compute_scores.py ${system} &
done
wait
date
