import os
import re

group = "B"
task = "2"

dir = "/Users/tomyaacov/Google Drive/My Drive/research/liveness extended/results/tasks/" + group

with open("groups/" + group + ".csv", "r") as f:
    for _id in f:
        l = os.listdir(dir + "/" + _id.strip())
        l = [x for x in l if "task"+task in x]
        if len(l) == 0:
            print("-")
        else:
            code_dir = dir + "/" + _id.strip() + "/" + l[0]
            with open(code_dir, "r") as f2:
                code = f2.read()
                if re.search('must', code, re.IGNORECASE):
                    if re.search('mustf', code, re.IGNORECASE):
                        print("yes")
                    else:
                        print(_id.strip(), "?")
                else:
                    print("no")

