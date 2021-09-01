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
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
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

    LoadID(new, artwork)
    LoadTitle(new, artwork)
    LoadConstituent(new, artwork)
    LoadMedium(new, artwork)
    LoadAcquired(new, artwork)
    LoadDimensions(new, artwork)

    lt.addLast(catalog["Artwork"], new)

def newArtwork():
    """
    Se crea un diccionario par cada obra
    """
    new = {'ID' : None,
           'Title' : None,
           'Constituent ID': None,
           'Medium': None,
           'Department': None,
           'Date_Acquired': None,
           'Dimensions': None}

    new['Constituent ID'] = lt.newList()

    return new

def LoadID(new, artwork):
    """
    Carga el ID de la obra
    """
    new["ID"] = artwork["ObjectID"]

def LoadTitle(new, artwork):
    """
    Carga el titulo de la obra
    """
    new["Title"] = artwork["Title"]

def LoadConstituent(new, artwork):
    """
    Carga los artistas de la obra
    """
    const = artwork["ConstituentID"].strip(" ").strip("[]").split(',')

    for i in const:
        lt.addLast(new['Constituent ID'], i)

def LoadMedium(new, artwork):
    """
    Carga la tecnica de la obra
    """
    new["Medium"] = artwork["Medium"]

def LoadDepartment(new, artwork):
    """
    carga el departamento en el que esta la obra
    """
    new["Department"] = artwork["Department"]

def LoadAcquired(new, artwork):
    """
    Carga fecha de adquisicion de la obra 
    """
    new["Date_Acquired"] = artwork["DateAcquired"]

def LoadDimensions(new, artwork):
    new["Dimensions"] = artwork["Dimensions"]

def addArtist(catalog, artist):
    """
    Carga solo la informacion necesaria de los artistas al catalogo
    """
    new = newArtist()

    LoadCont_2(new, artist)
    LoadName(new, artist)
    LoadNationality(new, artist)
    LoadBorn(new, artist)

    lt.addLast(catalog["Artist"], new)

def newArtist():
    """
    Crea un nuevo diccionario para cada artista
    """
    new = {'Constituent ID': None,
           'Display_Name': None,
           'Nationality': None,
           'BeginDate': None}
    return new

def LoadCont_2(new, artist):
    """
    Carga ID del artista
    """
    new["Constituent ID"] = artist["ConstituentID"]

def LoadName(new, artist):
    """
    Carga nombre del artista
    """
    new["Display_Name"] = artist["DisplayName"]

def LoadNationality(new, artist):
    """
    Carga la nacionalidad del artista
    """
    new["Nationality"] = artist["Nationality"]

def LoadBorn(new, artist):
    new["BeginDate"] = artist["BeginDate"]


# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento