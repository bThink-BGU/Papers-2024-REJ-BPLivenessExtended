# -*- coding: utf-8 -*-
"""task5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vb3qKAz39EH_H0m12i7lmntt4dWuQLlU
"""

# Don't touch this b-thread
@thread
def bt_1():
    while True:
        yield {request: [Up, Down, Left, Right]}

# Enter your solution below
def bt_2():
    yield {waitFor: At23, mustFinish: True}

def bt_3():
      yield {waitFor: At33, mustFinish: True}

def bt_4():
  e = At11
  visitedR = False
  while True:
    if visitedR:
      if e == At23:
        e = yield {waitFor: AnyAt, block: [Right, Left, Down]}
      elif e == At32:
        e = yield {waitFor: AnyAt, block: [Up, Right, Down]}
      else:
        e = yield {waitFor: AnyAt}
    else:
      if e == At33:
        visitedR = True
      e = yield {waitFor: AnyAt}