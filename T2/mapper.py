#!/usr/bin/env python3
import math
import sys

# TODO : Import the v file and page embeddings file into memory
# Placeholder below (Pick the appropriate DS)
# v = [1, 1, 1, 1]  List DS
v = {1:1, 2:1, 3:1, 4:1} # Dict DS

# TODO : Create dictionary of similarities from page embeddings
# Placeholder below
sims = {    1: {2: 0.95, 3: 0.96, 4: 0.98},
            2: {3: 0.98, 4: 0.93},
            3: {4: 0.91} 
    }   

# print(sims)

for line in sys.stdin:
    line = line.strip()
    node, outlinks = line.split(' ', 1)
    try:
        node = int(node)
        # print(node)
        outlinks = outlinks[1:-1].split(',')
        # print(outlinks)
        outlinks = [int(i) for i in outlinks]
    except ValueError:
        print('Error1') 
        exit()
    
    # print(node, outlinks)
    for outlink in outlinks:
        # Change this based on DS used for v
        init_contrib = v[node]/len(outlinks)

        if node == outlink:
            sim = 1
        else:
            sim =  sims[min(node, outlink)][max(node, outlink)]

        tot_contrib = init_contrib * sim
        print(outlink, tot_contrib)
    


       