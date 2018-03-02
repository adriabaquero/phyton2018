#coding:utf8
#Adrià Baquero
#02/03/2018

# Inicializaciones
salir = "N"
numero=1

while ( salir=="N" ):
    # Hago cosas
    print"El número és", numero

    # Incremento
    numero=numero+1
    # Activo indicador de salida si toca
    if (numero>50): # Condición de salida
            salir = "S"
