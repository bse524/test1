#seq1="ATGTTATAG"

#S = seq1.lower()
#print(S.replace("a","T").replace("g","C").replace("c","G").replace("t","A"))

import sys 

def comp1(seq: str):
    comp = ""
    for s in seq:
        if s == "A":    
            comp += "T"
        elif s == "C":
            comp += "G"
        elif s == "T":
            comp += "A"
        elif s == "G":
            comp += "C"
    return comp

def comp2(seq: str):
    d_comp = {"A":"T","T":"A","G":"C","G":"C"}
    comp = ""
    for s in seq:
        comp += d_comp[s]
    return comp

if __name__=="__main__": # 현재 스크립트 파일이 실행되는 상태를 보여줌
                         # 프로그램의 시작점일 때만 아래 코드 실행
                         # 외부 파일을 import할 때, if 아래에는 실행 x
    if len(sys.argv) !=2:
        print(f"#usage: python {sys.argv[0]} [string]")
        sys.exit()

    seq = sys.argv[1]
    c1 = comp1(seq)
    c2 = comp2(seq)
    print(seq)
    print(c1)
    print(c2)
