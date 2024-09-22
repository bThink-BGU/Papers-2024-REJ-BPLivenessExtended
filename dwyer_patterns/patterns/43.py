from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish

spec = "G (!q | G (X( !t U (t & F p)) | !(s & X t)))"
variables_names = ["s", "t", "p", "q"]


@b_thread
def pattern():
    """
    Kind: Response Chain: p responds to s,t
    Scope: After q
    LTL:
       G (!q || G (X(!t U (t && F p)) || !(s && XF t)))
    """
    e = yield {waitFor: q}
    should_finish = False
    last_had_s = e.s
    while True:
        e = yield {waitFor: true(), mustFinish: should_finish}
        should_finish = should_finish or (e.t and last_had_s)
        should_finish = not e.p
        last_had_s = e.s