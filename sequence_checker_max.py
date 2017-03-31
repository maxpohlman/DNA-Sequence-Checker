#!/usr/bin/python

#Max Pohlman

import sys
f = open(sys.argv[1], 'r')
dna=f.readlines()

def sequence_counter(inputt):
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
                
sequence_counter(dna)