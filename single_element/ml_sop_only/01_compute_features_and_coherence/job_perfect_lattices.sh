#!/bin/bash
#SBATCH --account=sua183
#SBATCH --partition=shared
#SBATCH --output=data/logs/job_out_perfect_lattices.log
#SBATCH --error=data/logs/job_err_perfect_lattices.log
#SBATCH --job-name=X_perfect_lattices
#SBATCH --ntasks-per-node=6
#SBATCH --nodes=1
#SBATCH --time=00:10:00

# Loop over all lattices.
lattices="fcc bcc hcp cd hd sc"
date
for lattice in ${lattices}
do
  in_dir="../../synthetic/01_perfect_lattices/data/dump_${lattice}.gz"
  out_dir="data/perfect_lattices/"
  fname="${lattice}"
  python3 compute.py ${in_dir} ${out_dir} ${fname} True False &
done
wait
date
