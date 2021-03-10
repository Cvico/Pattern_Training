# Pattern Training

  Code for training pseudo-bayes patterns

## How to use the code

1. Create the patterns and save them into a pickle object

       python trainPatterns_forCMSSW.py MB
       python trainPatterns_forCMSSW.py MB4

2. Get the information from the pickle file and creaate a c++ macro to convert it into rootfile:

       python pickleToC.py MB
       python pickleToC.py MB4

3. Run the macro to create the final rootfile:

       root -l -b -q createdPatterns_MB.cc
       root -l -b -q createdPatterns_MB4.cc

4. To dump the content of the created rootfile into a txt:

       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB.root")' > createdPatterns_MB.txt
       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB4.root")' > createdPatterns_MB4.txt

5. To compare two patterns txt files:

       python pattern_compare.py createdPatterns_MB.txt PseudoBayesPatterns_uncorrelated_v0.txt > comparison.txt


## For debugging:

       python trainPatterns_forCMSSW_Carlos.py
       python pickleToC.py Carlos
       root -l -b -q MBTrainTraining_uncorrelated.cc

