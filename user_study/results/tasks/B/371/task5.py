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
@thread
def bt_1():
  g = 0
  r = 0
  e = At11
  while True:
    if e == At23:
      g = 1
    elif e == At33:
      r = 1
    elif e == At13:
      if g == 1:
        e = yield {waitFor: AnyAt, block:[Down]}
      else:
        e = yield {waitFor: AnyAt}
    elif e == At32:
      if r == 1:
        e = yield {waitFor: AnyAt, block:[Right]}
      else:
        e = yield {waitFor: AnyAt}