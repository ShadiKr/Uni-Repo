# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 18:47:01 2018

@author: user
"""

import turtle

def HusseinD(n, l=100, t = 3):
    turtle.pensize(t)
    if n == 0:
        turtle.forward(l)
    else:
        HusseinD(n-1,l/2)
        turtle.pu()
        turtle.forward(l/2)
        turtle.pd()
        HusseinD(n-1,l/2)

HusseinD(3)

turtle.done()