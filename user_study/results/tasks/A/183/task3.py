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
def bt_2():
    e = At11
    count = 0
    if e == At11:
      count+=1
      if count < 2:
        e = yield {waitFor: AnyAt, block: [Up, Left]}
      else:
        e = yield {waitFor: AnyAt, block: [Up, Left, Left]}
    elif e == At13 and count<4:
      count+=1
      if count <4:
        e = yield {waitFor: AnyAt, block: [Up, Right]}
      else:
        e = yield {waitFor: AnyAt, block: [Up, Right, Left]}
    elif e == At31 and count<=2:
      count+=1
      e = yield {waitFor: AnyAt, block: [Down, Left, Up]}
    elif e == At33 and count<=4:
      count+=1
      e = yield {waitFor: AnyAt, block: [Down, Right, Left]}
    elif e == At21:
      count+=1
      e = yield {waitFor: AnyAt, block: [Left, Right, Up]}
    elif e == At23 and count==3:
      count+=1
      e = yield {waitFor: AnyAt, block: [Left, Right]}
    elif e == At32:
      count+=1
      e = yield {waitFor: AnyAt, block: [Up, Down, Left]}
    elif e == At12:
      count+=1
      if count<3:
        e = yield {waitFor: AnyAt, block: {Up, Down}}
      else:
        e = yield {waitFor: AnyAt, block: {Up, Down, Left}}