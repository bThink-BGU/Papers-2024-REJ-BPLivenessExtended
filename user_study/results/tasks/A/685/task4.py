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
@thred
def bt_2():
  e = At11
  while True:
   if e == At33:
    e = yield {waitFor: AnyAt, block: [Right, Down]}

@thred
def bt_3():
  e = At11
  is_visited = False
  while True:
   if e == At31:
    is_visited = True
    e = yield {waitFor: AnyAt}
   if e == At32 and not is_visited:
    e = yield {waitFor: AnyAt, block: [Right]}
   elif e == At23 and not is_visited:
    e = yield {waitFor: AnyAt, block: [Down]}
   else:
    e = yield {waitFor: AnyAt}