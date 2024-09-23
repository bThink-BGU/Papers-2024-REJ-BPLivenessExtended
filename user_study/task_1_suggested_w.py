@thread
def bt_1():
    for i in range(5):
        yield {request: [Up, Down, Left, Right]}

@bp.thread
def task_1_with_must_finish():
    yield {waitFor: At31}
    yield {mustFinish: True}