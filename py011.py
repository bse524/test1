'''
def Fact():
    result = 1
    n = 5

    while n > 0:
        result *= n
        n -= 1
    return result

result = Fact()
print(result)
'''

A = int(input("숫자를 입력하세요: "))

def Fact(A):
    result = 1
    n = A
 
    while n > 0:
        result *= n
        n -= 1
    return result

result = Fact(A)
print(result)



