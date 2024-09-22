from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish

spec = "(X (t & F p) | ! (s & X t)) U r  | !F r"
variables_names = ["s", "t", "p", "r"]


@b_thread
def pattern():
    """
    Kind: Response Chain: p responds to s,t
    Scope: Before r
    LTL:
       (X (t & F p) | ! (s & X t)) U r  | !F r
    """
    should_finish = False
    last_had_s = False
    while True:
        e = yield {waitFor: true(), mustFinish: should_finish}
        should_finish = should_finish or (e.t and last_had_s)
        if e.r and should_finish:
            yield {waitFor: p, mustFinish: True}
            break
        if e.r and e.s:
            e = yield {waitFor: true()}
            if e.t:
                yield {waitFor: p, mustFinish: True}
            break
        should_finish = not e.p
        last_had_s = e.s