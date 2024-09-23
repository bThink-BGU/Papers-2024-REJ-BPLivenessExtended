@thread
def bt_1():
    while True:
        yield {request: [Up, Down, Left, Right]}

@bp.thread
def task_4_without_must_finish():
    while True:
        e = yield {waitFor: At33}
        while True:
            if e == At23:
                e = yield {waitFor: AnyAt, block: Down}
            elif e == At32:
                e = yield {waitFor: AnyAt, block: Right}
            elif e == At33:
                e = yield {waitFor: AnyAt, block: [Down, Right]}
            elif e == At31:
                break
            else:
                e = yield {waitFor: AnyAt}