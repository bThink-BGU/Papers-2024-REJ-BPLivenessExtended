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
    while True:
        i=0
        e = At11
        if e == At33:
            i = 1
        if i==1:
          if e==At23:
            e = yield {waitFor: AnyAt,block: [Down]}
          if e==At32:
            e = yield {waitFor: AnyAt,block: [Right]}
        else:
          e = yield{waitFor:AnyAt}
@thread
def bt_3():
  yield {waitFor: At23, mustFinish:True}

@thread
def bt_3():
  yield {waitFor: At33, mustFinish:True}