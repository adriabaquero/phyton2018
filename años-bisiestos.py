#coding:utf8
#Adrià Baquero 
#28/02/2017


import os
os.system("clear")

print """
		***calculadora de años bisiestos***
 """
valor=input("Escribe el año que quieres saber si es bisiesto: ")

if(valor==0):
    print "El año 0 no existe"
elif(valor<0):
    if(valor%4==0):
        if(valor%400==0 or 400%valor==0):
            print -valor,"a.C es un año bisiesto"
        else:
	    print -valor,"a.C no es un año bisiesto"
    else:
        print -valor,"a.C no es un año bisiesto"
else:
    if(valor>0 and valor%4==0):
        if(valor%400==0 or 400%valor==0):
            print valor,"es un año bisiesto"
        else:
            print valor,"no es un año bisiesto"
    else:
        print valor,"no es un año bisiesto"
