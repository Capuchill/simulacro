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

def listarMascotas():
    cont=0
    for elem in dataPetShop['pets']:
        cont+=1
        print(f"{cont}.")
        print(f"> Tipo:{elem['tipo']}")
        print(f"> Raza:{elem['raza']}")
        print(f"> Precio:{elem['precio']}")
        print("Servicios: ")
        max=len(elem['servicios'])
        for i in range (0,max):
            print(f'{i+1}. {elem["servicios"][i]}')


def agregarMascota():
    print("***REGISTRO***")
    tipo=input(">> Tipo: ")
    raza=input(">> Raza: ")
    talla=input(">> Talla (grande/mediano/pequeño): ")
    precio=int(input(">> Precio: "))
    servicios=input("Ingrese los servicios separados por comas (','): ")
    listServicios=servicios.split(",")
    dataPetShop['pets'].append({
        "tipo":tipo,
        "raza":raza,
        "talla":talla,
        "precio":precio,
        "servicios":listServicios
    })

def actualizarTipo():


def opcionesCambio():
    print("***OPCIONES***")
    print("1. Tipo.")
    print("2. Raza.")
    print("3. Talla.")
    print("4. Precio.")
    print("5. Servicios.")
    print("6. Ninguno.")

    op=int(input("Opcion -> "))
    if op==1:
        actualizarTipo()
    if op==2:
        actualizarRaza()

    if op==3:
        actualizarTalla()
    if op==4:
        actualizarPrecio()
    if op==5:
        actualizarServicios()

def buscarMascota():
    listarMascotas()
    r=int(input("Cual mascota desea modificar?. (Ingrese el indice): "))
    len(dataPetShop['pets'])
    indiMascota=r-1

def actualizarDatos():
    buscarMascota()
    
    print("Que dato desea actualizar?")
    opcionesCambio()


def menu():
    seguir=True 
    while seguir:
        print("-"*10,"TIENDA DE MASCOTAS","-"*10)
        print(">> MENU:")
        print("1. Mostrar todas las mascotas.")
        print("2. Agregar mascota.")
        print("3. Actualizar datos de mascota.")
        print("4. Eliminar mascota.")
        print("5. Salir del programa")
        
        op=int(input("Opcion -> "))

        if op==1:
            listarMascotas()
        if op==2:
            agregarMascota()
        if op==3:
            actualizarDatos()
        if op==4:
            eliminar()
        if op==5:
            print("Gracias por utilizar el programa... Suerte!")
            seguir=False

        

menu()