# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 09:43:43 2022

@author: lab
"""
"""ENCAPSULAMIENTO"""
class Person:
    def __init__(self): #con none para poder rstringir las edades
        self._age=None          
        
    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if new_age>=0 and new_age <=120:
            self._age=new_age       #self.age=new_age """ no es varible igual por el guion 
            
persona=Person()
print(persona.get_age())
persona.set_age(50)
print(persona.get_age())

