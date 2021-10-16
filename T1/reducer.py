#!/usr/bin/env python3

import sys

curr_node = None
op_list = []
fname = sys.argv[1]


if __name__ == "__main__":
    f2 = open(fname, "w")
    for line in sys.stdin:
        line = line.strip()

        incoming, outgoing = line.split('\t', 1)

        try:
            incoming = int(incoming.strip())
            outgoing = int(outgoing.strip())
        except ValueError:
            continue

        if curr_node == incoming:
            if outgoing not in op_list:
                op_list.append(outgoing)
            else:
                continue

        else:
            if curr_node != None:
                print(f"{curr_node}\t{op_list}")
                f2.write(f"{curr_node},1\n")
            curr_node = incoming
            op_list = []
            op_list.append(outgoing)

    if curr_node == incoming:
        print(f"{curr_node}\t{op_list}")
        f2.write(f"{curr_node},1\n")
    f2.close()
