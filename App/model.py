"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.singlelinkedlist import addLast
import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as me
from DISClib.Algorithms.Sorting import quicksort as qs
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(tipo):
    """
    Inicializa el catálogo de . Crea dos listas vacias, una para las obras 
    y otro para los artistas
    """
    catalog = {'Artwork': None,
               'Artist': None}

    catalog['Artwork'] = lt.newList(tipo)
    catalog["Artist"] = lt.newList(tipo)

    return catalog

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork,tipo):
    """
    Carga solo la informacion necesaria al catalogo
    """
    new = newArtwork(tipo)

    for key in new.keys():

        if key == "DateAcquired" and artwork["DateAcquired"] == "":
            new[key] = "0"

        else:
            new[key] = artwork[key]

    
    lt.addLast(catalog["Artwork"], new)

def newArtwork(tipo):
    """
    Se crea un diccionario par cada obra
    """
    new = {'ObjectID' : None,
           'Title' : None,
           'ConstituentID': None,
           'Medium': None,
           'Dimensions': None,
           'CreditLine': None,
           'Classification': None,
           'Department': None,
           'DateAcquired': None,
           'URL': None
           }

    new['ConstituentID'] = lt.newList(tipo)

    return new

def addArtist(catalog, artist):

    lt.addLast(catalog["Artist"], artist)



def GetArtistas(catalog, inicial, final, tipo):

    en_rango = lt.newList(tipo)
    artistas  = lt.iterator(catalog["Artist"])


    for artista in artistas:
        Date = int(artista["BeginDate"]) 
        if (Date >= inicial) and (Date <= final):
            lt.addLast(en_rango, artista)

    sa.sort(en_rango, compareBeginDate)

    return en_rango


def GetArtwork(catalog, inicial, final, size, sort, tipo):
    sub_list = lt.subList(catalog["Artwork"], 1, size)
    sub_list = sub_list.copy()
    en_rango = lt.newList(tipo)
    obras = lt.iterator(sub_list)

    for obra in obras:
        Date = int(obra["DateAcquired"].replace("-", ""))
        if (Date >= inicial) and (Date <= final):
            lt.addLast(en_rango, obra)

    if sort == "ins":
        start_time = time.process_time()
        ins.sort(en_rango, cmpArtworkByDateAcquired)
        stop_time = time.process_time()

    elif sort == "sa":
        start_time = time.process_time()
        sa.sort(en_rango, cmpArtworkByDateAcquired)
        stop_time = time.process_time()

    elif sort == "me":
        start_time = time.process_time()
        me.sort(en_rango, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
        
    elif sort == "qs":
        start_time = time.process_time()
        qs.sort(en_rango, cmpArtworkByDateAcquired)
        stop_time = time.process_time()

    elapsed_rime_msg = (stop_time - start_time)*1000

    return elapsed_rime_msg, en_rango

def buscar_artist(ids,catalog,tipo):
    #sa.sort(catalog["Artist"], cmpids)
    nombres= lt.newList(tipo)
    artistas  = lt.iterator(catalog["Artist"])
    byecorchetes = ids.replace("[","")
    byecorchetedos = byecorchetes.replace("]","")
    authors = byecorchetedos.split(",")

    for id in authors:
        comp=int(id)
        for artista in artistas:
            posid = int(artista["ConstituentID"])
            #posauthor = lt.isPresent(nombres, artista["DisplayName"])
            #if posauthor==0:
            if comp==posid:
                lt.addLast(nombres, artista["DisplayName"])
        #aut= lt.getElement(catalog["Artist"], binary_search(catalog["Artist"], id))

    return nombres

def binary_search(arr, x):
    # Esta sección de codigo fue inspirada en: https://www.geeksforgeeks.org/python-program-for-binary-search/
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        elem=lt.getElement(arr, mid)
        if elem["ConstituentID"] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif elem["ConstituentID"] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1

def compareBeginDate(artist1, artist2):

    return (int(artist1["BeginDate"])) < (int(artist2["BeginDate"]))

def cmpArtworkByDateAcquired(Artwork1, Artwork2):

    return (int(Artwork1["DateAcquired"].replace("-", ""))) < (int(Artwork2["DateAcquired"].replace("-", "")))

def cmpids(id1, id2):
    return (int(id1["ConstituentID"])<int(id2["ConstituentID"]))


# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento