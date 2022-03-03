from numpy import *
from numpy.linalg import norm

# Read data files faster than numpy's loadtxt.
def read(fname,dtype=float64):
  # Count number of rows and columns.
  with open(fname,'r') as f:
    nrows = 0
    for line in f: 
      if line[0] == '#': continue
      nrows += 1
    ncols = len(line.split())
  # Allocate memory for data.
  if ncols > 1:
    X = zeros((nrows,ncols),dtype=dtype)
  else:
    X = zeros(nrows,dtype=dtype)
  # Read data.
  with open(fname,'r') as f:
    irow = 0
    for line in f:
      if line[0] == '#': continue
      X[irow] = array(line.split(),dtype=dtype)
      irow += 1
  return X

# Read only a predetermined number of rows.
def read_partial(fname,nrows,ncols,dtype=float64):
  # Allocate memory for data.
  if ncols > 1:
    X = zeros((nrows,ncols),dtype=dtype)
  else:
    X = zeros(nrows,dtype=dtype)
  # Read data.
  with open(fname,'r') as f:
    irow = 0
    for line in f:
      if line[0] == '#': continue
      X[irow] = array(line.split(),dtype=dtype)
      irow += 1
      if irow == nrows: break
  return X
