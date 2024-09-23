@thread
def bt_1():
    for i in range(5):
        yield {request: [Up, Down, Left, Right]}

@bp.thread
def task_1_without_must_finish_1():
    e = At11
    while True:
        if e == At32:
            e = yield {waitFor: AnyAt, block: Right}
        else:
            e = yield {waitFor: AnyAt}
@bp.thread
def task_1_without_must_finish_2():
    e = At11
    while True:
        if e == At23:
            e = yield {waitFor: AnyAt, block: Down}
        else:
            e = yield {waitFor: AnyAt}