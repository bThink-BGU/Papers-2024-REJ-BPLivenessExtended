from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish

spec = "G (!q || ((!p || (!r U (!r & s && !z & X((!r & !z) U t)))) U (r || G (!p || (s & !z & X(!z U t))))))"
variables_names = ["s", "t", "z", "p", "q", "r"]


@b_thread
def pattern():
    """
    Kind: Constrained Chain: s,t without z responds to p
    Scope: After q until r
    LTL:
       G (!q || ((!p || (!r U (!r && s && !z && X((!r && !z) U t)))) U (r || G (!p || (s && !z && X(!z U t))))))
    """
    mf = False
    while True:
        yield {waitFor: p, mustFinish: mf}
        e = yield {waitFor: Or(s, p), block: z, mustFinish: True}
        if e.p:
            mf = True
            continue
        e = yield {waitFor: Or(t, p), block: z, mustFinish: True}
        if e.p:
            mf = True