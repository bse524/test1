import sys
'''
if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} {txt}")
    sys.exit(1)

f = sys.argv[1]

try:
    with open(f,'r') as handle:
        read = handle.readlines() #리스트로 반환
except FileNotFoundError:
    print(f"{f} not found.. please check..")
    sys.exit()

print(read)
'''

if len(sys.argv) !=2:
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()
try:
    num = int(sys.argv[1])
    print(10/num)
except ValueError:
    print("input not valid")
    sys.exit()
except ZeroDivisionError:
    print("0으로는 못나눠요")
    sys.exit()
