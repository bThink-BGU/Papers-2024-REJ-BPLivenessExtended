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
    e = At11
    AnyExcept21 = [At11, At12, At13, At23, At31, At32, At33]
    AnyExcept32 = [At11, At12, At13, At21, At23, At31, At33]

    while True:
        if e == At21:
            e = yield {waitFor: AnyExcept21, block: Down}
        elif e == At32:
            e = yield {waitFor: AnyExcept32, block: Left}
        else:
            e = yield {waitFor: AnyAt}
