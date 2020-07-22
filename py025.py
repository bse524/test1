seq1='ATGTTATAG'

#print(seq1[::3])

S = len(seq1)
for i in range(0,S,3):
    print(i, seq1[i])  
