# -*- coding: utf-8 -*-
"""task4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xr0ykmflWmrE8LU7N72vjRC_AkZ90BNY
"""

# Don't touch this b-thread
@thread
def bt_1():
    while True:
        yield {request: [Up, Down, Left, Right]}

# Enter your solution below

@thread
def bt_2():
    e = At11
    while True:
        if e == At33:
            e = yield {waitFor: AnyAt, block: [Down, Right]}
        else:
            e = yield {waitFor: AnyAt}