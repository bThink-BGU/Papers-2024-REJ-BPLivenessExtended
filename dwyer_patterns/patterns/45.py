from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish

spec = "G (!q | ((X(!r U (t & F p)) | !(s & X(!r U t))) U (r | G (X(!r U (t & F p)) | !(s & X(!r U t))))))"
variables_names = ["s", "t", "p", "q", "r"]


@b_thread
def pattern():
    """
    Kind: Response Chain: p responds to s,t
    Scope: After q until r
    LTL:
       G (!q || ((X(!r U (t && F p)) || !(s && X(!r U t))) U (r || G (X(!r U (t && F p)) || !(s && X(!r U t))))))
    """
    while True:
        yield {waitFor: And(q, Not(r))}
        should_finish = False
        last_had_s = False
        while True:
            e = yield {waitFor: true(), mustFinish: should_finish}
            should_finish = should_finish or (e.t and last_had_s)
            should_finish = not e.p
            last_had_s = e.s
