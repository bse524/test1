import sys

def read_csv(file_name: str) -> list:
    ret = list()
    with open (file_name, 'r') as handle:
        for line in handle: 
            if line.startswith ("#"):
                header = line.strip().split(",")
            else:
                splitted = line.strip().split(",")
                d = dict(zip(header,splitted))
                ret.append(d)

        return ret

res = read_csv("read_sample.csv")
print(res) 
