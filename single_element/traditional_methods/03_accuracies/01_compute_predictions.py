from numpy import *
from ovito.io import *
from ovito.modifiers import *
import sys

################################################################################
# Setup.                                                                       #
################################################################################

T = float(sys.argv[1]) # Snapshot temperature.

dirs = ["01_fcc", "02_bcc", "03_hcp", "04_cd", "05_hd", "06_sc", "07_fcc_2", "08_bcc_2", "09_hcp_2", "10_cd_2"]
md_dir = '../../md/%s/data/dump/dump_%.2f_%d.gz'
steps = arange(10000,100000+1,10000) # MD snapshots range.
CP_cutoff = [0,0,0,2.9,3.5,0,0,0,0,2.9] # Cutoff for Chil+.

################################################################################
# Compute PTM prediction: optimized using MD data set.                         #
################################################################################

RMSD_cutoff = loadtxt('../01_PTM_optimization_md/data/RMSD_cutoff.dat')
for i in range(len(dirs)):
  for step in steps:
    pipeline = import_file(md_dir % (dirs[i],T,step))
    PTM = PolyhedralTemplateMatchingModifier()
    PTM.structures[PTM.Type.CUBIC_DIAMOND].enabled = True
    PTM.structures[PTM.Type.HEX_DIAMOND].enabled = True
    PTM.structures[PTM.Type.SC].enabled = True
    PTM.rmsd_cutoff = RMSD_cutoff[i]
    pipeline.modifiers.append(PTM)
    data = pipeline.compute()
    if 'y' in locals():
      y = concatenate((y,array(data.particles['Structure Type'])))
    else:
      y = array(data.particles['Structure Type'])
  savetxt('data/y/PTM_%s_%.2f.dat' % (dirs[i][3:],T), y, fmt='%d')
  del y

################################################################################
# Compute PTM prediction: optimized using synthetic data set.                  #
################################################################################

RMSD_cutoff = loadtxt('../02_PTM_optimization_synthetic/data/RMSD_cutoff.dat')
RMSD_cutoff = concatenate((RMSD_cutoff,RMSD_cutoff[:4]))
for i in range(len(dirs)):
  for step in steps:
    pipeline = import_file(md_dir % (dirs[i],T,step))
    PTM = PolyhedralTemplateMatchingModifier()
    PTM.structures[PTM.Type.CUBIC_DIAMOND].enabled = True
    PTM.structures[PTM.Type.HEX_DIAMOND].enabled = True
    PTM.structures[PTM.Type.SC].enabled = True
    PTM.rmsd_cutoff = RMSD_cutoff[i]
    pipeline.modifiers.append(PTM)
    data = pipeline.compute()
    if 'y' in locals():
      y = concatenate((y,array(data.particles['Structure Type'])))
    else:
      y = array(data.particles['Structure Type'])
  savetxt('data/y/PTM_synthetic_%s_%.2f.dat' % (dirs[i][3:],T), y, fmt='%d')
  del y

################################################################################
# Compute CNA prediction.                                                      #
################################################################################

for i in range(len(dirs)):
  if dirs[i][3:5] == 'cd' or dirs[i][3:5] == 'hd': continue
  for step in steps:
    pipeline = import_file(md_dir % (dirs[i],T,step))
    CNA = CommonNeighborAnalysisModifier()
    CNA.structures[CommonNeighborAnalysisModifier.Type.ICO].enabled = False
    pipeline.modifiers.append(CNA)
    data = pipeline.compute()
    if 'y' in locals():
      y = concatenate((y,array(data.particles['Structure Type'])))
    else:
      y = array(data.particles['Structure Type'])
  savetxt('data/y/CNA_%s_%.2f.dat' % (dirs[i][3:],T), y, fmt='%d')
  del y

################################################################################
# Compute modified CNA.                                                        #
################################################################################

for i in range(len(dirs)):
  if dirs[i][3:5] != 'cd' and dirs[i][3:5] != 'hd': continue
  for step in steps:
    pipeline = import_file(md_dir % (dirs[i],T,step))
    CNA = IdentifyDiamondModifier()
    CNA.structures[CNA.Type.CUBIC_DIAMOND_FIRST_NEIGHBOR].enabled = False
    CNA.structures[CNA.Type.CUBIC_DIAMOND_SECOND_NEIGHBOR].enabled = False
    CNA.structures[CNA.Type.HEX_DIAMOND_FIRST_NEIGHBOR].enabled = False
    CNA.structures[CNA.Type.HEX_DIAMOND_SECOND_NEIGHBOR].enabled = False
    pipeline.modifiers.append(CNA)
    data = pipeline.compute()
    if 'y' in locals():
      y = concatenate((y,array(data.particles['Structure Type'])))
    else:
      y = array(data.particles['Structure Type'])
  savetxt('data/y/CNA_%s_%.2f.dat' % (dirs[i][3:],T), y, fmt='%d')
  del y

################################################################################
# Compute iCNA prediction.                                                     #
################################################################################

for i in range(len(dirs)):
  for step in steps:
    pipeline = import_file(md_dir % (dirs[i],T,step))
    CNA = CommonNeighborAnalysisModifier(mode=CommonNeighborAnalysisModifier.Mode.IntervalCutoff)
    CNA.structures[CommonNeighborAnalysisModifier.Type.ICO].enabled = False
    pipeline.modifiers.append(CNA)
    data = pipeline.compute()
    if 'y' in locals():
      y = concatenate((y,array(data.particles['Structure Type'])))
    else:
      y = array(data.particles['Structure Type'])
  savetxt('data/y/iCNA_%s_%.2f.dat' % (dirs[i][3:],T), y, fmt='%d')
  del y

################################################################################
# Compute AJA prediction.                                                      #
################################################################################

for i in range(len(dirs)):
  for step in steps:
    pipeline = import_file(md_dir % (dirs[i],T,step))
    AJA = AcklandJonesModifier()
    AJA.structures[AJA.Type.ICO].enabled = False
    pipeline.modifiers.append(AJA)
    data = pipeline.compute()
    if 'y' in locals():
      y = concatenate((y,array(data.particles['Structure Type'])))
    else:
      y = array(data.particles['Structure Type'])
  savetxt('data/y/AJA_%s_%.2f.dat' % (dirs[i][3:],T), y, fmt='%d')
  del y

################################################################################
# Compute VoroTop prediction.                                                  #
################################################################################

for i in range(len(dirs)):
  for step in steps:
    pipeline = import_file(md_dir % (dirs[i],T,step))
    VTM = VoroTopModifier()
    VTM.filter_file='FCC-BCC-ICOS-HCP.filter'
    pipeline.modifiers.append(VTM)
    data = pipeline.compute()
    if 'y' in locals():
      y = concatenate((y,array(data.particles['Structure Type'])))
    else:
      y = array(data.particles['Structure Type'])
  savetxt('data/y/VTM_%s_%.2f.dat' % (dirs[i][3:],T), y, fmt='%d')
  del y

################################################################################
# Compute Chil+ prediction.                                                    #
################################################################################

for i in range(len(dirs)):
  if dirs[i][3:5] != 'cd' and dirs[i][3:5] != 'hd': continue
  for step in steps:
    pipeline = import_file(md_dir % (dirs[i],T,step))
    CPA = ChillPlusModifier()
    CPA.cutoff = CP_cutoff[i]
    pipeline.modifiers.append(CPA)
    data = pipeline.compute()
    if 'y' in locals():
      y = concatenate((y,array(data.particles['Structure Type'])))
    else:
      y = array(data.particles['Structure Type'])
  savetxt('data/y/CPA_%s_%.2f.dat' % (dirs[i][3:],T), y, fmt='%d')
  del y

################################################################################
