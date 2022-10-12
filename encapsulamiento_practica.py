# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 09:32:56 2022

@author: lab
"""
"""ENCAPSULAMIENTO"""

class Person:
    def __init__(self, age): #con vaariable age
        self._age=age
                 
    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if new_age>=0 and new_age <=120:
            self._age=new_age
            
            
persona=Person(10)
print(persona._age)
persona1=Person(30)
print(persona1._age)
