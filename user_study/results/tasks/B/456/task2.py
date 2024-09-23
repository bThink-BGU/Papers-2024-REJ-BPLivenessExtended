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
LeftWalls = [At11, At21, At31, At23]
RightWalls = [At13, At23, At33, At21]
UpperWalls = [At11, At12, At13, At32]
LowerWalls = [At31, At32, At33, At12]
e = At11

@thread
def bt_LeftCheck():
    while True:
        if e in LeftWalls:
            e = yield {waitFor: AnyAt, block: Left}
@thread
def bt_RightCheck():
    while True:
        if e in RightWalls:
            e = yield {waitFor: AnyAt, block: Right}

@thread
def bt_UpCheck():
    while True:
        if e in UpperWalls:
          e = yield {waitFor: AnyAt, block: Up}

@thread
def bt_DownCheck():
    while True:
        if e in LowerWalls:
          e = yield {waitFor: AnyAt, block: Down}