from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish


spec = "G (!q | G (!p | F s))"
variables_names = ["q", "p", "s"]

@b_thread
def pattern():  # done
    """
    Kind: Response: s responds to p
    Scope: After q
    LTL:
        G (!q || G (!p || F s))
    """
    e = yield {waitFor: q}
    if (not e.p) or e.s:
        yield {waitFor: And(p, Not(s))}
    while True:
        yield {waitFor: s, mustFinish: True}
        yield {waitFor: And(p, Not(s))}