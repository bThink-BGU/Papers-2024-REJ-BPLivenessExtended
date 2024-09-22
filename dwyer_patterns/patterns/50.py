from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish

spec = "G (!q | ((!p | (!r U (!r & s & X(!r U t)))) U (r | G (!p | (s & X(F t))))))"
variables_names = ["s", "t", "p", "q", "r"]

@b_thread
def pattern():
    """
    Kind: Response Chain: s,t responds to p
    Scope: After q until r
    LTL:
       G (!q || ((!p || (!r U (!r && s && X(!r U t)))) U (r || G (!p || (s && XF t)))))
    """
    while True:
        e = yield {waitFor: q}
        if not e.p:
            e = yield {waitFor: p}
        while True:
            yield {waitFor: s, mustFinish: True}
            while True:
                e = yield {waitFor: true(), block: Not(t), mustFinish: True}
                if not e.s:
                    break