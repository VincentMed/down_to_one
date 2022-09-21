# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 12:15:06 2022

@author: Vincent Medrano
"""

def down_to_one(x):
    num_seq = [x]
    steps = 0
    #if 0 or negative, return nada
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
    # Added line
       num_seq.append(x)
       steps += 1
    print("Number of steps: %d" % steps)   
    return num_seq
    
