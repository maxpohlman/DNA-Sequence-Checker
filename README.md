# DNA-Sequence-Checker
## By Max Pohlman

This python script will take in one *.fastq file as an argument and return the number of sequences of repeating nucleobases. 
The script will only count maximum lengths, meaning that a sequence of 5 is not also counted as a sequence of 4, 3, and 2.
A sample fastq is provided. 
This script must be run in a python environment such as Anaconda.

**Example**
    python sequence_checker_max.py sample.fastq
