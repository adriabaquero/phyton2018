#coding:utf8
#Adrià Baquero
#23/02/2018

valor1=input("Introduzca un valor:  ")
valor2=input("Introduzca un valor:  ")

if(valor1==0)or(valor2==0):
	print"ERROR"
else:
	if(valor1>valor2):
		mayor=valor1
		menor=valor2
	else:
		mayor=valor2
		menor=valor1
	if(mayor%menor==0):
		print mayor, "es múltiplo de", menor 
	else:
		print mayor, "no es múltiplo de", menor
		 
