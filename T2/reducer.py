#!/usr/bin/env python3
import sys
import json

for line in sys.stdin:
    line = line.strip()
    node, contribs = line.split('\t')
    contribs = json.loads(contribs)
    print(contribs, type(contribs))