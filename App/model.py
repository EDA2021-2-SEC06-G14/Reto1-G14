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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de . Crea dos listas vacias, una para las obras 
    y otro para los artistas
    """
    catalog = {'Artwork': None,
               'Artist': None}

    catalog['Artwork'] = lt.newList()
    catalog["Artist"] = lt.newList()

    return catalog

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):
    """
    Carga solo la informacion necesaria al catalogo
    """
    new = newArtwork()

    for key in new.keys():
        new[key] = artwork[key]

    lt.addLast(catalog["Artwork"], new)

def newArtwork():
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
           }

    new['ConstituentID'] = lt.newList()

    return new

def addArtist(catalog, artist):

    new = newArtist()

    for key in new.keys():
        new[key] = artist[key]

    lt.addLast(catalog["Artist"], new)


def newArtist():
    """
    Crea un nuevo diccionario para cada artista
    """
    new = {'ConstituentID': None,
           'DisplayName': None,
           'Nationality': None,
           'Gender': None,
           'BeginDate': None,
           'EndDate': None
           }
    return new



# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento