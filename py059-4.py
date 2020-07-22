import sys

class FASTQ:
    def __init__ (self, file_name: str):
        self.file_name=file_name
        self.read_num=0
        self.seq = ''
    def count_read_num (self):
        cnt = 0
        with open (self.file_name, 'r') as handle:
            for line in handle:
                if cnt % 4 == 0:
                    header = line.strip()
                    self.read_num += 1
                elif cnt % 4 == 1:
                    seq = line.strip()
                    self.seq += line.strip()
                elif cnt % 4 == 3:
                    qual = line.strip()
                cnt += 1
    def length_seq(self):
        return(len(self.seq))

file_name = sys.argv[1]
f1 = FASTQ(file_name)
f1.count_read_num()
print(f1.read_num) 

res = f1.length_seq()
print(res)
