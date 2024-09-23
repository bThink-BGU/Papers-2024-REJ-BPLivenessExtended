# without must finish
@thread
def bt_1():
  e = yield {request: [Right, Down]}
  if e == Right:
    e = yield {request: [Right, Left]}
    if e == Left:
      yield {request: Right}
      yield {request: Right}
      yield {request: Down}
    else:
      e = yield {request: [Right, Left]}
      if e == Left:
        yield {request: Right}
        yield {request: Down}
      else:
        e = yield {request: [Down, Up]}
        if e == Up:
          yield {request: Down}
        else:
          yield {request: Up}
  else:
    e = yield {request: [Up, Down]}
    if e == Down:
      yield {request: Right}
      yield {request: Right}
      yield {request: Up}
    else:
      yield {request: Right}
      yield {request: Right}
      yield {request: Down}