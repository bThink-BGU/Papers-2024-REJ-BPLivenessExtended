# -*- coding: utf-8 -*-
"""task4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xr0ykmflWmrE8LU7N72vjRC_AkZ90BNY
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
    while True:
        if e == At11:
            e = yield {waitFor: AnyAt, block: [Left,Up]}
        elif e == At12:
            e = yield {waitFor: AnyAt, block: [Down,Up]}
        elif e == At13:
            e = yield {waitFor: AnyAt, block: [Right,Up]}
        elif e == At21:
            e = yield {waitFor: AnyAt, block: [Left,Right]}
        elif e == At23:
            e = yield {waitFor: AnyAt, block: [Right,Left]}
        elif e == At31:
            e = yield {waitFor: AnyAt, block: [Down,Left]}
        elif e == At32:
            e = yield {waitFor: AnyAt, block: [Up,Down]}
        elif e == At33:
            e = yield {waitFor: AnyAt, block: [Right,Down]}

@thread
def bt_3():
  e=At11
  count=0
  while True:
    if e==A33:
      count =2
    elif e==A31 and count ==2:
      count = 0