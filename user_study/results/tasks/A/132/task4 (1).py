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
    visit =  False 
    e = At11
    while True:
       if visit ==  True :
          e = yield {waitFor: At23, mustFinish: True}
          visit =  False 
       elif e == At33:
          if visit ==  False :
            visit =  True 
       else:
        e = yield {waitFor: AnyAt}