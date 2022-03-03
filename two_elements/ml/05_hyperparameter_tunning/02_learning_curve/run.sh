#!/bin/bash

lattices="fcc bcc hcp cd hd sc"
for lattice in ${lattices}
do
  python3 compute.py ${lattice}
done
