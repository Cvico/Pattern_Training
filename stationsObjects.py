import numpy as np
import matplotlib.pyplot as plt

# DT chamber measures
globalDTwidth  = 4.2
globalDTheight = 1.3

# Gap between SL1 and SL3
SLgap     = 28.7 - globalDTheight*8 # originally, it was 29 - globalDTheight*8  ????
# SLgap_MB4 = 28.7 - globalDTheight*12 # 

# Number of cell per layer depending on the MB
nDTMB1 = 80 # 47
nDTMB2 = 80 # 59
nDTMB3 = 80 # 73
nDTMB4 = 80 # 102

# There is traslational symmetry in the patterns,
# and we have a maximum slope: 40 cells are enough, 
# independently of the MB?
nDTMBTrain = 40 

class Muon(object):
    def __init__(self, x0,y0, m):
        self.x0 = x0
        self.y0 = y0
        self.m  = m
        self.cellHits  = []
        self.semicells = []
        self.color = "r-"

    def getY(self, x, ydef):
        if self.m == 100000: 
            return (abs(x - self.x0) < 0.05*globalDTwidth)*ydef + (abs(x - self.x0) > 0.05*globalDTwidth)*10000000000  
        return self.m*(x-self.x0) + self.y0

    def plot(self, xmin = -600., xmax= 600):
        xr = np.linspace(xmin, xmax, 10000)
        plt.plot(xr, self.getY(xr, 0.), self.color)    

    def printHits(self):
        for l in self.cellHits:
            print(l.parent.idx, l.idx)

    def getPattern(self):
        self.pattern = []
        for i in range(len(self.cellHits)):
            self.pattern.append([self.cellHits[i].parent.idx, self.cellHits[i].idx, self.semicells[i]])
        return self.pattern

    def getRecoPattern(self):
        self.recopattern = []
        for i in range(len(self.cellHits)):
            self.recopattern.append([self.cellHits[i].parent.idx, self.cellHits[i].idx])
        return self.recopattern

class DT(object):
    def __init__(self,x,y,height,width, parent=0, idx=-1):
        self.xmin = x
        self.ymin = y
        self.height = height
        self.width  = width
        self.idx    = idx
        self.parent = parent
        self.muons  = []
        self.isMIn   = False

    def plot(self, doSemi = True):
        if self.isMIn:
            color = "g-"
        else:
            color = "k-"
        plt.plot([self.xmin, self.xmin + self.width], [self.ymin, self.ymin], color)
        plt.plot([self.xmin, self.xmin + self.width], [self.ymin + self.height, self.ymin + self.height], color)
        plt.plot([self.xmin, self.xmin], [self.ymin, self.ymin+ self.height], color)
        plt.plot([self.xmin + self.width, self.xmin + self.width], [self.ymin, self.ymin+ self.height], color)
        if doSemi:
            plt.plot([self.xmin + 0.5*self.width, self.xmin + 0.5*self.width], [self.ymin, self.ymin+ self.height], "k--")

    def isIn(self, muon):
        semicellIzq = False
        semicellDer = False
        #print "First Checks"
        if max(muon.getY(self.xmin, self.ymin + self.height/2.), muon.getY(self.xmin + self.width, self.ymin + self.height/2.)) < self.ymin or min(muon.getY(self.xmin, self.ymin + self.height/2.), muon.getY(self.xmin + self.width, self.ymin + self.height/2.)) > (self.ymin + self.height) and not(muon.m == 100000): return  
        xr = np.linspace(self.xmin, self.xmin + self.width,100)
        #print "All in"
        yr = muon.getY(xr, self.ymin + self.height/2.)
        self.isMIn = any(np.array([ y >= self.ymin-0.01*self.height and y <= self.ymin+self.height*1.01 for y in yr]))
        xr = np.linspace(self.xmin, self.xmin + self.width/2.,100)
        #print "SemiIzq"
        yr = muon.getY(xr, self.ymin + self.height/2.)
        semicellIzq = any(np.array([ y >= self.ymin and y <= self.ymin+self.height for y in yr]))
        xr = np.linspace(self.xmin+ self.width/2., self.xmin + self.width,100)
        #print "SemiDer"
        yr = muon.getY(xr, self.ymin + self.height/2.)
        semicellDer = any(np.array([ y >= self.ymin and y <= self.ymin+self.height for y in yr]))
        
        if self.isMIn: 
            self.muons.append(muon)
            muon.cellHits.append(self)
            if semicellIzq and semicellDer:
                muon.semicells.append(0.)
            elif semicellIzq:
                muon.semicells.append(-1.)
            elif semicellDer:
                muon.semicells.append(1.)

    def center(self):
        return self.xmin + self.width/2., self.ymin + self.height/2.

class Layer(object):  
    def __init__(self,xoff,yoff,nDTs, along = "X", parent=0, idx=-1, offset=0):
        self.xmin = xoff
        self.ymin = yoff
        self.nDTs = nDTs
        self.along = along
        self.offset = offset
        self.createDTs(nDTs)
        self.parent = parent
        self.idx = idx

    def createDTs(self, nDT, height=globalDTheight, width=globalDTwidth):
        x = self.xmin
        y = self.ymin
        self.DTlist = []
        for i in range(nDT):
            self.DTlist.append(DT(x, y, height, width, self, idx=i-self.offset))
            if self.along == "X":
                x += width
            else:
                y += height            

        if self.along == "X":
                y += height
        else:
                x += width
        self.width = x - self.xmin
        self.height = y - self.ymin

    def plot(self):
        for d in self.DTlist: d.plot()

class MB(object):
    def __init__(self, layers):
        self.layers = layers
    def plot(self):
        for l in self.layers: l.plot()
    def checkIn(self, muon):
        for l in self.layers:
            for d in l.DTlist:
                d.isIn(muon)
      
class Pattern(object):
    def __init__(self, seeds, hits):
        self.seeds = seeds
        self.hits  = hits
        self.len   = len(hits)
        self.busted = False
        self.overlap = 0
        self.overlapsw = []

    def hasseed(self, hit):
        if hit == seed:
            return True
        else:
            return False

    def hashit(self, hit):
        for h in self.hits:
            if h[:2] == hit:
                return True
        return False

    def recoHits(self, extra = 0, reverse = 1):
        return [[h[0],reverse*h[1]+extra] for h in self.hits]

    def genHits(self, extra = 0, reverse = 1):
        return [[h[0],reverse*h[1]+extra, h[2]] for h in self.hits]

    def isEqual(self, other):
        isEqual = True
        for h in self.hits:
            if h in other.hits: continue
            else: isEqual = False
        for h in other.hits:
            if h in self.hits: continue
            else: isEqual = False
        if isEqual: 
            self.overlap += 1
        self.overlapsw.append(isEqual)
        return isEqual

def patternSorter(p):
    layers  = [h[0] for h in p[0]]
    layers  = list(dict.fromkeys(layers))
    nLayers = len(layers)
    nHits   = len(p[0])
    return nLayers*1000 + nHits


# Define function to create chambers
def create_chamber(DT_width, DT_height, n_cells, gap, shift = 0, additional_cells = 0):
    """shift is un units of DT_width. 
    - positive shift: SL3 shifted to the right wrt SL1;
    - negative shift: SL3 shifted to the left wrt SL1;
    """
    
    # Define layers for SL1
    layer1 = Layer(-additional_cells*DT_width,                   0,               n_cells, idx=1, offset=additional_cells)
    layer2 = Layer((-additional_cells + 0.5)*DT_width,           DT_height,       n_cells, idx=2, offset=additional_cells)
    layer3 = Layer(-additional_cells*DT_width,                 2*DT_height,       n_cells, idx=3, offset=additional_cells)
    layer4 = Layer((-additional_cells + 0.5)*DT_width,         3*DT_height,       n_cells, idx=4, offset=additional_cells)

    # Define layers for SL3
    layer5 = Layer((-additional_cells + shift)*DT_width,       4*DT_height + gap, n_cells, idx=5, offset=additional_cells)
    layer6 = Layer((-additional_cells + 0.5 + shift)*DT_width, 5*DT_height + gap, n_cells, idx=6, offset=additional_cells)
    layer7 = Layer((-additional_cells + shift)*DT_width,       6*DT_height + gap, n_cells, idx=7, offset=additional_cells)
    layer8 = Layer((-additional_cells + 0.5 + shift)*DT_width, 7*DT_height + gap, n_cells, idx=8, offset=additional_cells)

    # Finally, define de output chamber
    out_MB = MB([layer1, layer2, layer3, layer4, layer5, layer6, layer7, layer8])

    return out_MB


# Now define chambers.
# Reference for geometry at: https://docs.google.com/document/d/144Kr25ThVqTIM6lWib_Z-fogahEJ0MX1_EY3zL-LDsU/edit

#####################
# Define MB1 chambers
# In MB1, SL3 is shifted half a cell wrt SL1

# These are used to generate muons
MB1_left  = create_chamber(globalDTwidth, globalDTheight, nDTMB1, SLgap, -0.5)
MB1_right = create_chamber(globalDTwidth, globalDTheight, nDTMB1, SLgap, +0.5)

# And these are used to check if the generated muons fall inside the chamber
MB1f_left  = create_chamber(globalDTwidth, globalDTheight, nDTMB1, SLgap, -0.5, additional_cells = 30)
MB1f_right = create_chamber(globalDTwidth, globalDTheight, nDTMB1, SLgap, +0.5, additional_cells = 30)


#####################
# Define MB2 chambers
# In MB2, SL3 is shifted one cell wrt SL1

# These are used to generate muons
MB2_left  = create_chamber(globalDTwidth, globalDTheight, nDTMB2, SLgap, -1)
MB2_right = create_chamber(globalDTwidth, globalDTheight, nDTMB2, SLgap, +1)

# And these are used to check if the generated muons fall inside the chamber
MB2f_left  = create_chamber(globalDTwidth, globalDTheight, nDTMB2, SLgap, -1, additional_cells = 30)
MB2f_right = create_chamber(globalDTwidth, globalDTheight, nDTMB2, SLgap, +1, additional_cells = 30)


#####################
# Define MB3 chambers
# In MB3, SL1 and SL3 are aligned :)

# This is used to generate muons
MB3  = create_chamber(globalDTwidth, globalDTheight, nDTMB3, SLgap, 0)

# And this is used to check if the generated muons fall inside the chamber
MB3f = create_chamber(globalDTwidth, globalDTheight, nDTMB3, SLgap, 0, additional_cells = 30)

    
#####################
# Define MB4 chambers

# In MB4, SL3 is shifted two cells wrt SL1

# These are used to generate muons
MB4_left   = create_chamber(globalDTwidth, globalDTheight, nDTMB4, SLgap, -2)
MB4        = create_chamber(globalDTwidth, globalDTheight, nDTMB4, SLgap,  0)
MB4_right  = create_chamber(globalDTwidth, globalDTheight, nDTMB4, SLgap, +2)

# And these are used to check if the generated muons fall inside the chamber
MB4f_left  = create_chamber(globalDTwidth, globalDTheight, nDTMB4, SLgap, -2, additional_cells = 30)
MB4f       = create_chamber(globalDTwidth, globalDTheight, nDTMB4, SLgap,  0, additional_cells = 30)
MB4f_right = create_chamber(globalDTwidth, globalDTheight, nDTMB4, SLgap, +2, additional_cells = 30)
