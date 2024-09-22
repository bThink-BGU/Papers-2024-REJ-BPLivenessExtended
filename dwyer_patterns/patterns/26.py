from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish


spec = "G (!p | F s)"
variables_names = ["p", "s"]

@b_thread
def pattern():  # done
    """
    Kind: Response: s responds to p
    Scope: Globally
    LTL:
        G (!p || F s)
    """
    while True:
        yield {waitFor: And(p, Not(s))}
        yield {waitFor: s, mustFinish: True}