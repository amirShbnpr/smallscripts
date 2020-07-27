import csv
import sys
import pandas as pd
import numpy as np
from math import pow,sqrt

root = []
disLoc = []
for i in range(1,len(sys.argv), 2):    
    root.append(pd.read_csv(sys.argv[i], header=None))
    disLoc.append(pd.read_csv(sys.argv[i+1], header=None))
root = np.array(root)
disLoc = np.array(disLoc)


drvClctr = [[],[],[],[],[]]
xx = []
for j in range(0, len(root)):
    for i in range(0, len(disLoc[j])):
        deriv =  disLoc[j][i][1] - root[j][i][1]
        drvClctr[j].append(deriv / 0.001)
        xx.append(root[0][i][0])
drvClctr = np.array(drvClctr)

errMat = []
with open("", 'r') as covInp:
    csvRdr = csv.reader(covInp, delimiter=",")
    for row in csvRdr:
        row = [float(item) for item in row]
        errMat.append(row)

outRoot = []
for i in range(0,len(drvClctr[0])):
    a = 0
    for k in range(0, len(drvClctr)):
        for j in range(0, len(drvClctr)):    
            a += drvClctr[j][i] * errMat[j][k] * drvClctr[k][i]
    outRoot.append(sqrt(a))

uppBnd = []
dnBnd = []
centre = []
for i in range(0,len(root[0])):
    uppBnd.append(root[0][i][1] + outRoot[i])
    dnBnd.append(root[0][i][1] - outRoot[i])
    centre.append(root[0][i][1])
with open('', 'w+') as outp:
    for i in range(0, len(centre)):
        a = str(xx[i]) + "\t" + str(centre[i]) + "\t" + str(uppBnd[i])+"\t"+ str(dnBnd[i]) + '\n'
        outp.writelines(a)
