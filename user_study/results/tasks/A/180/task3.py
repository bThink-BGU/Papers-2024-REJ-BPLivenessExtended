# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i05U7S9LuriwTXAsHRCavGFZEMFk3dm5
"""

# Don't touch this b-thread
@thread
def bt_1():
    for i in range(5):
        yield {waitFor: [Up, Down, Left, Right]}
    yield {block: [Up, Down, Left, Right]}

# Enter your solution below
@thread
def bt_2():
     e = At11
     for i in range(5):
        if e == At12:
           yield {request: [Right]}
           e = yield {waitFor: AnyAt, block: [LLeft, Up, Down]}
        elif e == At11:
          yield {request: [Right, Down]}
          e = yield {waitFor: AnyAt, block: [Up, Left]}
        elif e == At21:
           yield {request: [Down]}
           e = yield {waitFor: AnyAt, block: [Up, Left, Right]}
        elif e == At31:
          yield {request: [Right]}
          e = yield {waitFor: AnyAt, block: [Up, Left, Down]}
        elif e == At32:
          yield {request: [Right]}
          e = yield {waitFor: AnyAt, block: [Up, Down, Left]}
        elif e == At33:
          yield {request: [Up]}
          e = yield {waitFor: AnyAt, block: [Down, Right, Left]}
        elif e == At13:
          yield {request: [Down]}
          e = yield {waitFor: AnyAt, block: [Up, Right, Left]}
        elif e == At23:
          yield {request: [Up, down]}
          e = yield {waitFor: AnyAt, block: [Left, Right]}