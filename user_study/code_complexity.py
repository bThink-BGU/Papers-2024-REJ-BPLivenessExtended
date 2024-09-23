from radon.visitors import ComplexityVisitor
from radon.raw import analyze
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--group", default="A")
parser.add_argument("--task", default="1")

args = parser.parse_args()


group = args.group
task = args.task

dir = "results/tasks/" + group

with open("groups/" + group + ".csv", "r") as f:
    for _id in f:
        l = os.listdir(dir + "/" + _id.strip())
        l = [x for x in l if "task"+task in x]
        if len(l) == 0:
            print("-")
        else:
            complexity, loc , lloc, sloc = 0, 0, 0, 0
            code_dir = dir + "/" + _id.strip() + "/" + l[0]
            with open(code_dir, "r") as f2:
                code = f2.read()
                v = ComplexityVisitor.from_code(code)
                for func in v.functions:
                    func_code = "\n".join(code.split("\n")[func.lineno - 1:func.endline])
                    res = analyze(func_code)
                    complexity = max(complexity, func.complexity)
                    loc = max(loc, res.loc)
                    lloc = max(lloc, res.lloc)
                    sloc = max(sloc, res.sloc)
            print(_id.strip(), complexity, loc, lloc, sloc)




