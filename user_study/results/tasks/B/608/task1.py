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
def bt_2():
  while True:
    yield{waitfor:At21, block:Down}
def bt_3():
  yield{waitfor:At30, block:Right}
def bt_4():
  yield{waitfor:At32, block:Left}