This is the code written in a pynb for training a deep neural network for binary Malware Classification. 
The dataset used is EMBER 2017 version 2. EMBER stands for Endgame Malware Benchmark for Research which is a large dataset composed
of labeled and unlabeled samples of parsed features of PE header files from binaries under 2MB. Extracting and vectorizing features of these samples can be done through project LIEF's library which is bundled at the EMBER's GitHub.

More information about them can be found on their GitHub:
https://github.com/endgameinc/ember/tree/master/malconv

The midterm is composed of three tasks: Making a deep neural network, deploying it to the cloud via Amazon SagaMaker, and creating a script
for say a client to use to determine a single PE file (under 2MB) is malicious or benign. In this repository, putty.exe is used as the
sample.

Task 1: Completed. Can be found under midterm-nanci.pynb. The training pynb is as it sounds, it's the notebook full of hyperparameter tweaks and longer epochs.

Task 2: Completed. Needed to be implemented for Task 3.

Task 3: Completed. Can be found in the subfolder midterm files.

Youtube video presentation can be found here:
https://youtu.be/QyhNCxZWde0
