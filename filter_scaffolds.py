#!/usr/bin/env python3

import sys
count =0
short=0
with open(sys.argv[1], 'r') as fin, open('filtered.fa', 'w') as fout:
    for line in fin:
        line=line.rstrip()
        if line.startswith('>'):
                if float(line.split()[1].split('=')[1])>3000:
                    short=0
                else:
                    short=1
        if not short:
            print(line, file=fout)
