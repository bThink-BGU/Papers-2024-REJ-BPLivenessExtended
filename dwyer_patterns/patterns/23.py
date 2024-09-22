from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish


spec = "G !q | F (q & (s U (!p | s)))"
variables_names = ["q", "p", "s", "d"]


@b_thread
def pattern():
    """
    Kind: Precedence: s precedes p
    Scope: After q
    LTL:
        G !q || F (q && (s V (!p || s)))

        G !q || F(q & (!p W s))
    """
    yield {waitFor: And(q, s) }
    while True:
        e = yield {waitFor: Or(And(q, s), And(Not(p), q, Not(s))), mustFinish: True}
        if e in And(q,s):
            break
        if e in And(Not(p),q,Not(s)):
            if non_deterministic(e):
                continue
            yield {waitFor: s, block: And(p, Not(s))}
            break
    # e = yield {waitFor: q}
    # if e in Not(s):
    #     yield {waitFor: s, block: And(p, Not(s))}
    #
    #
    #
    #
    # e = yield {waitFor: Or(Not(q),
    #                    And(Not(p), q, Not(s)),
    #                    Or(Not(q), Not(s)),
    #                    And(q, s)), mustFinish: True}
    # if e in Not(q):
    #     if non_deterministic(e):
    #         # 2
    #     else:
    #         # 4
    # elif e in Not(s):
    #     if e in p:
    #         # 4
    #     else:
    #         if non_deterministic(e):
    #             # 3
    #         else:
    #             # 4
    # else:
    #     # 1





