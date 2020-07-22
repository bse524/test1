import sys
import gzip

if len(sys.argv) !=2:
    print(f"#usage: python {sys.argv[0]} [fasta.gz]")
    sys.exit()

f = sys.argv[1]
d= {}
with gzip.open(f,'rb') as handle:
    for line in handle:
        line = line.decode("utf-8").strip() #bite개체가 str개체로 변환
        if line.startswith(">"):
            continue
        for s in line:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
with open("result1.txt",'w') as handle:
    handle.write(f"A: {d['A']}\n")
    handle.write(f"C: {d['C']}\n")
    handle.write(f"G: {d['G']}\n")
    handle.write(f"T: {d['T']}\n")

    
