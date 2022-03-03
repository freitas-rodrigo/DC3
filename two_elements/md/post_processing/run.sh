#!/bin/bash

n_lattices=6
lattices=(L1_0 L1_2 B2 zincblende rocksalt wurtzite)

rm data/* data*/*

# Compute thermodynamic averages.
for n in `seq 1 ${n_lattices}`
do
  python3 01_compute_averages.py ${n} ${lattices[$(echo ${n}-1|bc)]} &
done
wait

# Compute crystal structure metastability limit temperature.
python3 02_compute_metastability_limit.py

# Plot time evolution of thermodynamic properties.
for n in `seq 1 ${n_lattices}`
do
  python3 03_plot_time_evolution.py ${n} ${lattices[$(echo ${n}-1|bc)]} &
done
wait

# Plot average thermodynamic properties vs temperature.
for n in `seq 1 ${n_lattices}`
do
  python3 04_plot_averages.py ${n} ${lattices[$(echo ${n}-1|bc)]} &
done
wait

# Collect dump files to verify metastability prediction.
SCRATCH='/expanse/lustre/projects/sua182/freitas'
cd `pwd | sed -e "s@${HOME}@${SCRATCH}@"`

for n in `seq 1 ${n_lattices}`
do
  lattice=${lattices[$(echo ${n}-1|bc)]} 
  n=$(echo $n | sed -e :a -e 's/^.\{1,1\}$/0&/;ta')

  cd dump
  mkdir -p ${lattice}

  cd ../../${n}_${lattice}/dump
  for file in dump_1.??_relaxed.gz
  do
    cp $file ../../post_processing/dump/${lattice}/${file}
  done
  cd ../../post_processing
done
