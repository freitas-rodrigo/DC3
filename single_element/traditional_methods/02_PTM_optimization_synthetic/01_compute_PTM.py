from numpy import *
from ovito.io import *
from ovito.modifiers import *

################################################################################
# Setup.                                                                       #
################################################################################

lattices = ['fcc', 'bcc', 'hcp', 'cd', 'hd', 'sc']
M_crystal = 40 # Number of independent data sets for crystal structures.
M_liquid = 10 # Number of independent data sets for liquid.

################################################################################
# Compute RMSD and predicted label for each crystal structure.                 #
################################################################################

for n in range(len(lattices)):
  for m in range(M_crystal):
    print(m)
    # Perform PTM analysis.
    pipeline = import_file('../../synthetic/02_crystal/data/dump/dump_%s_%d.gz' % (lattices[n],m))
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
  savetxt('data/RMSD/RMSD_%s.dat' % lattices[n], RMSD, fmt='%.10e')
  savetxt('data/y/y_%s.dat' % lattices[n], y, fmt='%d')
  del RMSD, y

################################################################################
# Compute RMSD and predicted label for liquid.                                 #
################################################################################

# Loop over temperatures (one for melting point and another for liquid phase).
for m in range(1,M_liquid+1):
  # Perform PTM analysis.
  pipeline = import_file('../../synthetic/03_liquid/data/dump_%d.gz' % m)
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
savetxt('data/RMSD/RMSD_liquid.dat', RMSD, fmt='%.10e')
savetxt('data/y/y_liquid.dat', y, fmt='%d')
del RMSD, y

################################################################################
