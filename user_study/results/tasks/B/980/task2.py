# -*- coding: utf-8 -*-
"""task2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cU6_kbhswbYJbN_RYiga8-D5X-S2MD2O
"""

# Don't touch this b-thread
@thread
def bt_1():
    for i in range(5):
        yield {request: [Up, Down, Left, Right]}

# Enter your solution below
@thread
def bt_2():
      e = At11
      while True:
          if e == At12 or  e == At13 or e==At11:
              e = yield {waitFor: AnyAt, block: Up}
          elif e == At31 or e==At32 or e==At33:
              e = yield {waitFor: AnyAt, block: Down}
          else:
              e = yield {waitFor: AnyAt}
@thread
def bt_3():
      e = At11
      while True:
          if e == At21 or  e == At31 or e==At11:
              e = yield {waitFor: AnyAt, block: Left}
          elif e == At13 or e==At23 or e==At33:
              e = yield {waitFor: AnyAt, block: Right}
          else:
              e = yield {waitFor: AnyAt}