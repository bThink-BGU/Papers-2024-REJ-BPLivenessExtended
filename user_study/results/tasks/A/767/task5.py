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
    e = At11
    e = yield {waitFor: AnyAt, block: [Up, Down, Left]}
    e = yield {waitFor: AnyAt, block: [Up, Down, Left]}
    e = yield {waitFor: AnyAt, block: [Up, Right, Left]}
    e = yield {waitFor: AnyAt, block: [Up, Right, Left]}
    while True:
            e = yield {waitFor: AnyAt, block: [Down, Right]}
            while True:
              if e == At32:
                e = yield {waitFor: AnyAt, block: [Right]}
              elif e == At23:
                e = yield {waitFor: AnyAt, block: [Down]}
              else:
                e = yield {waitFor: AnyAt}