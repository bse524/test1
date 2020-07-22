seq = "AGTTTATAG"

for i in range(0, len(seq),1):
    if seq[i:i+2] == "TT":
        print(i,i+2, seq[i:i+2])
