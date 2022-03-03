import matplotlib.pyplot as plt
from numpy import *

################################################################################
# Plot neurons and learning rate.                                              #
################################################################################

# Setup
N = [5,10,20,50,100] # Hidden layers size.
epsilon = [0.0001, 0.001, 0.002, 0.005, 0.010] # Learning rate init.
acc = zeros((5,5))
err = zeros((5,5))
for i in range(5):
  for j in range(5):
    data = loadtxt('../data/scores/neurons_%d_%d.dat' % (i,j))
    acc[i,j] = data[0]
    err[i,j] = data[1]

# Start figure.
fig = plt.figure()
ax  = fig.add_axes([0.15, 0.15, 0.80, 0.80])

# Plot.
for n in range(5):
  ax.plot(epsilon, acc[:,n], 'C%d-' % n, lw=2, label='(%d,%d,%d)' % (N[n],N[n],N[n]))
  ax.fill_between(epsilon, acc[:,n]-err[:,n], acc[:,n]+err[:,n], alpha=0.2, color='C%d' % n, lw=0)
 
# Add details.
ax.set_xlabel(r'Learning rate initialization')
ax.set_ylabel(r'Accuracy')
ax.set_ylim(0.96,0.98)
ax.set_xlim(0,0.010)
ax.legend(fontsize=12,ncol=1, title='Neural network size')

# Save figure.
fig.savefig("figures/fig_neurons_and_learning_rate.pdf")
plt.close()

################################################################################
# Plot number of hidden layers.                                                #
################################################################################

# Setup
N = [1,2,3,4,5] # Hidden layers size.
acc = zeros(5)
err = zeros(5)
for n in range(len(N)):
    data = loadtxt('../data/scores/hidden_layers_%d.dat' % (n+1))
    acc[n] = data[0]
    err[n] = data[1]

# Start figure.
fig = plt.figure()
ax  = fig.add_axes([0.15, 0.15, 0.80, 0.80])

# Plot.
ax.plot(N, acc, 'C0-', lw=3)
ax.fill_between(N, acc-err, acc+err, alpha=0.2, color='C0', lw=0)
 
# Add details.
ax.set_xlabel(r'Number of hidden layers')
ax.set_ylabel(r'Accuracy')
ax.set_ylim(0.97,0.98)
ax.set_xlim(1,5)

# Save figure.
fig.savefig("figures/fig_hidden_layers.pdf")
plt.close()

################################################################################
# Plot learning curve.                                                         #
################################################################################

# Setup
f = arange(1,11)/10
N = f * 414000 * 0.8 # Size of training set.
acc = zeros(len(N))
err = zeros(len(N))
for n in range(len(N)):
  data = loadtxt('../data/scores/learning_curve_%.1f.dat' % f[n])
  acc[n] = data[0]
  err[n] = data[1]

# Start figure.
fig = plt.figure()
ax  = fig.add_axes([0.15, 0.15, 0.80, 0.80])

# Plot.
ax.plot(N, acc, 'C1-', lw=2)
ax.fill_between(N, acc-err, acc+err, alpha=0.2, color='C1', lw=0)
 
# Add details.
ax.set_xlabel(r'Training set size')
ax.set_ylabel(r'Accuracy')
ax.set_ylim(0.95,0.98)
ax.set_xlim(0,400000)

# Save figure.
fig.savefig("figures/fig_training_curve.pdf")
plt.close()

################################################################################
