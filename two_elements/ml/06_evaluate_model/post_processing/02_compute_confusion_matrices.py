from numpy import *
from sklearn.metrics import confusion_matrix 

import sys
sys.path.append('/home/freitas/dc3/two_elements/ml/util')
from read_functions import read

# Load MD crystal predicted and true labels.
y_pred = read('../data/y_pred_md_crystal.dat')
y_true = read('../../02_organize_data/data/md_crystal/y.dat')

# Screen MD data for melting temperature only.
yT = read('../../02_organize_data/data/md_crystal/yT.dat')
cond = isclose(yT,1.00,atol=1e-3)
y_pred = y_pred[cond]
y_true = y_true[cond]

# Load MD liquid data.
y_pred = concatenate((y_pred,read('../data/y_pred_md_liquid.dat')))
y_true = concatenate((y_true,zeros(len(y_pred)-len(y_true))))

# Compute the confusion matrix for the first data set (positive true labels).
cm = 100*confusion_matrix(y_true,y_pred,normalize='true',labels=[1,2,3,4,5,6,0,-1]) 
cm = cm[:-1] # Eliminate row of unknown crystal label (no data, all zeros).
savetxt('../data/post_processed/confusion_matrix.dat', cm, fmt='%7.3f')
