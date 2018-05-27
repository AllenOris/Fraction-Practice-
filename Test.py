# -*- coding: utf-8 -*-
"""
Created on Fri May 25 20:31:02 2018

@author: ASUS
"""

import fraction as frac
import os
print(help(frac))
a=frac.make_frac(3,5)
b=frac.make_frac(7,10)
print("a=",end='')
a.show_frac()
print("b=",end='')
b.show_frac()
print()

c=a+b
print("a+b=",end='')
c.show_frac()
print()

c=a+1
print("a+1=",end='')
c.show_frac()
print()

c=a-b
print("a-b=",end='')
c.show_frac()
print()

c=a*b
print("a*b=",end='')
c.show_frac()
print()

c=a/b
print("a/b=",end='')
c.show_frac()
print()

c=1/a
print("1/a=",end='')
c.show_frac()
print()

c=a**3
print("a**3=",end='')
c.show_frac()
print()

c=a**(-3)
print("a**(-3)=",end='')
c.show_frac()


os.system("pause")