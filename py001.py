#! /usr/bin/python
#-*-coding: utf-8-*-
#-*-coding: euc-kr-*-
'''
import sys

f = sys.argv[1]

with open(f,'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        print(line.strip())
'''

import sys

if len(sys.argv) != 2:
    print(f"#usage:python {sys.argv[0]} [fasta]")
    sys. exit()

f = sys.argv[1]
d = {}

with open(f,'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for s in line.strip():
            if s in d:
                d[s] += 1 
            else:
                d[s] = 1
    
print(d)
total = 0
for k,v in d.items(): #key, values
    total += v  #전체 values 값 구하기
print(total)

with open("result.txt",'w') as handle:
    handle.write(f"A: {d['A']}\n")
    handle.write(f"C: {d['C']}\n")
    handle.write(f"G: {d['G']}\n")
    handle.write(f"T: {d['T']}\n")



