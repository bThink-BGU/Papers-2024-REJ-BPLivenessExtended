from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish


spec = "G (!(q & !r) | (!r U (p & !r)))"
variables_names = ["q", "p", "r"]

@b_thread
def pattern():  # done
    """
    Kind: Existence: p becomes true
    Scope: After q until r
    LTL:
        G (!(q && !r) || (!r U (p && !r)))
    """
    while True:
        yield {waitFor: And(Not(p), q, Not(r))}
        yield {waitFor: p, block: r, mustFinish: True}