#!/bin/bash
#SBATCH --account=sua182
#SBATCH --partition=compute
#SBATCH --output=data/job_out.log
#SBATCH --error=data/job_err.log
#SBATCH --job-name=viz
#SBATCH --ntasks-per-node=128
#SBATCH --nodes=1
#SBATCH --time=01:00:00

date
python3 01_compute_PCA.py
for perplexity in 5 10 25 50 100 200 500 1000
do
  python3 02_compute_tSNE.py ${perplexity} &
  python3 03_compute_tSNE_T_dependence.py ${perplexity} &
done
wait
date
