#!/bin/bash
#SBATCH --account=sua182
#SBATCH --partition=shared
#SBATCH --output=data/logs/job_out_md_VAR_n.log
#SBATCH --error=data/logs/job_err_md_VAR_n.log
#SBATCH --job-name=X_md_VAR_n
#SBATCH --ntasks-per-node=100
#SBATCH --nodes=1
#SBATCH --time=00:10:00

# Input parameters.
T=$(echo VAR_n*0.04 | bc | sed 's/^\./0./')
lattices="fcc bcc hcp cd hd sc fcc_2 bcc_2 hcp_2 cd_2"

# Loop over lattices and timestamps for selected temperature.
date
nlattice=01 # Counter for lattice number
for lattice in ${lattices}
do
  md_dir="../../md/${nlattice}_${lattice}/data/dump"
  for step in `seq 10000 10000 100000`
  do
    in_dir="${md_dir}/dump_${T}_${step}.gz"
    out_dir="data/md/"
    fname="${lattice}_${T}_${step}"
    python3 compute.py ${in_dir} ${out_dir} ${fname} True True &
  done
  nlattice=$(echo ${nlattice}+1 | bc | sed -e :a -e 's/^.\{1,1\}$/0&/;ta')
done
wait
date
