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
a=true
@thread
def bt_3():
  while True:
    yield {waitFor: At33, block:[Right,Down]}
    while a:
      yield{waitFor : At32, block: [Right]}

@thread
def bt_4():
  while True:
    yield {waitFor: At33, block: [Right,Down]}
    while a:
      yield{waitFor : At23, block: [Down]}

def bt_5():
  while True:
    yield {waitFor: At33, block:[Right,Down]}
    yield{waitFor : At31}
    a=False;