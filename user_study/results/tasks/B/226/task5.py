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

@thread
def bt_2():
    e = At11
    r=0
    while True:
      if e == At33 :
            e = yield {waitFor: AnyAt, block: [Right, Down]}
            r=1
      elif e == At23 and r==1:
            e = yield {waitFor: AnyAt, block: [Down]}
      elif e == At32 and r==1:
            e = yield {waitFor: AnyAt, block: [Right]}
      else:
            e = yield {waitFor: AnyAt}