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
@thread
def bt_2():
  AnyAt = [At11, At12, At13, At21, At23, At31, At32, At33]
  e = At11
  yield {waitFor: At23, mustFinish: True}
  yield {waitFor: At32, mustFinish: True}