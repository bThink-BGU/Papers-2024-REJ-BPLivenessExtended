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
    e = At11
    while True:
        if e == At32:
            e = yield {waitFor: AnyAt, block: [Left]}
        elif e == At21:
            e = yield {waitFor: AnyAt, block: [Down]}
        else:
            e = yield {waitFor: AnyAt}