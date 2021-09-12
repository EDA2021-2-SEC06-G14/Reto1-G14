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



def GetArtistas(catalog, inicial, final):

    en_rango = lt.newList()
    artistas  = lt.iterator(catalog["Artist"])


    for artista in artistas:
        Date = int(artista["BeginDate"]) 
        if (Date >= inicial) and (Date <= final):
            lt.addLast(en_rango, artista)

    sa.sort(en_rango, compareBeginDate)

    return en_rango


def GetArtwork(catalog, inicial, final, size, sort):
    sub_list = lt.subList(catalog["Artwork"], 1, size)
    en_rango = lt.newList()
    obras = lt.iterator(sub_list)

    for obra in obras:

        if obra["DateAcquired"] != "":
            Date = int(obra["DateAcquired"].replace("-", ""))
        else:
            Date = 0
        
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


def compareBeginDate(artist1, artist2):

    return (int(artist1["BeginDate"])) < (int(artist2["BeginDate"]))

def cmpArtworkByDateAcquired(Artwork1, Artwork2):

    return (int(Artwork1["DateAcquired"].replace("-", ""))) < (int(Artwork2["DateAcquired"].replace("-", "")))

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento