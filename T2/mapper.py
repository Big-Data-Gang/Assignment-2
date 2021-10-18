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
    try:
        ans = dot_prod / (mod_v1 * mod_v2)
        # wrong file gave denominator as zero
    except:
        return 0
    return ans    

def main():
    # Getting arguments for the various files
    v_path = sys.argv[1]
    embed_path = sys.argv[2]

    # Loading V data into memory
    v_file = open(v_path, 'r')
    v = dict()
    for line in v_file.readlines():
        key, value = line.strip().split(',')
        v[key] = float(value)

    # Loading page embeddings
    embed_file = open(embed_path, 'r') 
    embeds = json.load(embed_file)

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
            continue
        
        # Print 0 for each source node as well (To handle page rank calculation for nodes with no incoming links)
        print(node, 0, sep = '\t')

        # Calculating initial contributions
        init_contrib = v[str(node)]/len(outlinks)

        for outlink in outlinks:
            # If self loop
            if node == outlink:
                sim = 1
            else:
                # Get similarity between node and outlink
                sim = similarity(embeds[str(node)], embeds[str(outlink)])
                
            # Calculate C value for (node, outlook) combination
            tot_contrib = init_contrib * sim
            # Print outlink and contribution to outlink
            print(outlink, tot_contrib, sep = '\t')

if __name__ == '__main__':
    main()

       