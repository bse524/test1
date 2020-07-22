seq1 = "ATGTTATAG"

#print(seq1[0:3])
#print(seq1[3:6])
#print(seq1[6:9])


for i in range(0, len(seq1),3):
    print(i, i+3, seq1[i:i+3])
