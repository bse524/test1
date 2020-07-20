import sys

d = {}
with open(sys.argv[1],'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue #continue는 반복문안에서 그 아래에 있는 명령어를 실행하지 않고 다시 반복문의 처음으로 되돌아간다.
        for s in line.strip():
            if s in d:
                d[s] +=1
            else:
                d[s] = 1
print(d) 

total = 0               
for k,v in d.items():
    total += v
print(total)

with open("result.txt", 'w') as handle:
    handle.write(f"A: {d['A']}\n")
    handle.write(f"C: {d['C']}\n")
    handle.write(f"G: {d['G']}\n")
    handle.write(f"T: {d['T']}\n")
  
