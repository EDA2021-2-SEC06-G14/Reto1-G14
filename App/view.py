"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from prettytable import PrettyTable, ALL
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronologicamente los artistas")
    print("3- Listar cronologicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por tecnica")
    print("5- Clasificar las obras por nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")
    print("7- Proponer una nueva exposicion en el museo")
    print("0- Salir")

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()

def loadData(catalog):

    """
    Carga datos en el catalogo
    """
    controller.loadData(catalog)

def printartistas(artistas, inicial, final):

    """
    Imprime los artistas nacidos en rango de anos 
    """

    size = lt.size(artistas)

    print("============= Req No. 1 Inputs =============")
    print("Artist born between " + str(inicial) + " and " + str(final) + "\n")
    print("============= Req No. 1 Answer =============")
    print("There are " + str(size) + " artist born between " + str(inicial) + " and " + str(final) + "\n")
    print("The first and last 3 artists in range are")
    x = PrettyTable()
    x.field_names = (["ConstituentID","DisplayName","BeginDate","Nationality","Gender","ArtistBio","Wiki QID","ULAN"])
    x.hrules=ALL

    for i in range(1, 4):
        artista = lt.getElement(artistas, i)
        
        x.add_row([artista["ConstituentID"], artista["DisplayName"], artista["BeginDate"],
                   artista["Nationality"], artista["Gender"], artista["ArtistBio"], 
                   artista["Wiki QID"], artista["ULAN"]])

    for i in range(size-2, size+1):
        artista = lt.getElement(artistas, i)
        x.add_row([artista["ConstituentID"], artista["DisplayName"], artista["BeginDate"],
                   artista["Nationality"], artista["Gender"], artista["ArtistBio"], 
                   artista["Wiki QID"], artista["ULAN"]])
        
    print(x)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....\n")
        catalog = initCatalog()
        loadData(catalog)
        sizeartista = lt.size(catalog["Artist"])
        sizeartwork = lt.size(catalog["Artwork"])
        print("Artistas cargados: " + str(sizeartista))
        print("Obras cargadas: " + str(sizeartwork))
        print("Ultimos tres artistas: \n")
        print(lt.getElement(catalog["Artist"], sizeartista-2))
        print(lt.getElement(catalog["Artist"], sizeartista-1))
        print(lt.getElement(catalog["Artist"], sizeartista ))
        print("\nUltimas tres obras: \n")
        print(lt.getElement(catalog["Artwork"], sizeartwork-2))
        print(lt.getElement(catalog["Artwork"], sizeartwork-1))
        print(lt.getElement(catalog["Artwork"], sizeartwork))


    elif int(inputs[0]) == 2:
        inicial = int(input("Año inicial: "))
        final = int(input("Año final: "))
        print("Se estan obteniendo los artistas...")
        artistas = controller.GetArtistas(catalog, inicial, final)
        printartistas(artistas, inicial, final)
        

    elif int(inputs[0]) == 3:
        inicial = input("Año inicial: ")
        final = input("Año final: ")
        print("Se estan organizando las adquisiciones cronologicamente...")
        

    elif int(inputs[0] == 4):
        artista = input("Artista: ")
        print("Se estan organizando las obras por tecnica...")
        

    elif int(inputs[0] == 5):
        print("Se estan organizando las obras por la nacionalidad...")
        

    elif int(inputs[0] == 6):
        depar = input("Departamento del museo...")
        print("Se esta calculando el costo...")
        

    elif int(inputs[0] == 7):
        pass

    else:
        sys.exit(0)
sys.exit(0)

