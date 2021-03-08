# Pattern Training

  Code for training pseudo-bayes patterns

## How to use the code

1. Create the patterns and save them into a pickle object

       python trainPatterns_forCMSSW.py
       python trainPatterns_forCMSSW.py MB4

2. Get the information from the pickle file and creaate a c++ macro to convert it into rootfile:

       python pickleToC.py MB
       python pickleToC.py MB4

3. Run the macro to create the final rootfile:

       root -l -b -q createdPatterns_MB.cc
       root -l -b -q createdPatterns_MB4.cc
