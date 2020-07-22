import sys

class FASTQ:
    def __init__ (self, file_name: str):
        self.file_name=file_name
        self.read_num=0
        self.base = {}
        self.length = 0
    def count_read_num (self):
        cnt = 0
        with open (self.file_name, 'r') as handle:
            for line in handle:
                if cnt % 4 == 0:
                    header = line.strip()
                    self.read_num += 1
                elif cnt % 4 == 1:
                    seq = line.strip()
                    for s in seq:
                        if s in self.base:
                            self.base[s] += 1
                        else:
                            self.base[s] = 1
                elif cnt % 4 == 3:
                    qual = line.strip()
                cnt += 1
    def length_seq(self):
        for k,v in self.base.items():
            self.length += v

file_name = sys.argv[1]
f1 = FASTQ(file_name)
f1.count_read_num()
print(f1.read_num) 
print(f1.base)

f1.length_seq()
print(f1.length)

