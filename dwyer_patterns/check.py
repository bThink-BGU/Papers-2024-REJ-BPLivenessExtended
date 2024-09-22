from symbolic_bprogram_verifier import SymbolicBProgramVerifier
from utils import *
from bppy.model.b_thread import b_thread
from bppy.model.sync_statement import waitFor, request, block, mustFinish
from bppy.model.bprogram import BProgram
from bppy.model.event_selection.simple_event_selection_strategy import SimpleEventSelectionStrategy
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("--pattern", default="8")

args = parser.parse_args()

with open(os.path.join("patterns", args.pattern + ".py"), "r") as f:
    exec(f.read())


event_list = [Assignment({k: v for k, v in zip(variables_names, values)}) for values in itertools.product([True, False], repeat=len(variables_names))]

@b_thread
def general():
    while True:
        yield {request: event_list}


def bprogram_generator():
    return BProgram(bthreads=[general(), pattern()],
                    event_selection_strategy=SimpleEventSelectionStrategy())


verifier = SymbolicBProgramVerifier(bprogram_generator, event_list)

assumption = "G ( F must_finish = FALSE )"

if "d" in variables_names:
    non_det_assumption = "G ( F d )"
else:
    non_det_assumption = "TRUE"

result, explanation_str = verifier.verify(spec=f"G ( ( {assumption} ) & ( {non_det_assumption} ) ) -> ( {spec} )", type="BDD", find_counterexample=True,
                                          print_info=False)


if result:
    print("Under assumption specification holds - OK")
else:
    print("Under assumption - Violation Found! Counterexample:")
    print(explanation_str)

