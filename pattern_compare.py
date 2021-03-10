import sys, os

# Input variable
if len(sys.argv) < 3:
    print("Please tell me which patterns txt file you want to compare")
    print("")
    print("python pattern_compare.py pattern1.txt pattern2.txt")
    print("")
    print("python pattern_compare.py createdPatterns_MB.txt PseudoBayesPatterns_uncorrelated_v0.txt")
    print("python pattern_compare.py createdPatterns_MB.txt MBTrainTraining_uncorrelated.txt")
    print("python pattern_compare.py PseudoBayesPatterns_uncorrelated_v0.txt MBTrainTraining_uncorrelated.txt")
    sys.exit()

f1_name = sys.argv[1]    
f1 = open(f1_name, "r")
lines1 = []

f2_name = sys.argv[2]    
f2 = open(f2_name, "r")
lines2 = []

for l1 in f1:
    lines1.append(l1)

for l2 in f2:
    lines2.append(l2)

for i in range(0, len(lines1)):
    if (lines1[i] != lines2[i]):
        print(i)
        print("{}{}".format(lines1[i], lines2[i]))
        print()
    
f1.close() 
f2.close() 
