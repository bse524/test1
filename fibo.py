import sys

def fibo(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2) #리턴이 되면서 함수로 다시 호출

n = int(sys.argv[1])

print(fibo(n))
         
