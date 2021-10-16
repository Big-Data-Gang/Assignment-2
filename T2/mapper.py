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

    return ans    

# Check for inverse entry
def inverse(sims, i, j):
    if j in sims:
        if i in sims[j]:
            return True
    return False


# Function to create similarity matrix
def construct_sim(embeds):

    sims = dict()

    for i in embeds.keys():
        s = dict()

        for j in embeds.keys():
            if inverse(sims, i, j):
                pass
            else:
                s[j] = similarity(embeds[i], embeds[j])

        sims[i] = s

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

for line in sys.stdin:
    line = line.strip()
    node, outlinks = line.split('\t', 1)
    try:
        # Converting to int
        node = int(node)
        
        # Removing square brackets from stri`ng
        outlinks = outlinks[1:-1].split(',')

        # Converting to int
        outlinks = [int(i) for i in outlinks]
    except ValueError:
        print('Error1') 
        exit()
    
    # Calculating initial contributions
    init_contrib = v[str(node)]/len(outlinks)

    for outlink in outlinks:
        # If self loop
        if node == outlink:
            sim = 1
        else:
            # Get similarity between node and outlink
            #print(node, outlink)
            try:
                sim =  sim_matrix[str(min(node, outlink))][str(max(node, outlink))]
            except:
                sim =  sim_matrix[str(max(node, outlink))][str(min(node, outlink))]
        # Calculate C value for (node, outlook) combination
        tot_contrib = init_contrib * sim
        # Print outlink and contribution to outlink
        print(outlink, tot_contrib, sep = '\t')

       