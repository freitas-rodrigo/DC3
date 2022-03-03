from numpy import *
from sklearn.neural_network import MLPClassifier
import joblib

import sys
sys.path.append('/home/freitas/dc3/single_element/ml/util')
from read_functions import read

X = read('../02_organize_data/data/synthetic_crystal/X.dat')
y = read('../02_organize_data/data/synthetic_crystal/y.dat')
NN = MLPClassifier(hidden_layer_sizes=(100,100,100), early_stopping=True, learning_rate_init=0.005, verbose=1)
NN.fit(X,y)
joblib.dump(NN,'data/neural_network.pkl')
