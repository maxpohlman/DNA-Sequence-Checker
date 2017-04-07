#!/usr/bin/python

#Max Pohlman

import sys
import math
f = open(sys.argv[1], 'r')
dna=f.readlines()

def sequence_counter(inputt, lenn):
    output = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]] #defines output matrix
    mylets = ['A','C','G','T'] #defines input letters for loop
    for line_num,line in enumerate(inputt): #looks at each line 
        if line_num % 4 ==1: #if line number is divisible by 4, we can do analysis
            i=0 #sets initial location for char string
            while i < len(line): #i use while instead of enumerate because it's what I'm used to
                for let in mylets: #loops through the letters
                    if (line[i] == let and line[i+1] == let): #checks if there's a match between current spot and next spot
                        lchk=1 #sets counter for how long the sequence will be
                        while line[i+lchk] ==let: #while the next character checked is a match
                            lchk+=1 #increase the checking range until no match
                        output[mylets.index(let)][lchk-2]+=1 #adds a count to the correct sequence length spot in the output matrix (row = letter, column = length)
                        i = i + lchk # increases the location to after the sequence (used to prevent counting a 5 chain as a 4,3,2 chain as well)
                i+=1 #if there are no matches, just move up one slot

    #This section just prints output, nothing really fancy.                
    for i in range(4):
        if i == 0:
            for j in range(7):
                print('There were', output[i][j], 'counts of', j+2, 'back-to-back As.')
        if i == 1:
            for j in range(7):
                print('There were', output[i][j], 'counts of', j+2, 'back-to-back Cs.')
        if i == 2:
            for j in range(7):
                print('There were', output[i][j], 'counts of', j+2, 'back-to-back Gs.')
        if i == 3:
            for j in range(7):
                print('There were', output[i][j], 'counts of', j+2, 'back-to-back Ts.')

				
def pair_checker(inputt):
	output = {'AA':0,'AC':0,'AG':0,'AT':0,'CA':0,'CC':0,'CG':0,'CT':0,'GA':0,'GC':0,'GG':0,'GT':0,'TA':0,'TC':0,'TG':0,'TT':0}			
	mylets = ['AA','AC','AG','AT','CA','CC','CG','CT','GA','GC','GG','GT','TA','TC','TG','TT']
	for line_num,line in enumerate(inputt): #looks at each line 
		if line_num % 4 ==1: #if line number is divisible by 4, we can do analysis
			i=0 #sets initial location for char string
			while i < len(line): #i use while instead of enumerate because it's what I'm used to	
				for let in mylets: #loops through the pairs
					if line[i:i+2] == let : #checks if there's a match between the two pairs
						output[let]+=1 #adds to the correct bin
						i = i + 1 # moves up the window
				i=i+1 #moves up the window
	print(output)

def sequence_length(inputt, ll):
	output = 0
	for line_num,line in enumerate(inputt): #looks at each line 
		if line_num % 4 ==1: #if line number is divisible by 4, we can do analysis
			kmer = len(line) - ll + 1 #counts number of each kmer
			output = output + kmer #adds to total
	print('There are', output, 'kmers of length', ll)

sarg = sys.argv[2]

	
if sarg == 'repeats':
	sequence_counter(dna)
if sarg =='pairs':
	pair_checker(dna)
if len(sarg) < 5:
	ll = int(sarg)
	sequence_length(dna, ll)
	
	
