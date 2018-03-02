#coding:utf8
#Adrià Baquero 
#02/03/2018

import os
os.system ("clear")
from math import pi 

print """

 Pulsa la tecla T si quieres calcular el área de un triángulo.
 Pulsa la tecla C si quieres calcular el área de un círculo.
 
"""
figura=raw_input("Que quieres calcular? ")
 
if(figura=="T" or figura=="t"):
	base=input("Escriba la base del triangulo: ")
	altura=input("Escribe la altura del triangulo: ")
	if(base<0 or altura<0):
		print "Algún valor es negativo"
	else:
		print "Un triangulo de base",base,"y altura",altura,"tiene una área de" ,round(base*altura/2,2)
else:
	if(figura=="C" or figura=="t"):
		radio=input("Escriba el radio del círculo: ")
		if(radio<0):
			print "Algún valor es negativo"
		else:
			print "Un circulo de radio",radio,"tiene una área de" ,round(pi*radio**2,2)
	else:
print "Selecciona triángulo(T) o círculo(C)"
