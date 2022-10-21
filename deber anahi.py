# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:56:16 2022

@author: Patricio Haro
"""

class Cliente():
  def __init__(self):
    self._nombre = ""
    self._edad = ""
    self._identi= ""
    self._saldo = (120)
  def get_saldo(self):
       return self.saldo   
    
  # def set_saldo(self, new_saldo):
  #     if  new_saldo >= 0 and new_saldo <= 120:
  #         self.saldo = new_saldo

#
# class  Maquina():
#   def __init__(self,nombre_p,codigo,precio):
#       self.nombre_p = nombre_p
#       self.codigo = codigo
#       self.precio = precio
        
# #
# class Galleta():
#     def __init__(self,galleta):
#         self.galleta= galleta
       
#     def incorporarMaquina (self):
#         galleta_g = []
#         galleta_g.append(Maquina("OREO","45","0.5"))
#         return galleta_g
   
#     def generarMaquina(self):
#         galleta_g = []
#         for i in range (0,self.galleta):
#             galleta_g.append(Maquina("OREO","45","0.5"))
#         return galleta_g
# #     
cliente_1 = Cliente()
cliente_1._nombre = "Pedro"
cliente_1._edad = "20"
cliente_1._identi = "1724991748"
cliente_1.set_saldo(50)
print("Nombre:",cliente_1._nombre,",tiene:", cliente_1._edad, "años, con Nº de Identificacion:"
,cliente_1._identi, "su SALDO es: $",cliente_1._saldo)