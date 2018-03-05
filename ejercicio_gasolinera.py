#coding: utf8
#Adrià Baquero
#04/03/2018

import os
os.system("clear")

print """
    Tipos de gasolina:
-Super:     1-Normal(1.5€)      2-Turbo(1.55€)
-Sin plomo: 3-Normal(1.6€)      4-Con aditivos(sabor naranja)(1.65€)
-Diesel:    5-Normal((1.7€)     6-Fast&Furious(1.75€)
 
 gasolina=input ("Qué gasolina desea? ")

if(gasolina==1):
	litros=input ("Cuántos litros quiere? ")
	print "Costará :" ,1.5*litros,"€"
elif(gasolina==2):
	litros=input ("Cuántos litros quiere? ")
	print "Costará:" ,1.55*litros,"€"
elif(gasolina==3):
	litros=input ("Cuantos litros quiere? ")
	print "Costará:" ,1.60*litros,"€"
elif(gasolina==4):
	litros=input ("Cuantos litros quiere? ")
	print "Costará:" ,1.65*litros,"€"
elif(gasolina==5):
	litros=input ("Cuantos litros quiere? ")
	print "Costará:" ,1.70*litros,"€"
elif(gasolina==6):
	litros=input ("Cuantos litros quiere? ")
	print "Costará:" ,1.75*litros,"€"
else:
	print "Selecciona un producto del 1 al 6"
    
