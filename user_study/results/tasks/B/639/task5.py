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
def bt_2():
  e = At11
  red = False
  while True:
    if red:
      if e == At23:
        e = yield{waitFor:AnyAt, block:Left}
      elif e == At32:
        e = yield{waitFor:AnyAt, block:Down}
      else:
        e = yield{waitFor:AnyAt}
    else:
      e = yield{waitFor:AnyAt}