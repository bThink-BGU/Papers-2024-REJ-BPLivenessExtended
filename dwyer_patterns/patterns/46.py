from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish


spec = "G (!p | F (s & X t))"
variables_names = ["p", "s", "t", "d"]

@b_thread
def pattern():
    """
    Kind: Response Chain: s,t responds to p
    Scope: Globally
    LTL:
       G (!p || F (s && XF t))
    """
    while True:
        yield {waitFor: p}
        while True:
            e = yield {waitFor: true(), mustFinish: True}
            if e in non_det:
                break
        yield {block: Not(s), waitFor: true(), mustFinish: True}
        yield {block: Not(t), waitFor: true(), mustFinish: True}