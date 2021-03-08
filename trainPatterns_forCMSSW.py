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


# Generate all sets of semilayer-semilayer patterns

# --> Positive slope, left laterality
######################################################################################
# Starting point: each layer of SL1 (l_in_sl1), 
# first cell (starting from the left), left laterality,
# and positive slope 
for l_in_sl1 in range(0, 4):
    print("")
    print("Layer in SL1 = {}".format(l_in_sl1))
    x0 = MBTrain.layers[l_in_sl1].DTlist[0].xmin + MBTrain.layers[l_in_sl1].DTlist[0].width/4. 
    y0 = MBTrain.layers[l_in_sl1].DTlist[0].ymin + MBTrain.layers[l_in_sl1].DTlist[0].height/2.

    # Final point: each layer of SL3: consider all valid cells and both lateralities
    for l_in_sl3 in range(4, 8):
        print("Layer in SL3 = {}".format(l_in_sl3))
        for d in MBTrain.layers[l_in_sl3].DTlist:
            # Consider both lateralities
            for semicell in [0.25, 0.75]:
                xf = d.xmin + semicell*d.width
                if abs(xf - x0) < 0.1*d.width: 
                    m = 100000
                else:
                    yf = d.ymin + d.height/2.
                    m = (yf-y0)/(xf-x0)
                if abs(m) < mmax:  continue
                mm = Muon(x0, y0, m)
                if m < mmax: 
                    mm.color = "k-"
                MBTrainf.checkIn(mm)
                if (l_in_sl3 == 7 and l_in_sl1 == 0):
                    mm.plot()        
                if abs(m) > mmax:
                    allPatterns.append(mm.getPattern())
                    allSeeds.append([l_in_sl1, l_in_sl3, d.idx - MBTrain.layers[l_in_sl1].DTlist[0].idx])


# --> Negative slope, left laterality
######################################################################################
# Starting point: each layer of SL1 (l_in_sl1), 
# first cell (starting from the right), left laterality,
# and negative slope 

for l_in_sl1 in range(0, 4):
    print("")
    print("Layer in SL1 = {}".format(l_in_sl1))
    x0 = MBTrain.layers[l_in_sl1].DTlist[-1].xmin + MBTrain.layers[l_in_sl1].DTlist[-1].width/4. 
    y0 = MBTrain.layers[l_in_sl1].DTlist[-1].ymin + MBTrain.layers[l_in_sl1].DTlist[-1].height/2.

    # Final point: each layer of SL3: consider all valid cells and both lateralities
    for l_in_sl3 in range(4, 8):
        print("Layer in SL3 = {}".format(l_in_sl3))
        for d in MBTrain.layers[l_in_sl3].DTlist:
            for semicell in [0.25, 0.75]:
                xf = d.xmin + semicell*d.width
                if abs(xf - x0) < 0.1*d.width: 
                    m = 100000
                else:
                    yf = d.ymin + d.height/2.
                    m = (yf - y0)/(xf - x0)
                if abs(m) < mmax:  continue
                mm = Muon(x0, y0, m)
                if m < mmax: 
                    mm.color = "k-"
                MBTrainf.checkIn(mm)
                # mm.plot()        
                if abs(m) > mmax:
                    allPatterns.append(mm.getPattern())
                    allSeeds.append([l_in_sl1, l_in_sl3, d.idx - MBTrain.layers[l_in_sl1].DTlist[-1].idx])



# --> Positive slope, right laterality
######################################################################################
# Starting point: each layer of SL1 (l_in_sl1), 
# first cell (starting from the left), right laterality,
# and positive slope 

for l_in_sl1 in range(0, 4):
    print("")
    print("Layer in SL1 = {}".format(l_in_sl1))
    x0 = MBTrain.layers[l_in_sl1].DTlist[0].xmin + 3*MBTrain.layers[l_in_sl1].DTlist[0].width/4. 
    y0 = MBTrain.layers[l_in_sl1].DTlist[0].ymin +   MBTrain.layers[l_in_sl1].DTlist[0].height/2.

    # Final point: each layer of SL3: consider all valid cells and both lateralities
    for l_in_sl3 in range(4, 8):
        print("Layer in SL3 = {}".format(l_in_sl3))
        for d in MBTrain.layers[l_in_sl3].DTlist:
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
                MBTrainf.checkIn(mm)
                # mm.plot()        
                if abs(m) > mmax:
                    allPatterns.append(mm.getPattern())
                    allSeeds.append([l_in_sl1, l_in_sl3, d.idx - MBTrain.layers[l_in_sl1].DTlist[0].idx])


# --> Negative slope, right laterality
######################################################################################
# Starting point: each layer of SL1 (l_in_sl1), 
# first cell (starting from the right), right laterality,
# and negative slope 

for l_in_sl1 in range(0, 4):
    print("")
    print("Layer in SL1 = {}".format(l_in_sl1))
    x0 = MBTrain.layers[l_in_sl1].DTlist[-1].xmin + 3*MBTrain.layers[l_in_sl1].DTlist[-1].width/4. 
    y0 = MBTrain.layers[l_in_sl1].DTlist[-1].ymin +   MBTrain.layers[l_in_sl1].DTlist[-1].height/2.

    # Final point: each layer of SL3: consider all valid cells and both lateralities
    for l_in_sl3 in range(4, 8):
        print("Layer in SL3 = {}".format(l_in_sl3))
        for d in MBTrain.layers[l_in_sl3].DTlist:
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
                MBTrainf.checkIn(mm)
                # mm.plot()        
                if abs(m) > mmax:
                    allPatterns.append(mm.getPattern())
                    allSeeds.append([l_in_sl1, l_in_sl3, d.idx - MBTrain.layers[l_in_sl1].DTlist[-1].idx])



#################################################
### And now the uncorrelated sets of patterns ###
#################################################

# Starting from uncorrelated in SL1

# --> Positive slope, left laterality
######################################################################################
# Starting point: each layer of SL1 (l_in_sl1), 
# first cell (starting from the left), left laterality,
# and positive slope 

for l_in_sl1 in range(0, 4):
    print("")
    print("Lower layer in SL1 = {}".format(l_in_sl1))
    x0 = MBTrain.layers[l_in_sl1].DTlist[0].xmin + MBTrain.layers[l_in_sl1].DTlist[0].width/4. 
    y0 = MBTrain.layers[l_in_sl1].DTlist[0].ymin + MBTrain.layers[l_in_sl1].DTlist[0].height/2.

    # Final point: each layer of SL1 (excluding the one from where we start), 
    # considering all valid cells and both lateralities
    for l_in_sl1_up in range(l_in_sl1 + 1, 4):
        print("Upper layer in SL1 = {}".format(l_in_sl1_up))
        for d in MBTrain.layers[l_in_sl1_up].DTlist:
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
                MBTrainf.checkIn(mm)
                # mm.plot()        
                if abs(m) > mmax:
                    allPatterns.append(mm.getPattern())
                    allSeeds.append([l_in_sl1, l_in_sl1_up, d.idx - MBTrain.layers[l_in_sl1].DTlist[0].idx])


# --> Negative slope, left laterality
######################################################################################
# Starting point: each layer of SL1 (l_in_sl1), 
# first cell (starting from the left), left laterality,
# and negative slope 

for l_in_sl1 in range(0, 4):
    print("")
    print("Lower layer in SL1 = {}".format(l_in_sl1))
    x0 = MBTrain.layers[l_in_sl1].DTlist[-1].xmin + MBTrain.layers[l_in_sl1].DTlist[-1].width/4. 
    y0 = MBTrain.layers[l_in_sl1].DTlist[-1].ymin + MBTrain.layers[l_in_sl1].DTlist[-1].height/2.

    # Final point: each layer of SL1 (excluding the one from where we start), 
    # considering all valid cells and both lateralities
    for l_in_sl1_up in range(l_in_sl1 + 1, 4):
        print("Upper layer in SL1 = {}".format(l_in_sl1_up))
        for d in MBTrain.layers[l_in_sl1_up].DTlist:
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
                MBTrainf.checkIn(mm)
                # mm.plot()        
                if abs(m) > mmax:
                    allPatterns.append(mm.getPattern())
                    allSeeds.append([l_in_sl1, l_in_sl1_up, d.idx - MBTrain.layers[l_in_sl1].DTlist[-1].idx])


# --> Positive slope, right laterality
######################################################################################
# Starting point: each layer of SL1 (l_in_sl1), 
# first cell (starting from the left), right laterality,
# and positive slope 

for l_in_sl1 in range(0, 4):
    print("")
    print("Lower layer in SL1 = {}".format(l_in_sl1))
    x0 = MBTrain.layers[l_in_sl1].DTlist[0].xmin + 3*MBTrain.layers[l_in_sl1].DTlist[0].width/4. 
    y0 = MBTrain.layers[l_in_sl1].DTlist[0].ymin +   MBTrain.layers[l_in_sl1].DTlist[0].height/2.

    # Final point: each layer of SL1 (excluding the one from where we start), 
    # considering all valid cells and both lateralities
    for l_in_sl1_up in range(l_in_sl1 + 1, 4):
        print("Upper layer in SL1 = {}".format(l_in_sl1_up))
        for d in MBTrain.layers[l_in_sl1_up].DTlist:
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
                MBTrainf.checkIn(mm)
                # mm.plot()        
                if abs(m) > mmax:
                    allPatterns.append(mm.getPattern())
                    allSeeds.append([l_in_sl1, l_in_sl1_up, d.idx - MBTrain.layers[l_in_sl1].DTlist[0].idx])


# --> Negative slope, right laterality
######################################################################################
# Starting point: each layer of SL1 (l_in_sl1), 
# first cell (starting from the right), right laterality,
# and negative slope 

for l_in_sl1 in range(0, 4):
    print("")
    print("Lower layer in SL1 = {}".format(l_in_sl1))
    x0 = MBTrain.layers[l_in_sl1].DTlist[-1].xmin + 3*MBTrain.layers[l_in_sl1].DTlist[-1].width/4. 
    y0 = MBTrain.layers[l_in_sl1].DTlist[-1].ymin +   MBTrain.layers[l_in_sl1].DTlist[-1].height/2.

    # Final point: each layer of SL1 (excluding the one from where we start), 
    # considering all valid cells and both lateralities
    for l_in_sl1_up in range(l_in_sl1 + 1, 4):
        print("Upper layer in SL1 = {}".format(l_in_sl1_up))
        for d in MBTrain.layers[l_in_sl1_up].DTlist:
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
                MBTrainf.checkIn(mm)
                # mm.plot()        
                if abs(m) > mmax:
                    allPatterns.append(mm.getPattern())
                    allSeeds.append([l_in_sl1, l_in_sl1_up, d.idx - MBTrain.layers[l_in_sl1].DTlist[-1].idx])


# And now uncorrelated in SL3

# --> Positive slope, left laterality
######################################################################################
# Starting point: each layer of SL3 (l_in_sl3), 
# first cell (starting from the left), left laterality,
# and positive slope 

for l_in_sl3 in range(4, 8):
    print("")
    print("Lower layer in SL3 = {}".format(l_in_sl3))
    x0 = MBTrain.layers[l_in_sl3].DTlist[0].xmin + MBTrain.layers[l_in_sl3].DTlist[0].width/4. 
    y0 = MBTrain.layers[l_in_sl3].DTlist[0].ymin + MBTrain.layers[l_in_sl3].DTlist[0].height/2.

    # Final point: each layer of SL3 (excluding the one from where we start), 
    # considering all valid cells and both lateralities
    for l_in_sl3_up in range(l_in_sl3 + 1, 8):
        print("Upper layer in SL3 = {}".format(l_in_sl3_up))
        for d in MBTrain.layers[l_in_sl3_up].DTlist:
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
                MBTrainf.checkIn(mm)
                # mm.plot()        
                if abs(m) > mmax:
                    allPatterns.append(mm.getPattern())
                    allSeeds.append([l_in_sl3, l_in_sl3_up, d.idx - MBTrain.layers[l_in_sl3].DTlist[0].idx])


# --> Negative slope, left laterality
######################################################################################
# Starting point: each layer of SL3 (l_in_sl3), 
# first cell (starting from the left), left laterality,
# and negative slope 

for l_in_sl3 in range(4, 8):
    print("")
    print("Lower layer in SL3 = {}".format(l_in_sl3))
    x0 = MBTrain.layers[l_in_sl3].DTlist[-1].xmin + MBTrain.layers[l_in_sl3].DTlist[-1].width/4. 
    y0 = MBTrain.layers[l_in_sl3].DTlist[-1].ymin + MBTrain.layers[l_in_sl3].DTlist[-1].height/2.

    # Final point: each layer of SL3 (excluding the one from where we start), 
    # considering all valid cells and both lateralities
    for l_in_sl3_up in range(l_in_sl3 + 1, 8):
        print("Upper layer in SL3 = {}".format(l_in_sl3_up))
        for d in MBTrain.layers[l_in_sl3_up].DTlist:
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
                MBTrainf.checkIn(mm)
                # mm.plot()        
                if abs(m) > mmax:
                    allPatterns.append(mm.getPattern())
                    allSeeds.append([l_in_sl3, l_in_sl3_up, d.idx - MBTrain.layers[l_in_sl3].DTlist[-1].idx])


# --> Positive slope, right laterality
######################################################################################
# Starting point: each layer of SL3 (l_in_sl3), 
# first cell (starting from the left), right laterality,
# and positive slope 

for l_in_sl3 in range(4, 8):
    print("")
    print("Lower layer in SL3 = {}".format(l_in_sl3))
    x0 = MBTrain.layers[l_in_sl3].DTlist[0].xmin + 3*MBTrain.layers[l_in_sl3].DTlist[0].width/4. 
    y0 = MBTrain.layers[l_in_sl3].DTlist[0].ymin +   MBTrain.layers[l_in_sl3].DTlist[0].height/2.

    # Final point: each layer of SL1 (excluding the one from where we start), 
    # considering all valid cells and both lateralities
    for l_in_sl3_up in range(l_in_sl3 + 1, 8):
        print("Upper layer in SL1 = {}".format(l_in_sl3_up))
        for d in MBTrain.layers[l_in_sl3_up].DTlist:
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
                MBTrainf.checkIn(mm)
                # mm.plot()        
                if abs(m) > mmax:
                    allPatterns.append(mm.getPattern())
                    allSeeds.append([l_in_sl3, l_in_sl3_up, d.idx - MBTrain.layers[l_in_sl3].DTlist[0].idx])


# --> Negative slope, right laterality
######################################################################################
# Starting point: each layer of SL3 (l_in_sl3), 
# first cell (starting from the right), right laterality,
# and negative slope 

for l_in_sl3 in range(4, 8):
    print("")
    print("Lower layer in SL3 = {}".format(l_in_sl3))
    x0 = MBTrain.layers[l_in_sl3].DTlist[-1].xmin + 3*MBTrain.layers[l_in_sl3].DTlist[-1].width/4. 
    y0 = MBTrain.layers[l_in_sl3].DTlist[-1].ymin +   MBTrain.layers[l_in_sl3].DTlist[-1].height/2.

    # Final point: each layer of SL3 (excluding the one from where we start), 
    # considering all valid cells and both lateralities
    for l_in_sl3_up in range(l_in_sl3 + 1, 8):
        print("Upper layer in SL3 = {}".format(l_in_sl3_up))
        for d in MBTrain.layers[l_in_sl3_up].DTlist:
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
                MBTrainf.checkIn(mm)
                # mm.plot()        
                if abs(m) > mmax:
                    allPatterns.append(mm.getPattern())
                    allSeeds.append([l_in_sl3, l_in_sl3_up, d.idx - MBTrain.layers[l_in_sl3].DTlist[-1].idx])


# Plots, printouts, and save
listPatterns = []

for i in range(len(allPatterns)):
      listPatterns.append(Pattern(allSeeds[i], allPatterns[i]))
      # print "---------------------------------"
      # print allSeeds[i], allPatterns[i]
      # print "---------------------------------"

print "Patterns: ", len(listPatterns)
pick = open("./MBTrainTraining_uncorrelated_MB4.pck", "w")
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
MBTrain.plot()

plt.axis([0,170,-5,30])
plt.xlabel("z/cm")
plt.ylabel("r/cm")
plt.show()

