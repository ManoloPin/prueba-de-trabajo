
from flask import Flask
from main_nodo import nodo
import sys
import time

"""archivos donde se encuentran los modulos"""
sys.path.insert(0, '..') 

"""nodo """
node = nodo("142.44.246.92", 8001)

time.sleep(1)
node.start()
time.sleep(2)
"""-----  conocidos del nodo -----"""
node.connect_with_node('142.44.246.23', 8002)
node.connect_with_node('142.44.246.12', 8003)
node.connect_with_node('158.69.63.154', 8004)



time.sleep(1)

""" funcion de pedir, guardar dato y calcular suma """
while True:
    try: 
        print("\n_____________BIENVENIDO___________\n"
        +"\n Ingrese el numero de la acción que desea realizar:"
        +"\n1. Agregar numero \n2.Sumar numero \n3. Salir")
        
        op = int(input(" \n : "))

        if op == 1:
            num = input("\nEscriba el numero que desea agregar  ")
            archivo = open("numeros.txt","a")#Creando txt con la información del cliente
            archivo.write("{},0".format(num))
            archivo.close() 
            print("Numero guardado")
            node.send_to_nodes(num)
        elif op == 2:
            numbers = []
            with open("numeros.txt", "r") as file:
                for line in file:
                    fields = line.split(",")
                    #print(line.rstrip("n"))
                subnumbers = (int(field) for field in fields)
                numbers.extend(subnumbers)
                suma = sum(numbers)
            print("\nLa suma es: "+str(suma))
        elif op == 3:
            node.stop()
            print('end')
            break
    except ValueError:
        print("Porfavor, ingresa solo numeros")
    

