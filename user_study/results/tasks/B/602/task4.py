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
A31_flag =False
def bt_2():
  while True:
     yield{waitFor: A33}
     yield{request: [Up,Left],block:[Right,Down]}
     yield{waitFor: A31}
     A31_flag =True

def bt_3():
  while True:
     yield{waitFor: A23}
     if A31_flag==False:
        yield{waitFor:A13, block:Down}
def bt_4():
  while True:
     yield{waitFor: A32}
     if A31_flag==False:
        yield{waitFor:A31, block:Right}