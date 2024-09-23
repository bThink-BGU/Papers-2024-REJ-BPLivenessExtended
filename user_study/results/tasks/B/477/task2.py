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
    block = []
    if e == At11 or e == At12 or e == At13:
      block.append(Up)
    if e == At11 or e == At21 or e == At31:
      block.append(Left)
    if e == At13 or e == At23 or e == At33:
      block.append(Right)
    if e == At12 or e == At22 or e == At32:
      block.append(Down)
    e = yield {block: block, waitFor: AnyAt}