#coding:utf8
#Adrià Baquero
#08/03/18

#Inicializaciones
salir="N"
contador=1

while(salir=="N"):
    #Hace cosas
    print contador
    #Incremento
    contador=contador+1
    #Activo indicador de salida si hace falta
    if(contador>50):#Condición de salida
salir = "S"
