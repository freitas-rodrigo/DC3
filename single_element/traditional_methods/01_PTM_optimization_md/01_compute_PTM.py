from numpy import *
from ovito.io import *
from ovito.modifiers import *

################################################################################
# Setup.                                                                       #
################################################################################

lattices = ['fcc', 'bcc', 'hcp', 'cd', 'hd', 'sc', 'fcc_2', 'bcc_2', 'hcp_2', 'cd_2']
steps = arange(10000,100000+1,10000) # MD step range.

################################################################################
# Compute RMSD and predicted label for each material.                          #
################################################################################

# Loop over temperatures (one for melting point and another for liquid phase).
for T in [1.00,1.60]:
  for n in range(len(lattices)):
    for step in steps:
      # Perform PTM analysis.
      pipeline = import_file('../../md/%02d_%s/data/dump/dump_%.2f_%d.gz' % (n+1,lattices[n],T,step))
      PTM = PolyhedralTemplateMatchingModifier()
      PTM.structures[PTM.Type.CUBIC_DIAMOND].enabled = True
      PTM.structures[PTM.Type.HEX_DIAMOND].enabled = True
      PTM.structures[PTM.Type.SC].enabled = True
      PTM.rmsd_cutoff = 0
      PTM.output_rmsd = True
      pipeline.modifiers.append(PTM)
      data = pipeline.compute()
      RMSD_tmp = data.particles['RMSD']
      y_tmp = data.particles['Structure Type']
      # Accumulate RMSD and predicted labels.
      if 'RMSD' in locals():
        RMSD = concatenate([RMSD,RMSD_tmp])
        y = concatenate([y,y_tmp])
      else:
        RMSD = RMSD_tmp
        y = y_tmp
    # Save data and clean memory.
    if T == 1.60:
      sulfix = '_liquid'
    else:
      sulfix = ''
    savetxt('data/RMSD/RMSD_%s.dat' % (lattices[n]+sulfix), RMSD, fmt='%.10e')
    savetxt('data/y/y_%s.dat' % (lattices[n]+sulfix), y, fmt='%d')
    del RMSD, y

################################################################################
