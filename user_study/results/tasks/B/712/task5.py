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
    wentToAt33 = False
    wentToAt23 = False

    e = At11
    while True:
        if e == At11:
            e = yield {waitFor: [Down, Right], block: [Left, Up]}
        elif e== At12:
            e = yield {waitFor: [Left, Right], block: [Down, Up]}
        elif e== At13:
              e = yield {waitFor: [Left, Down], block: [Right, Up]}
        elif e== At21:
            e = yield {waitFor: [Up, Down], block: [Left, Right]}
        elif e== At23:
            wentToAt23 = True
            if wentToAt33:
              e = yield {waitFor: [Up], block: [Left, Right,Down]}
            else:
              e = yield {waitFor: [Up, Down], block: [Left, Right]}
        elif e== At31:
            e = yield {waitFor: [Right], block: [Left, Down,Up]}
        elif e== At32:
            if wentToAt33 or not wentToAt23:
              e = yield {waitFor: [Left], block: [Right,Down , Up]}
            else:
              e = yield {waitFor: [Right,Left], block: [Down , Up]}
        elif e== At33:
            wentToAt33 = True
            e = yield {waitFor: [Up,Left], block: [Right, Down]}