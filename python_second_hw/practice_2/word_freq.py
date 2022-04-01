#!/usr/bin/python

import sys

# get filename `*.txt`
filename=str(sys.argv[1])
# get number to display
n = int(sys.argv[2])
# read file
file = open(filename,"r")
# make dictionary
D = {}
# by line
while True:
    line = file.readline()
    if not line:
        break
    line = line.strip()
    line = line.split(' ')
    for i in range(len(line)):
        if line[i] in D:
            D[line[i]] += 1
        else:
            D[line[i]] = 1
# check for top words
D_sort = dict(sorted(D.items(), key = lambda D: D[1], reverse = True))
# print the result
cnt = 0
for key , value in D_sort.items():
    cnt+=1
    print("{:10}{:>10}".format(key,value))
    if cnt == n: 
        break
    