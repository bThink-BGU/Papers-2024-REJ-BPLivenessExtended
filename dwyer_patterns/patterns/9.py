from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish


spec = "F ( G p)"
variables_names = ["p", "d"]

@b_thread
def pattern():
    """
    F ( G p)
    """
    while True:
        e = yield {waitFor: true(), mustFinish: True}
        if e in non_det:
            break
    yield {block: Not(p)}