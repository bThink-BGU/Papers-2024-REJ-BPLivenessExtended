from radon.visitors import ComplexityVisitor
from radon.raw import analyze
import os


code_dir = "task_3_suggested_w.py"
complexity, loc , lloc, sloc = 0, 0, 0, 0
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
print(complexity, sloc)