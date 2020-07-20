import sys

if len(sys.argv) !=2: #argument가 2개, 0번은 내꺼-sys.argv[0], 1번자리에 인수(파일)를 붙혀줘라-num, fasta, txt-sys.argv[1]
    print(f"#usage: python {sys.argv[0]}[num]")
    sys.exit()

try:
    num = int(sys.argv[1])
    print(10/num)
except ValueError:
    print("input not valid")
    sys.exit()
except ZeroDivisionError:
    print("0으로 못나눠요")
    sys.exit()

