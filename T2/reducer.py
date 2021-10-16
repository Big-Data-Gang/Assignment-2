#!/usr/bin/env python3
import sys

curr_node = None
total_contrib = 0

for line in sys.stdin:
    line = line.strip()
    node, contrib = line.split('\t')
    # Convert node and contrib to float
    node = int(node)
    contrib = float(contrib)

    # If current node is same as previous node
    if node == curr_node:
        total_contrib += contrib
    else:
        # If there is a current node
        if curr_node:
            new_rank = round(0.15 + 0.85 * total_contrib, 2)
            print(f"{curr_node},{new_rank}")

        curr_node = node
        total_contrib = contrib 

if curr_node == node:
    new_rank = round(0.15 + 0.85 * total_contrib, 2)
    print(f"{curr_node},{new_rank}")