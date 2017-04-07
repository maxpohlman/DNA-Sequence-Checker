# DNA-Sequence-Checker
## By Max Pohlman

This python script will take in one *.fastq file as an argument and return one of the following based on a second argument

* 'repeats' returns number of repeating sequences of the same bases

* 'pairs' returns the number of each pair of bases

* A number between 1 and 100 will return the number of kmers of that length (


A sample fastq is provided. 

This script must be run in a python environment such as Anaconda.

**Examples**
```
python sequence_checker_max.py sample.fastq repeats
python sequence_checker_max.py sample.fastq pairs
python sequence_checker_max.py sample.fastq 5
```
