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
    first=False
    while True:
        if e == At31:
           first=True
           e = yield {waitFor: AnyAt, block: [Up]}
        elif e==At21:
          if (first):
             e = yield {waitFor: AnyAt, block: [Down]}
          else:
              e = yield {waitFor: AnyAt}
        elif e==At32:
          if (first):
             e = yield {waitFor: AnyAt, block: [Left]}
          else:
              e = yield {waitFor: AnyAt}
        else:
            e = yield {waitFor: AnyAt}