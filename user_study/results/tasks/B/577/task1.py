# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d_z0MZtTzD811ztjAOUM2a0yL_ASrZrG
"""

# Don't touch this b-thread
@thread
def bt_1():
    for i in range(5):
        yield {request: [Up, Down, Left, Right]}

# Enter your solution below

@thread
def bt_2():
    while True:
      yield {waitFor: At21, block: Down}

@thread
def bt_3():
    while True:
      yield {waitFor: At32, block: Left}