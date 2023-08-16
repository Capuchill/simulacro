import os 
""" Elabore un programa Python para gestionar el CRUD del archivo de datos PetShopping.json con las siguientes funcionalidades:

    
Mostrar en pantalla todas las mascotas a la venta visualizando: Tipo, Raza, Precio y Servicios

    
Crear Nueva mascota con la posibilidad de múltiples ítems de Servicio

    
Mostrar los datos de Mascotas por Tipo elegido visualizando: Raza, Precio y Servicios

    
Actualizar los datos de una mascota consultada por índice (Mostrar el listado total y elegir por     índice)

    
Eliminar una mascota de la tienda (Mostrar el listado total y elegir por índice) """

import json 

dataPetShop={}
dataPetShop['pets']=[]
with open ('PetShopping.json') as clientes:
    mascotas=json.load(clientes)
    for elem in mascotas['pets']:

        puichico={}
        puichico['tipo']=elem['tipo']
        puichico['raza']= elem['raza']
        puichico['talla']= elem['talla']
        puichico['precio']= elem['precio']
        puichico['servicios']=elem['servicios']
        dataPetShop['pets'].append(puichico)


def menu():
    seguir=True 
    while seguir:
        print("-"*10,"TIENDA DE MASCOTAS","-"*10)
        print(">>MENU<<")
        
        break



menu()