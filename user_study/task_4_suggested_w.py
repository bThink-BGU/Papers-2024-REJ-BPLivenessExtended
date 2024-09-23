@thread
def bt_1():
    while True:
        yield {request: [Up, Down, Left, Right]}

@bp.thread
def task_4_with_must_finish():
    while True:
        yield {waitFor: At33}
        e = yield {waitFor: [At31, At33]}
        if e == At33:
            yield {mustFinish: True}