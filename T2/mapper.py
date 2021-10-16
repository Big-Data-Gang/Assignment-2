#!/usr/bin/env python3
import math
import sys
import json

# Function to calculate similarity
def similarity(v1, v2):
    dot_prod = 0
    mod_v1 = 0
    mod_v2 = 0

    for i in range(len(v1)):
        dot_prod += v1[i] * v2[i]
        mod_v1 += math.pow(v1[i], 2)
        mod_v2 += math.pow(v2[i], 2)

    mod_v1 = math.sqrt(mod_v1)
    mod_v2 = math.sqrt(mod_v2)

    ans = dot_prod / (mod_v1 * mod_v2)

    return round(ans, 2)    


# Function to create similarity matrix
def construct_sim(embeds):

    sims = list()

    for i in sorted(embeds):
        s = list()

        for j in sorted(embeds):
            s.append(similarity(embeds[i], embeds[j]))
        
        sims.append(s)

    return sims

# Getting arguments for the various files
v_path = sys.argv[1]
embed_path = sys.argv[2]

# Loading V data into memory
v_file = open(v_path, 'r')
v = dict()
for line in v_file.readlines():
    key, value = line.strip().split(',')
    v[key] = int(value)

# Loading page embeddings
embed_file = open(embed_path, 'r') 
embeds = json.load(embed_file)


# Function to create similarity matrix
sim_matrix = construct_sim(embeds)
print(sim_matrix)


# for line in sys.stdin:
#     line = line.strip()
#     node, outlinks = line.split(' ', 1)
#     try:
#         # Converting to int
#         node = int(node)
        
#         # Removing square brackets from string
#         outlinks = outlinks[1:-1].split(',')

#         # Converting to int
#         outlinks = [int(i) for i in outlinks]
#     except ValueError:
#         print('Error1') 
#         exit()
    
#     for outlink in outlinks:
#         # Calculate initial contribution
#         init_contrib = v[node]/len(outlinks)

#         if node == outlink:
#             sim = 1
#         else:
#             sim =  sims[min(node, outlink)][max(node, outlink)]

#         tot_contrib = init_contrib * sim
#         print(outlink, tot_contrib)
    


       