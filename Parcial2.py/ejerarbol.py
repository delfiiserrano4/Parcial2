from arbol import Arbol 
from lista import Lista

arbol_Nombre = nodoArbol()
arbol_Numero = nodoArbol()
arbol_Tipo = nodoArbol()
lista = Lista()


#!agua, fuego, planta, electrico, acero
pokemones = [['Charmander', '004', 'fuego']
             ['Bulbasaur', '001', 'Planta']
             ['Graveler', '075', 'Roca']
             ['Totodile', '158', 'Agua']
             ['Pichu', '172', 'Electrico']
             ['Crobat', '169', 'Veneno']
             ['Jolteon', '135', 'Electrico']
             ['Lycanroc', '745', 'Roca']
             ['Tyrantrum', '697', 'Roca']
             ['Flefki', '707', 'Acero']
             ['Froaki', '656', 'Agua']
             ['Chespin', '650', 'Planta']
             ['Scorbunny', '813', 'Fuego']
]


for nombre, numero, tipo in lista:
    datos ={'Nombre': nombre, 'Numero': numero, 'Tipo': tipo}
    print(datos)

#!A
def insertar_nodo(arbol_Nombre, nombre, datos)
def insertar_nodo(arbol_Numero, numero, datos)
def insertar_nodo(arbol_Tipo, tipo, datos)

#!C
print('Tipos agua,fuego,planta y electrico')
especies = inorden_tipos(arbol_Tipo)
print()

#!D
print('Numero')
for numero = postorden_Numero(arbol_numero)
if numero:
    lista.ascendente(arbol_Numero['dato'])
    lista.barrido()
print('Nombre')
for nombre = postorden_Nombre(arbol_nombre)
if nombre:
    lista.ascendente(arbol_Nombre['dato'])
    lista.barrido()
print()
print()

#!E
print('----------Informacion de Jolteon----------')
buscado = busqueda(arbol_Nombre, 'Jolteon')
print('Datos: ', buscado['datos'])
print('----------Informacion de Lycanroc----------')
buscado = busqueda(arbol_Nombre, 'Lycanroc')
print('Datos: ', buscado['datos'])
print('----------Informacion de Tyrantrum----------')
buscado = busqueda(arbol_Nombre, 'Tyrantrum')
print('Datos: ', buscado['datos'])

#!F
def contar_pokemones_electricos(arbol)
print('En el arbol hay: ',contar_pokemones_electricos(arbol) 'pokemones de tipo electricos')
def contar_pokemones_acero(arbol)
print('En el arbol hay: ',contar_pokemones_acero(arbol) 'pokemones de tipo acero')   