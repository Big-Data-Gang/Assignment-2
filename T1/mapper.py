#!/usr/bin/env python3

import sys
if __name__ == "__main__":
    for line in sys.stdin:
        incoming, outgoing = line.split('\t', 1)
        try:
            incoming = int(incoming)
            outgoing = int(outgoing)
        except ValueError:
            continue
        line = f"{incoming}\t{outgoing}"
        print(line)
