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

from DISClib.DataStructures.arraylist import getElement
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
import config as cf
assert cf



def newCatalogA():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'Artists': None,
               'Artworks': None,
               'Artists_Artworks':None}

    catalog['Artists'] = lt.newList('ARRAY_LIST')
    catalog['Artworks'] = lt.newList('ARRAY_LIST')
    catalog['Artists_Artworks'] = lt.newList('ARRAY_LIST')


    return catalog

def newCatalogS():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'Artists': None,
               'Artworks': None,}

    catalog['Artists'] = lt.newList('SINGLE_LINKED')
    catalog['Artworks'] = lt.newList('SINGLE_LINKED')
    catalog['Artists_Artworks'] = lt.newList('SINGLE_LINKED')


    return catalog
# Funciones para agregar informacion al catalogo

def addArtists(catalog, artist):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['Artists'], artist)
    # Se obtienen los autores del libro
    # ID = artist['Constituent ID']
    
def addArtists_Artworks(catalog, artist):
    artista={
        'ConstituentID':artist['ConstituentID'],
        'DisplayName':artist['DisplayName'],
        'ObjectID':"",
    }
    lt.addLast(catalog['Artists_Artworks'], artista)

#CODIGO DONDE SE AGREGAN LOS OBJETOS A LOS AUTORES!!
def addObject(catalog,work):
    p = work["ConstituentID"]
    byecorchetes = p.replace("[","")
    byecorchetedos = byecorchetes.replace("]","")
    authors = byecorchetedos.split(",")
    for i in authors:
        index = binary_search(catalog['Artists_Artworks'],int(i))
        ele = lt.getElement(catalog['Artists_Artworks'], index)
        viejos = ele["ObjectID"]
        if (viejos == None) or (viejos == ''):
            nuevo = work["ObjectID"]
        else:
         nuevo = viejos+","+work["ObjectID"]
        i_insert={
            'ConstituentID':ele['ConstituentID'],
            'DisplayName':ele['DisplayName'],
            'ObjectID':nuevo,
        }
        lt.changeInfo(catalog['Artists_Artworks'], index, i_insert)
    

def sortAux(catalog):
    ordenado = sa.sort(catalog['Artists_Artworks'],cmpFunctionIndice)
    return ordenado

def addArtworks(catalog, artwork):
    # Se adiciona el libro a la lista de libros
    obra = {
        'ObjectID':artwork['ObjectID'],
        'ConstituentID':artwork['ConstituentID'],
        'Title':artwork['Title'],
        'Medium':artwork['Medium'],
        'Dimensions':artwork['Dimensions'],
        'CreditLine':artwork['CreditLine'],
        'DateAcquired':artwork['DateAcquired'],
        'Department':artwork['Department'],
        'URL':artwork['URL'],
        'Height (cm)':artwork['Height (cm)'],
        'Length (cm)':artwork['Length (cm)'],
        'Weight (kg)':artwork['Weight (kg)'],
        'Width (cm)':artwork['Width (cm)'],
        'Classification':artwork['Classification']
    }
    lt.addLast(catalog['Artworks'], obra)

def binary_search(arr, x):
    low = 0
    high = lt.size(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
        comp= lt.getElement(arr,mid)
        ahorasi=int(comp["ConstituentID"])
 
        # If x is greater, ignore left half
        if ahorasi < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif ahorasi > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1

    # Se obtienen los autores del libro
    # ID = artist['Constituent ID']
def funcionReqUno(catalog,minimo,maximo):
    ordenado = sa.sort(catalog['Artists'],cmpFunctionRuno)
    indexmin = binary_search_min(ordenado, int(minimo))
    indexmax = binary_search_max(ordenado, int(maximo))
    cant= indexmax-indexmin
    la_lista = lt.subList(ordenado, indexmin,cant)
    return la_lista


def binary_search_max(arr, x):
    """
    CODIGO SACADO DE: https://www.geeksforgeeks.org/python-program-for-binary-search/
    https://stackoverflow.com/questions/13197552/using-binary-search-with-sorted-array-with-duplicates
    """
    low = 0
    high = lt.size(arr) - 1
    mid = 0
    rta=0
 
    while low <= high:
 
        mid = int((high - low) / 2 + low)
        ele=lt.getElement(arr, mid)
 
        # If x is greater, ignore left half
        if int(ele["BeginDate"]) > x:
            high = mid - 1
 
        # If x is smaller, ignore right half
        elif int(ele["BeginDate"]) == x:
            rta=mid
            low = mid + 1
        else:
            low = mid + 1
    if rta == 0:
        rta= mid+2
    return rta

def binary_search_min(arr, x):
    """
    CODIGO SACADO DE: https://www.geeksforgeeks.org/python-program-for-binary-search/
    https://stackoverflow.com/questions/13197552/using-binary-search-with-sorted-array-with-duplicates
    """
    low = 0
    high = lt.size(arr) - 1
    mid = 0
    rta=0
 
    while low <= high:
 
        mid = int((high - low) / 2 + low)
        ele=lt.getElement(arr, mid)
 
        # If x is greater, ignore left half
        if int(ele["BeginDate"]) > x:
            high = mid - 1
 
        # If x is smaller, ignore right half
        elif int(ele["BeginDate"]) == x:
            rta=mid
            high = mid - 1
        else:
            low = mid + 1
    if rta == 0:
        rta=mid
    return rta

def funcionReqDos(catalog, minimo, maximo):
    mini= minimo[0:4]+minimo[5:7]+minimo[8:10]
    maxi= maximo[0:4]+maximo[5:7]+maximo[8:10]
    mini = int(mini)
    maxi = int(maxi)
    ordenado = sa.sort(catalog['Artworks'],cmpFunctionRdos)
    indexmin = binary_search_min2(ordenado, int(mini))
    indexmax = binary_search_max2(ordenado, int(maxi))
    cant= indexmax-indexmin
    la_lista = lt.subList(ordenado, indexmin,cant)
    la_rta= lt.newList("ARRAY_LIST")
    for n in range(1,lt.size(la_lista)+1):
        elemento= lt.getElement(la_lista,n)
        buscar= elemento["ConstituentID"]
        byecorchetes = buscar.replace("[","")
        byecorchetedos = byecorchetes.replace("]","")
        authors = byecorchetedos.split(",")
        autores=""
        for x in authors:
            index = binary_search(catalog['Artists_Artworks'],int(x))
            ele = lt.getElement(catalog['Artists_Artworks'], index)
            autores = autores +"-"+ ele['DisplayName'] + "-"
        agregar = {
            'ObjectID':elemento['ObjectID'],
            'Title':elemento['Title'],
            'Artists':autores,
            'Medium':elemento['Medium'],
            'Dimensions':elemento['Dimensions'],
            'DateAcquired':elemento['DateAcquired'],
            'URL':elemento['URL']
        }
        lt.addLast(la_rta,agregar)
    return la_rta

def funcionReqTres(catalog, nombre):
    index = normal_search_nombre(catalog['Artists_Artworks'],nombre)
    if index != (-1):
        autor = lt.getElement(catalog['Artists_Artworks'],index)
        objetos = autor["ObjectID"]
        if (objetos==None) or (objetos==''):
            vacio = "NOHAYOBRAS"
            tupla = vacio,vacio
            return tupla
        else:
            lt_objetos = objetos.split(",")
            ordenado = sa.sort(catalog["Artworks"], cmpobjectid)
            tad_objetos = lt.newList("ARRAY_LIST")
            tad_medios = lt.newList("ARRAY_LIST",cmpfunction=comparemedio)
            for i in lt_objetos:
                index = binary_search_id(ordenado, i)
                elemento = lt.getElement(ordenado, index)
                agregar = {
                    'ObjectID':elemento['ObjectID'],
                    'Title':elemento['Title'],
                    'Medium':elemento['Medium'],
                    'Dimensions':elemento['Dimensions'],
                    'DateAcquired':elemento['DateAcquired'],
                    'Department':elemento['Department'],
                    'Classification':elemento['Classification'],
                    'URL':elemento['URL'],
                    'ConstituentID':elemento['ConstituentID']
                }
                lt.addLast(tad_objetos, agregar)
                cambiarTADmedios(tad_medios,elemento['Medium'])
            sa.sort(tad_medios,cmpcount)
            mediorep = lt.getElement(tad_medios, 1)
            rtafinal= lt.newList("ARRAY_LIST")
            objetos  = lt.iterator(tad_objetos)
            for objeto in objetos:
                name = objeto["Medium"]
                if (name == mediorep["Medium"]):
                    lt.addLast(rtafinal, objeto)
            tuplarta= tad_medios,rtafinal
            return tuplarta
            
    else:
        vacio = "NOHAYAUTOR"
        tupla = vacio,vacio
        return tupla



def cambiarTADmedios(arr, x):
    pos = lt.isPresent(arr,x)
    if pos!=0:
        o = lt.getElement(arr,pos)
        coso= int(o["Count"])
        cambio= coso + 1
        cambiodict = {
            'Medium': o["Medium"],
            'Count': cambio
        }
        lt.changeInfo(arr,pos,cambiodict)
    else:
        nuevodict={
            'Medium': x,
            'Count': "1"
        }
        lt.addLast(arr,nuevodict)

def comparemedio(medio, medios):
    if (medio.lower() in medios['name'].lower()):
        return 0
    return -1
        

def normal_search_nombre(arr, x):
    largo  = lt.size(arr)
    for artist in range(1,largo+1):
        artista = lt.getElement(arr,artist)
        name = artista["DisplayName"]
        if (name == x):
            return artist
    return -1

def binary_search_max2(arr, x):
    """
    CODIGO SACADO DE: https://www.geeksforgeeks.org/python-program-for-binary-search/
    https://stackoverflow.com/questions/13197552/using-binary-search-with-sorted-array-with-duplicates
    """
    low = 0
    high = lt.size(arr) - 1
    mid = 0
    rta=0
 
    while low <= high:
 
        mid = int((high - low) / 2 + low)
        ele=lt.getElement(arr, mid)
        e = ele["DateAcquired"]
        if (e!=None) and (e!=""):
            m= e[0:4]+e[5:7]+e[8:10]
            m= int(m)
        else:
            m=0
 
        # If x is greater, ignore left half
        if int(m) > x:
            high = mid - 1
 
        # If x is smaller, ignore right half
        elif int(m) == x:
            rta=mid
            low = mid + 1
        else:
            low = mid + 1
    if rta == 0:
        rta= mid+2
    return rta

def binary_search_min2(arr, x):
    """
    CODIGO SACADO DE: https://www.geeksforgeeks.org/python-program-for-binary-search/
    https://stackoverflow.com/questions/13197552/using-binary-search-with-sorted-array-with-duplicates
    """
    low = 0
    high = lt.size(arr) - 1
    mid = 0
    rta=0
 
    while low <= high:
 
        mid = int((high - low) / 2 + low)
        ele=lt.getElement(arr, mid)
        e = ele["DateAcquired"]
        if (e!=None) and (e!=""):
            m= e[0:4]+e[5:7]+e[8:10]
            m= int(m)
        else:
            m=0
 
        # If x is greater, ignore left half
        if int(m) > x:
            high = mid - 1
 
        # If x is smaller, ignore right half
        elif int(m) == x:
            rta=mid
            high = mid - 1
        else:
            low = mid + 1
    if rta == 0:
        rta= mid+2
    return rta

def binary_search_id(arr, x):
    low = 0
    high = lt.size(arr) - 1
    mid = 0
    xdepurado = x.replace("'","")
    xdep = xdepurado.replace(" ","")
    xint = int(xdep)
 
    while low <= high:
 
        mid = (high + low) // 2
        comp= lt.getElement(arr,mid)
        ahorasi=int(comp["ObjectID"])
 
        # If x is greater, ignore left half
        if ahorasi < xint:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif ahorasi > xint:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1




def cmpFunctionRuno(anouno, anodos):
    return (int(anouno["BeginDate"]) < int(anodos["BeginDate"]))

def cmpobjectid(iduno, iddos):
    return (int(iduno["ObjectID"]) < int(iddos["ObjectID"]))

def cmpFunctionIndice(artist1, artist2):
    return (int(artist1["ConstituentID"]) < int(artist2["ConstituentID"]))

def cmpcount(countuno, countdos):
    return (int(countuno["Count"])> int(countdos["Count"]))

def cmpFunctionRdos(feuno, fedos):
    fechauno= feuno["DateAcquired"]
    fechados = fedos["DateAcquired"]
    if (fechauno!=None) and (fechauno!=""):
        mini= fechauno[0:4]+fechauno[5:7]+fechauno[8:10]
        mini= int(mini)
    else:
        mini=0
    if (fechados!=None) and (fechados!=""):
        maxi= fechados[0:4]+fechados[5:7]+fechados[8:10]
        maxi= int(maxi)
    else:
        maxi=0
    return (int(mini) < int(maxi))