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
    yield {waitFor: At31, mustFinish: True}
    visited = False

@thread
def bt_3():
    yield {waitFor: At33, mustFinish: True}
    visited = True

@thread
def bt_3():
    e = At11
    while True:
        if visited:
            while True:
                if e == At23:
                    e = yield {waitFor: AnyAt, block: [Down]}
                elif e == At32:
                    e = yield {waitFor: AnyAt, block: [Right]}
                else:
                    e = yield {waitFor: AnyAt}
        else:
            e = yield {waitFor: AnyAt}