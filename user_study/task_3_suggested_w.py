# with must finish

@thread
def bt_2():
    e = At11
    while True:
        block_l = []
        if e in [At11, At12, At13]:
            block_l.append(Up)
        if e in [At31, At32, At33]:
            block_l.append(Down)
        if e in [At11, At21, At31]:
            block_l.append(Left)
        if e in [At13, At23, At33]:
            block_l.append(Right)
        e = yield {waitFor: AnyAt, block: block_l}

@thread
def bt_3(): # G at 5 moves
  for i in range(4):
    e = yield {waitFor: AnyAt, mustFinish: True}
  e = yield {waitFor: At23, mustFinish: True}