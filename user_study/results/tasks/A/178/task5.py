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
check = True
AnyAt = [At11, At12, At13, At21, At23, At31, At32, At33]
l = []
@thread
def bt_2(): #blocks wall movement
    e = At11
    a = 1 # [a,b]
    b = 1
    blocks = []
    while True:
        if a == 1:
          blocks.append(Up)
        if a ==2 and b == 1:
          blocks.append(Right)
        if a ==2 and b == 3:
          blocks.append(Left)
        if a == 3:
          blocks.append(Down)
        if b == 1:
          blocks.append(Left)
        if b ==2 and a == 1:
          blocks.append(Down)
        if b ==2 and a == 3:
          blocks.append(Up)
        if b == 3:
          blocks.append(Right)
        e = yield {waitFor: AnyAt, block: blocks}
        x , y , a , b = e
@thread
def bt_3():
  while True:
    e = yield {waitfor: anyAt2}
    if e==At33:
      l.append(e)
    if e==At23:
      l.append(e)

@thread
def bt_4():
  while True:
    yield{waitfor: l}
    yield {mustFinish : True}