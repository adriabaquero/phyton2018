#coding:utf8
#Adrià Baquero
#02/03/2018

# Inicializaciones
salir = "N"
numero=1
maximo=input("introduce un numero:")

if(maximo<=0):
	salir="S"

while ( salir=="N" ):
    # Hago cosas
    print"El número és", numero

    # Incremento
    numero=numero+1
    # Activo indicador de salida si toca
    if (numero>maximo): # Condición de salida
            salir = "S"
