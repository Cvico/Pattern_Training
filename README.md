# Pattern Training

  Code for training pseudo-bayes patterns

## How to use the code

1. Create the patterns and save them into a pickle object

       python trainPatterns_forCMSSW.py MB1_left
       python trainPatterns_forCMSSW.py MB1_right
       python trainPatterns_forCMSSW.py MB2_left 
       python trainPatterns_forCMSSW.py MB2_right
       python trainPatterns_forCMSSW.py MB3
       python trainPatterns_forCMSSW.py MB4_left 
       python trainPatterns_forCMSSW.py MB4
       python trainPatterns_forCMSSW.py MB4_right

2. Get the information from the pickle file and creaate a c++ macro to convert it into rootfile:

       python pickleToC.py MB1_left
       python pickleToC.py MB1_right
       python pickleToC.py MB2_left 
       python pickleToC.py MB2_right
       python pickleToC.py MB3
       python pickleToC.py MB4_left 
       python pickleToC.py MB4
       python pickleToC.py MB4_right

3. Run the macro to create the final rootfile:

       root -l -b -q createdPatterns_MB1_left.cc
       root -l -b -q createdPatterns_MB1_right.cc
       root -l -b -q createdPatterns_MB2_left.cc 
       root -l -b -q createdPatterns_MB2_right.cc
       root -l -b -q createdPatterns_MB3.cc
       root -l -b -q createdPatterns_MB4_left.cc 
       root -l -b -q createdPatterns_MB4.cc
       root -l -b -q createdPatterns_MB4_right.cc

4. To dump the content of the created rootfile into a txt:

       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB1_left.root")'  > createdPatterns_MB1_left.txt
       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB1_right.root")' > createdPatterns_MB1_right.txt
       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB2_left.root")'  > createdPatterns_MB2_left.txt 
       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB2_right.root")' > createdPatterns_MB2_right.txt
       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB3.root")'       > createdPatterns_MB3.txt
       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB4_left.root")'  > createdPatterns_MB4_left.txt 
       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB4.root")'       > createdPatterns_MB4.txt
       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB4_right.root")' > createdPatterns_MB4_right.txt


5. To compare two patterns txt files:

       python pattern_compare.py createdPatterns_MB1.txt createdPatterns_MB2.txt > comparison.txt

## All training steps

MB1_left:

       python trainPatterns_forCMSSW.py MB1_left
       python pickleToC.py MB1_left
       root -l -b -q createdPatterns_MB1_left.cc
       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB1_left.root")' > createdPatterns_MB1_left.txt

MB1_right:

       python trainPatterns_forCMSSW.py MB1_right
       python pickleToC.py MB1_right
       root -l -b -q createdPatterns_MB1_right.cc
       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB1_right.root")' > createdPatterns_MB1_right.txt

MB2_left:

       python trainPatterns_forCMSSW.py MB2_left
       python pickleToC.py MB2_left
       root -l -b -q createdPatterns_MB2_left.cc
       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB2_left.root")' > createdPatterns_MB2_left.txt

MB2_right:

       python trainPatterns_forCMSSW.py MB2_right
       python pickleToC.py MB2_right
       root -l -b -q createdPatterns_MB2_right.cc
       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB2_right.root")' > createdPatterns_MB2_right.txt

MB3:

       python trainPatterns_forCMSSW.py MB3
       python pickleToC.py MB3
       root -l -b -q createdPatterns_MB3.cc
       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB3.root")' > createdPatterns_MB3.txt


MB4_left:

       python trainPatterns_forCMSSW.py MB4_left
       python pickleToC.py MB4_left
       root -l -b -q createdPatterns_MB4_left.cc
       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB4_left.root")' > createdPatterns_MB4_left.txt

MB4:

       python trainPatterns_forCMSSW.py MB4
       python pickleToC.py MB4
       root -l -b -q createdPatterns_MB4.cc
       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB4.root")' > createdPatterns_MB4.txt

MB4_right:

       python trainPatterns_forCMSSW.py MB4_right
       python pickleToC.py MB4_right
       root -l -b -q createdPatterns_MB4_right.cc
       root -l -b -q 'pattern_dumper.cc("createdPatterns_MB4_right.root")' > createdPatterns_MB4_right.txt



## For debugging:

       python trainPatterns_forCMSSW_Carlos.py
       python pickleToC.py Carlos
       root -l -b -q MBTrainTraining_uncorrelated.cc

