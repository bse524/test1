import sys

l1 = ['A','C','G','T']
l2 = ['A','C','G','T']

def mer (l1, l2, n):
    if n == 1:
        return l2

    ltmp = []
    for i in l1:
        for j in l2:
           ltmp.append(i+j) 
    return mer(l1, ltmp, n-1) 

n = int(sys.argv[1])

res = mer(l1, l2, n)
print(res)     

