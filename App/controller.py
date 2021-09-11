﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadObras(catalog)
    loadArtistas(catalog)
    

def loadObras(catalog):
    """
    Carga las obras 
    """
    Artworksfile = cf.data_dir + "MoMA/Artworks-utf8-small.csv"
    inputfile = csv.DictReader(open(Artworksfile, encoding='utf8'))
    for artwork in inputfile:
        model.addArtwork(catalog, artwork)

    

def loadArtistas(catalog):
    """
    Carga los artistas
    """
    Artistfile = cf.data_dir + "MoMA/Artists-utf8-small.csv"
    inputfile = csv.DictReader(open(Artistfile, encoding = "utf8"))
    for artist in inputfile:
        model.addArtist(catalog, artist)

# Funciones de ordenamiento

def GetArtistas(catalog, inicial, final):
    """
    Encontrar los artistas en un rango de anos     
    """
    Artistas = model.GetArtistas(catalog, inicial, final)

    return Artistas

# Funciones de consulta sobre el catálogo
