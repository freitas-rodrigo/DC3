#!/bin/bash
#SBATCH --account=sua183
#SBATCH --partition=shared
#SBATCH --output=data/logs/job_out_VAR_Th.log
#SBATCH --error=data/logs/job_err_VAR_Th.log
#SBATCH --job-name=fcc_VAR_Th
#SBATCH --ntasks-per-node=1
#SBATCH --nodes=1
#SBATCH --time=00:30:00

# Load required modules for running LAMMPS in parallel.
module --force purge
ml load cpu slurm gcc openmpi

# Define aliases.
lammps="${HOME}/dc3/lammps/src/lmp_mpi"
potdir="${HOME}/dc3/potentials"

# Run job.
date
srun  ${lammps} -in in.lmp \
                -log data/logs/lammps_VAR_Th.log \
                -screen none \
                -var potdir ${potdir} \
                -var RANDOM ${RANDOM} \
                -var Th VAR_Th
date
