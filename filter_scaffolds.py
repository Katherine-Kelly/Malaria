#!/usr/bin/env python3

import sys
import re
short=0
GC=0
with open(sys.argv[1], 'r') as fin, open('filtered.fa', 'w') as fout:
    for line in fin:
        line=line.rstrip()
        if line.startswith('>'):
                if float(line.split()[1].split('=')[1])>3000:
                    short=0
                else:
                    short=1
        else:
            GC=float(len(re.findall('[GCgc]', line))/len(line))
        if GC<0.3 and not short:        # filter out reads <3000 bp and those with GC%>30
            print(line, file=fout)
