# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i05U7S9LuriwTXAsHRCavGFZEMFk3dm5
"""

# Don't touch this b-thread
@thread
def bt_1():
    for i in range(5):
        yield {waitFor: [Up, Down, Left, Right]}
    yield {block: [Up, Down, Left, Right]}

# Enter your solution below
def bt_2():
    e = At11
    List = []
    while True:
      if e in AnyAt[0:2] or e == At32:
         List.append(Up)
      elif e in AnyAt[5:] or e == At12:
         List.append(Down)
      if e in [At11, At21, At31, At23]:
        List.append(Left)
      elif e in [At13, At23, At33, At21]:
        List.append(Right)
      e = yield {waitFor: AnyAt, block: List}

def bt_2():
  for i in range(4):
    yield {waitFor: AnyAt}
  yield {waitFor: At23, mustFinish: True}