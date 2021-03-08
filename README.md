# Pattern_Training

  Code for training pseudo-bayes patterns

## How to use the code

1. Create the patterns and save them into a pickle object

       python trainPatterns_forCMSSW.py

- Get the information from the pickle file and creaate a c++ macro to convert it into rootfile:

       python pickleToC.py

- Run the macro to create the final rootfile:

       root -l -b -q createdPatterns_MB.cc