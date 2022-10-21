# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 22:01:18 2022

@author: Patricio Haro
"""

class Padre():
  def __int__(self, ojos,cejas):
    self.ojos= ojos
    self.cejas= cejas
  
class Hijo(Padre):
  def __init__(self,ojos, cejas, cara):
    Padre.__int__(self, ojos, cejas)
    self.cara=cara

juan= Hijo("verdes", "negras", "redonda")
print(juan.ojos, juan.cejas, juan.cara)



class A(object):
    def __init__(self):
        self.a="a"
        
class B(A):
    def __init__(self):
        A .__init__(self)
        self.b ="b"

obj_b = B()
print("aa: ",obj_b.a , "bb: ",obj_b.b)


class C(B):
    def __init__(self):
         B .__init__(self)
         self.c= "c"

obj_c = C()
print("aa: ",obj_c.a , "bb: ",obj_c.b, "cc: ",obj_c.c)