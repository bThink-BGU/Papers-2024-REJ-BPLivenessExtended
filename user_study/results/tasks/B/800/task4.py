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

def bt_2():
  e = At11
  while True:
    if e==At11 or e==At12 or e==At13 or e==At32:
       e = yield{waitFor: AnyAt, block:[Up]}

    elif e==At31 or e==At32 or e==At33 or e==At12:
       e = yield{waitFor: AnyAt, block:[Down]}

    elif e==At13 or e==At23 or e==At33 or e==At21:
       e = yield{waitFor: AnyAt, block:[Right]}

    elif e==At11 or e==At21 or e==At31 or e==At23:
       e = yield{waitFor: AnyAt, block:[Left]}

    else:
      e = yield{waitFor: AnyAt}