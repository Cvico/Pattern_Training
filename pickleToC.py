import sys, os
import pickle
# import ROOT

# Input variable
if len(sys.argv) < 2:
    print("Please tell me which MB patterns you want extract: MB or MB4")
    print("")
    print("python pickleToC.py MB")
    print("python pickleToC.py MB4")
    print("python pickleToC.py Carlos")
    sys.exit()

MB_input = sys.argv[1]
print("MB to use: " + MB_input)

if MB_input == "MB":
    input_file_name  = "trainedPatterns_MB.pck"
    output_file_name = "createdPatterns_MB"
elif MB_input == "MB4": 
    input_file_name  = "trainedPatterns_MB4.pck"
    output_file_name = "createdPatterns_MB4"
elif MB_input == "Carlos":
    input_file_name  = "MBTrainTraining_uncorrelated.pck"
    output_file_name = "MBTrainTraining_uncorrelated"
else:
    raise ValueError("Input must be 'MB' or 'MB4'")


print("Loading pickle")
patterns = pickle.load(open(input_file_name,"rb"))
print("Creating patterns")


class Pattern(object):
    def __init__(self, seeds, hits):
        self.seeds = seeds
        self.hits  = hits
        self.len   = len(hits)
        self.busted = False

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


# Pattern structure:
# Seed: (lower_seed_layer, upper_seed_layer, upper_cell_number - lower_cell_number)
# Then, for each of the eight layers:
# (layer_number, cell_number - lower_seed_cell_number, laterality)
# Where laterality: {left: -1, right: 1, unknown: 0}

f = open(output_file_name + ".cc", "w")
i = 0

# Writing header
f.write('#include "TFile.h"\n')
f.write('#include <vector>\n')
f.write("\n")
f.write('int ' + output_file_name + '() {\n')
f.write("\n")
f.write('gInterpreter->GenerateDictionary("vector<vector<vector<int>>>", "vector");\n')
f.write("\n")
f.write('TFile* f = new TFile("{}.root", "RECREATE");\n'.format(output_file_name))
f.write("\n")
f.write("std::vector<std::vector<std::vector<int>>> allPatterns;\n")
f.write("\n")

# Writing patterns
for p in patterns:
    i += 1
    print(i, len(patterns))
    f.write("std::vector<std::vector<int>> pattern_"+str(i) +" = {std::vector<int> {" + str(p.seeds[0])+", "+str(p.seeds[1])+ ", " + str(p.seeds[2]) + "}, std::vector<int> {" + "}, std::vector<int>{ ".join([", ".join([str(int(i)) for i in p.hits[j][:]]) for j in range(len(p.hits)) ])+ "}};\n")
    f.write("allPatterns.push_back(pattern_{});\n".format(i))
    f.write("\n")
    print(p.seeds, p.hits)

# Closing lines
f.write('f->cd();\n')
f.write('f->WriteObject(&allPatterns, "allPatterns");\n')
f.write('f->Close();\n')
f.write('return 0;\n')
f.write('}\n')
    
f.close()
