seq1 = "ATGTTATAG"

d_comp = {"A":"T","G":"C","C":"G","T":"A"}
comp=""
for i in seq1:
    comp += d_comp[i]
print(seq1)
print(comp)

S = seq1.lower()

A= S.replace("a","T").replace("g","C").replace("c","G").replace("t","A")
print(A)
