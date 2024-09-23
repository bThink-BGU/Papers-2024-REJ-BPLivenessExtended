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

def bt_2():
    visited_23 = False
    visited_33 = False
    e = At11
    while True:
        if e == At23:
            visited_23 = True
            if visited_33:
                e = yield {waitFor: AnyAt, block: [Down]}
            else:
                e = yield {waitFor: AnyAt}
        elif e == At32:
            if visited_33:
                e = yield {waitFor: AnyAt, block: [Right]}
            else:
                e = yield {waitFor: AnyAt}
        elif e == At33:
            visited_33 = True
            e= yield {waitFor: AnyAt, block: [Down, Right]}
        else:
            e = yield {waitFor: AnyAt}