from Bio import SeqIO 

record = SeqIO.read("059.fasta","fasta") #read: 1개의 header 가짐

A = record.seq.count("A") #record.seq:하나의 객체, 문자열과 동일
C = record.seq.count("C")
G = record.seq.count("G")
T = record.seq.count("T")

print(f"A: {A}")
print(f"C: {C}")
print(f"G: {G}")
print(f"T: {T}")



