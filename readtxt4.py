import sys

def readtxt(file_name: str)-> str:
    ret = ""
    with open (file_name, 'r') as handle:
        for line in handle:
           if line.startswith(">"):
               continue
           else:
               ret += line.strip()
        return ret

res = readtxt ("read_sample.txt")
print(res)

'''
f = sys.argv[1]

res = readtxt(f)
print(res)
'''
