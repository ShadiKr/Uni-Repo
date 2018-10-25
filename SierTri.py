# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 18:02:00 2018

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:40:44 2018

@author: Shadi Kreidly
"""

import turtle

def SierTriangle(n, l):
   if n == 0:  
       turtle.forward(l)
       turtle.left(120)
       turtle.forward(l)
       turtle.left(120)
       turtle.forward(l)
   else:
       SierTriangle(n-1, l/2)
       turtle.left(120)
       turtle.forward(l/2)
       SierTriangle(n-1,l/2)
       turtle.left(120)
       turtle.forward(l/2)
       turtle.left(120)
       turtle.forward(l/2)
       SierTriangle(n-1, l/2)
       turtle.left(120)
       turtle.forward(l/2)
       turtle.left(120)
       turtle.forward(l)
       turtle.left(120)
       SierTriangle(n-1, l)
       
     
        
        
        
'''    else:
        turtle.left(60)
        turtle.forward(l)
        SierTriangle(n-1, l)
        turtle.left(120)
        turtle.forward(2*l)
        SierTriangle(n-1,2*l)
        turtle.left(60)
'''
turtle.speed(0)
        
SierTriangle(3, 220)

turtle.done()