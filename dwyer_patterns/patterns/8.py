from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish


spec = "G !q | F (q & F p)"
variables_names = ["q", "p"]

@b_thread
def pattern():  # done
    """
    Kind: Existence: p becomes true
    Scope: After q
    LTL:
        G !q || F (q && F p)
    """
    yield {waitFor: And(q, Not(p))}
    yield {waitFor: p, mustFinish: True}