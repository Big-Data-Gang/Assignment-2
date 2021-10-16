#!/usr/bin/env python3
import sys
import json

c = dict()

for line in sys.stdin:
    line = line.strip()
    node, contribs = line.split('\t')

    # Replacing ' with " to convert into json friendly format
    contribs = contribs.replace("\'", "\"")
    contribs = json.loads(contribs)
    
    for node in contribs:
        if node not in c:
            c[node] = contribs[node]
        else:
            c[node] += contribs[node]

# Convert to final contribs

for node in c:
    c[node] = 0.15 + 0.85 * c[node]

for i in sorted(c):
    print(i, round(c[i], 2))