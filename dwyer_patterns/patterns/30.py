from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish

spec = "G (!(q & !r) | (r V (!p | r | (!r U (!r & s)))))"
variables_names = ["q", "p", "r", "s"]

@b_thread
def pattern():  # done
    """
    Kind: Response: s responds to p
    Scope: After q until r
    LTL:
        G (!(q && !r) || (r V (!p || r || (!r U (!r && s)))))
    """
    while True:
        e = yield {waitFor: And(q, Not(r))}
        if (not e.p) or e.s:
            e = yield {waitFor: Or(r, And(p, Not(s)))}
        while not e.r:
            yield {waitFor: s, block: r, mustFinish: True}
            e = yield {waitFor: Or(r, And(p, Not(s)))}