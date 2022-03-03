from numpy import *

import sys
sys.path.append('/home/freitas/dc3/single_element/ml/util')
from constants import md_lattices

################################################################################

# Traditional methods labels and colors.
methods_per_lattice = [['PTM', 'iCNA', 'CNA', 'AJA', 'VTM'],
                       ['PTM', 'iCNA', 'CNA', 'AJA', 'VTM'],
                       ['PTM', 'iCNA', 'CNA', 'AJA', 'VTM'],
                       ['PTM', 'CNA', 'CPA'],
                       ['PTM', 'CNA', 'CPA'],
                       ['PTM'],
                       ['PTM', 'iCNA', 'CNA', 'AJA', 'VTM'],
                       ['PTM', 'iCNA', 'CNA', 'AJA', 'VTM'],
                       ['PTM', 'iCNA', 'CNA', 'AJA', 'VTM'],
                       ['PTM', 'CNA', 'CPA'],
                       ['PTM', 'iCNA', 'CNA', 'AJA', 'VTM', 'CPA']]

lattice = ['fcc', 'bcc', 'hcp', 'cd', 'hd', 'sc', 'fcc', 'bcc', 'hcp', 'cd']
methods = array(['PTM', 'iCNA', 'CNA', 'AJA', 'VTM', 'CPA'])
method_name = array(['PTM', 'iCNA', 'CNA', 'AJA', 'VoroTop', 'Chill+'])
material = ['Al', 'Fe', 'Ti', 'Si', 'H$_2$O', 'NaCl', 'Ar', 'Li', 'Mg','Ge']
n = 19
m = 8
indent = '' # 6*' '

with open('../../../traditional_methods/03_accuracies/data/accuracies/liquid.dat','r') as f_liquid:
  f_liquid.readline()
  with open('../data/post_processed/accuracy_table.dat','w') as f:
    # Print header.
    f.write(indent+m*' ')
    for i in range(len(lattice)):
      f.write('& %s (%s)' % (material[i],lattice[i]) + (n-3-len(lattice[i])-len(material[i]))*' ')
    f.write('& liquid ')
    f.write('\\\\ \hline \n')
    # Print DC3 results.
    f.write(indent+'DC3' + (m-3)*' ')
    min_acc = 100.0
    max_acc = 0
    for i in range(len(lattice)):
      T, acc, acc_err = loadtxt('../data/post_processed/accuracy_vs_temperature_%s.dat' % md_lattices[i],unpack=True)
      acc = around(acc[T==1.00][0],1)
      acc_err = max(10*around(acc_err[T==1.00][0],1),1)
      if acc == 100: acc_err = 0
      if min_acc > acc:
        min_acc = acc
        min_latt = material[i]+'('+lattice[i]+')'
      if max_acc < acc:
        max_acc = acc
        max_latt = material[i]+'('+lattice[i]+')'
      f.write(r'& \textbf{%5.1f (%d)}' % (acc,acc_err) + 1*' ')
    print('DC3: %.2f %s vs %s' % (around(max_acc/min_acc,2),min_latt,max_latt))
    acc, acc_err = loadtxt('../data/post_processed/accuracy_liquid.dat',unpack=True)
    cf = loadtxt('../data/post_processed/confusion_matrix.dat')
    acc = around(acc+cf[-1,-1],1)
    acc_err = max(10*around(acc_err,1),1)
    f.write(r'& %5.1f (%d)' % (acc,acc_err) + 1*' ')
    f.write('\\\\\n')
    # Print methods line by line.
    for j in range(len(methods)):
      f.write(indent+method_name[j] + (m-len(method_name[j]))*' ')
      min_acc = 100.0
      max_acc = 0
      for i in range(len(lattice)):
        if methods[j] in methods_per_lattice[i]:
          T, acc, acc_err = loadtxt('../../../traditional_methods/03_accuracies/data/accuracies/%s_%s.dat' % (methods[j],md_lattices[i]), unpack=True)
          acc = around(acc[T==1.00][0],1)
          acc_err = max(10*around(acc_err[T==1.00][0],1),1)
          if acc == 100: acc_err = 0
          if min_acc > acc:
            min_acc = acc
            min_latt = material[i]+'('+lattice[i]+')'
          if max_acc < acc:
            max_acc = acc
            max_latt = material[i]+'('+lattice[i]+')'
          f.write('&' + (n-9)*' ' + '%5.1f (%d)' % (acc,acc_err) + ' ')
        else:
          f.write('&' + (n-2)*' ' + '-- ')
      print('%s: %.2f %s vs %s' % (methods[j],around(max_acc/min_acc,2),min_latt,max_latt))
      line = f_liquid.readline().split(' ')
      acc = float(line[-2])
      acc_err = float(line[-1])
      acc = around(acc,1)
      acc_err = max(10*around(acc_err,1),1)
      if acc == 100: acc_err = 0
      f.write('& %5.1f (%d)' % (acc,acc_err) + ' ')
      f.write('\\\\\n')
  

################################################################################
