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
        if e == At11:
            e = yield {waitFor: AnyAt, block: [Up,Right]}
        elif e == At12 or e == At32:
            e = yield {waitFor: AnyAt, block: [Down, Up]}
        elif e == At13:
            e = yield {waitFor: AnyAt, block: [Up, Left]}
        elif e == At21 or e == At23:
            e = yield {waitFor: AnyAt, block: [Left, Right]}
        elif e == At31 :
            e = yield {waitFor: AnyAt, block: [Down, Right]}
        elif e == At33:
            e = yield {waitFor: AnyAt, block: [Down, Left]}