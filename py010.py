'''
def mySum(n1, n2):
    print(n1+n2)

mySum(2,3)
mySum(5,7)
mySum(10,15)
'''


def mySum(n1: int, n2:int)->None: #return값이 없다는 것을 주석처럼 표현
    print(f"{n1}+{n2}={n1+n2}") #간단하게 포맷팅해주는 것?

res1 = mySum(2,3)
res2 = mySum(5,7)
res3 = mySum(10,15)

print(res1)
print(res2)
print(res3)


def mySum(n1: int, n2:int)->None:
    print(f"{n1}+{n2}={n1+n2}")
    return n1+n2

res1 = mySum(2,3)
res2 = mySum(5,7)
res3 = mySum(10,15)

print(res1)
print(res2)
print(res3)
