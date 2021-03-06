import sys

class FASTA:
    def __init__ (self, file_name: str):
        self.file_name = file_name
        self.count = {}
        self.length = 0
    def count_base(self):
        with open (file_name, 'r') as handle:
            for line in handle:
                if line.startswith(">"):
                    continue
                for s in line.strip():
                    if s in self.count:
                        self.count[s] += 1
                    else:
                        self.count[s] = 1
    def get_length(self):
        for k,v in self.count.items():
            self.length += v

file_name = sys.argv[1]
f1 = FASTA(file_name)
f1.count_base()
f1.get_length()
print(f1.count)
print(f1.length)
                
