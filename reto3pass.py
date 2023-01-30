# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 15:46:25 2023

@author: oardila
"""

# Se realizan los imports de las clases que se necesitan utilizar, los 2 modulos importados
#hacen parte de la biblioteca estandar
import secrets
import string


# Se definen los caracteres a utilizar
letters = string.ascii_letters #cocantenación de letras upper y lower
digits = string.digits # cadena de digitos de 0 a 9
special_chars = string.punctuation # carecters especiales

alphabet = letters + digits + special_chars # defino el alfabeto disponible a usar

# fix password length4
pwd_length = input("Defina la cantidad de caracteres que desea entre 6 y 16 ")

try:
  valido= int(pwd_length)
  if valido > 5 and valido < 17:
    pwd = ''
    for i in range(valido):
      pwd += ''.join(secrets.choice(alphabet))
    print("Salida primera opción de solución")
    print(pwd)
  else:
      print ("El valor digitado no es un valor valido")
     
      
except (ValueError):
  print ("El valor digitado no es un valor valido")
#-----------------------------------------------------------------------------------  
#otra forma

import random
#--import Werkzeug
from Werkzeug import security



def esta_en_rango (valido):
  return valido in range([6, 16])

while esta_en_rango==True and type(pwd_length)== int:
  pwd_length = input("Defina la cantidad de caracteres que desea entre 6 y 16 ")
  try:
    resultado= random.sample(alphabet, valido)
    password= "".join(resultado)
    password_encriptado= security.generate_password_hash(password)
    print("Segunda opción de solución con pass visible y pass encriptado")
    print("{} => {}" .format (password, password_encriptado))
    
  except ValueError:
    print("valor invalido")
 
    
    


# generate a password string
'''pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))
print("Salida primera opción de solución")
print(pwd)
'''
'''
# generate password meeting constraints
while True:
  pwd = ''
  for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

  if (any(char in special_chars for char in pwd) and 
      sum(char in digits for char in pwd)>=2):
          break
print(pwd)
'''
