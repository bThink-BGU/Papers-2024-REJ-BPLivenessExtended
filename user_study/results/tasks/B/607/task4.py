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
def bt_track_R():
    was_at_R = False
    for event in AnyAt:
        yield {waitFor: event}
        if event == 'At33':
            was_at_R = True
        elif event != 'At31' and was_at_R:

            yield {request: [Up, Down, Right]}
@thread
def bt_track_B():
    was_at_B = False
    for event in AnyAt:
        yield {waitFor: event}
        if event == 'At31':
            was_at_B = True
        elif event == 'At33' and was_at_B:
            was_at_B = False