#!/bin/bash
#SBATCH --account=sua183
#SBATCH --partition=shared
#SBATCH --output=data/logs/job_out_synthetic_crystal_VAR_LATT.log
#SBATCH --error=data/logs/job_err_synthetic_crystal_VAR_LATT.log
#SBATCH --job-name=X_synthetic_crystal_VAR_LATT
#SBATCH --ntasks-per-node=40
#SBATCH --nodes=1
#SBATCH --time=00:10:00

# Input information.
synthetic_dir="../../synthetic/02_crystal/data"
lattice=VAR_LATT

# Number of simulation cells created for this lattice.
M=`cat "${synthetic_dir}/n_cells_created.dat"`

# Run job.
date
for m in `seq 0 $(echo ${M}-1 | bc)`
do
  in_dir="${synthetic_dir}/dump/dump_${lattice}_${m}.gz"
  out_dir="data/synthetic_crystal/"
  fname="${lattice}_${m}"
  python3 compute.py ${in_dir} ${out_dir} ${fname} True True &
done
wait
date
