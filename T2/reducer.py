#!/usr/bin/env python3
import sys

curr_node = None
total_contrib = 0

for line in sys.stdin:
    line = line.strip()
    node, contrib = line.split('\t')
    node = int(node)
    contrib = float(node)

    if node == curr_node:
        total_contrib += contrib
    else:
        if curr_node:
            new_rank = round(0.15 + 0.85 * total_contrib, 2)
            # TODO : Write new_rank in

        curr_node = node
        total_contrib = contrib 