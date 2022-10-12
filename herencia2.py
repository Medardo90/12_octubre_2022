# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:32:54 2022

@author: lab
"""

"""HERENCIA  ejemplo"""

class Padre(object): 
    def __init__(self,ojos, cejas):
        self.ojos= ojos 
        self.cejas= cejas 

class Hijo(Padre):
    def __init__(self, ojos , cejas , cara):
        Padre.__init__(self,ojos, cejas)
        self.cara = cara 
        
juan = Hijo (" veerdes", "Negras", "redonda")
print(juan.ojos, juan.cejas, juan.cara)