import numpy as np
import matplotlib.pyplot as plt
from stationsObjects import*
import copy
import pickle


#mmax = -10000
#mmax =  2*MBTrain.layers[0].DTlist[0].height/MBTrain.layers[0].DTlist[0].width 

# Maximum slope allowed for a pattern (mmax is the atan of the phi angle)
mmax = 0.3

allPatterns = []
allSeeds    = [] #Naming convention is [SLdown, SLup, diff in units of halfs of cell width] == [SLup, SLdown, -diff]

# Choose which MB use for training,
# considering those defined in stationsObjects.py
MB_train   = MBTrain
MB_train_f = MBTrainf
#MB_train   = MB4
#MB_train_f = MB4f

# Output file name
output_file_name = "trainedPatterns_MB.pck"
#output_file_name = "trainedPatterns_MB4.pck"

# Generate all sets of semilayer-semilayer patterns

#################################################
### Starting from correlated sets of patterns ###
#################################################

#################################################
# Starting point: each layer of SL1 (l_in_sl1), 
# first cell (starting from left or right), 
# both lateralities, positive and negative slope 

for slope in [0, -1]:
    for lat in [0.25, 0.75]:
        for l_in_sl1 in range(0, 4):
            print("")
            print("Layer in SL1 = {}".format(l_in_sl1))
            x0 = MB_train.layers[l_in_sl1].DTlist[slope].xmin + lat*MB_train.layers[l_in_sl1].DTlist[slope].width 
            y0 = MB_train.layers[l_in_sl1].DTlist[slope].ymin + MB_train.layers[l_in_sl1].DTlist[slope].height/2.

            # Final point: each layer of SL3: consider all valid cells and both lateralities
            for l_in_sl3 in range(4, 8):
                print("Layer in SL3 = {}".format(l_in_sl3))
                for d in MB_train.layers[l_in_sl3].DTlist:
                    # Consider both lateralities
                    for semicell in [0.25, 0.75]:
                        xf = d.xmin + semicell*d.width
                        if abs(xf - x0) < 0.1*d.width: 
                            m = 100000
                        else:
                            yf = d.ymin + d.height/2.
                            m = (yf - y0)/(xf - x0)
                        if abs(m) < mmax:  continue
                        mm = Muon(x0, y0, m)
                        #if m < mmax: 
                        if slope == -1:
                            mm.color = "k-"
                        MB_train_f.checkIn(mm)
                        if (l_in_sl3 == 7 and l_in_sl1 == 0):
                            mm.plot()        
                        if abs(m) > mmax:
                            allPatterns.append(mm.getPattern())
                            allSeeds.append([l_in_sl1, l_in_sl3, d.idx - MB_train.layers[l_in_sl1].DTlist[slope].idx])


#################################################
### And now the uncorrelated sets of patterns ###
#################################################

# Starting from uncorrelated in SL1

#################################################
# Starting point: each layer of SL1 (l_in_sl1), 
# first cell (starting from left or right), 
# both lateralities, positive and negative slope 

for slope in [0, -1]:
    for lat in [0.25, 0.75]:
        for l_in_sl1 in range(0, 4):
            print("")
            print("Lower layer in SL1 = {}".format(l_in_sl1))
            x0 = MB_train.layers[l_in_sl1].DTlist[slope].xmin + lat*MB_train.layers[l_in_sl1].DTlist[slope].width
            y0 = MB_train.layers[l_in_sl1].DTlist[slope].ymin + MB_train.layers[l_in_sl1].DTlist[slope].height/2.

            # Final point: each layer of SL1 (excluding the one from where we start), 
            # considering all valid cells and both lateralities
            for l_in_sl1_up in range(l_in_sl1 + 1, 4):
                print("Upper layer in SL1 = {}".format(l_in_sl1_up))
                for d in MB_train.layers[l_in_sl1_up].DTlist:
                    for semicell in [0.25, 0.75]:
                        xf = d.xmin + semicell*d.width
                        if abs(xf - x0) < 0.1*d.width: 
                            m = 100000
                        else:
                            yf = d.ymin + d.height/2.
                            m = (yf - y0)/(xf - x0)
                        if abs(m) < mmax:  continue
                        mm = Muon(x0,y0, m)
                        if m < mmax: 
                            mm.color = "k-"
                        MB_train_f.checkIn(mm)
                        # mm.plot()        
                        if abs(m) > mmax:
                            allPatterns.append(mm.getPattern())
                            allSeeds.append([l_in_sl1, l_in_sl1_up, d.idx - MB_train.layers[l_in_sl1].DTlist[slope].idx])


# And now uncorrelated in SL3

#################################################
# Starting point: each layer of SL3 (l_in_sl3), 
# first cell (starting from left or right), 
# both lateralities, positive and negative slope 

for slope in [0, -1]:
    for lat in [0.25, 0.75]:
        for l_in_sl3 in range(4, 8):
            print("")
            print("Lower layer in SL3 = {}".format(l_in_sl3))
            x0 = MB_train.layers[l_in_sl3].DTlist[slope].xmin + lat*MB_train.layers[l_in_sl3].DTlist[slope].width
            y0 = MB_train.layers[l_in_sl3].DTlist[slope].ymin + MB_train.layers[l_in_sl3].DTlist[slope].height/2.

            # Final point: each layer of SL3 (excluding the one from where we start), 
            # considering all valid cells and both lateralities
            for l_in_sl3_up in range(l_in_sl3 + 1, 8):
                print("Upper layer in SL3 = {}".format(l_in_sl3_up))
                for d in MB_train.layers[l_in_sl3_up].DTlist:
                    for semicell in [0.25, 0.75]:
                        xf = d.xmin + semicell*d.width
                        if abs(xf - x0) < 0.1*d.width: 
                            m = 100000
                        else:
                            yf = d.ymin + d.height/2.
                            m = (yf - y0)/(xf - x0)
                        if abs(m) < mmax:  continue
                        mm = Muon(x0,y0, m)
                        if m < mmax: 
                            mm.color = "k-"
                        MB_train_f.checkIn(mm)
                        # mm.plot()        
                        if abs(m) > mmax:
                            allPatterns.append(mm.getPattern())
                            allSeeds.append([l_in_sl3, l_in_sl3_up, d.idx - MB_train.layers[l_in_sl3].DTlist[slope].idx])


# Plots, printouts, and save
listPatterns = []

for i in range(len(allPatterns)):
      listPatterns.append(Pattern(allSeeds[i], allPatterns[i]))
      # print "---------------------------------"
      # print allSeeds[i], allPatterns[i]
      # print "---------------------------------"

print "Patterns: ", len(listPatterns)

pick = open(output_file_name, "w")
pickle.dump(listPatterns, pick)

"""
overlaps = 0
for i in range(len(listPatterns)):
    for j in range(len(listPatterns)):
        if listPatterns[i].isEqual(listPatterns[j]): overlaps += 1

#print [i.overlap for i in listPatterns]
print overlaps
"""

#print listPatterns[0].overlapsw
MB_train.plot()

plt.axis([0,170,-5,30])
plt.xlabel("z/cm")
plt.ylabel("r/cm")
plt.show()

