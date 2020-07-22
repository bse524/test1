import sys
import json

def read_tsv(file_name: str) -> list:
    ret = list()
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split("\t")
            else:
                splitted = line.strip().split("\t")
                d = dict(zip(header,splitted))
                ret.append(d)
    return ret

res = read_tsv("read_sample.tsv")
#print(res)

def write_json(l: list, file_name: str) -> None:
    with open (file_name, 'w') as handle:
        json.dump(l, handle, indent =4)

print(write_json(res, 'sample_test3.json'))

def read_json(file_name: str) -> list:
    with open (file_name, 'r') as handle:
        l = json.load(handle)
        return l

if __name__ == "__main__":

    res = read_json("sample_test3.json")
    print(res)
