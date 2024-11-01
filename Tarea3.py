import copy as cp
import random
from functools import reduce
import os
import shutil

# Clonar lista
lista = ["Samu", "Ainhoa", "Jon", "Maria", "Alex"]
lista2 = lista.copy()
print(f"Lista 1: {lista}\nLista 2: {lista2}")

"""
¿Cuál es la diferencia en Python entre “shallow copy” y “deep copy”?

La diferencia es que el shallow copy(copia superficial) copia la instancia del objeto original pero no copia los objetos anidados, sino que hace referencia a ellos, 
de manera que si por ejemplo modificas una lista en la copia también lo hace en la original. Sin embargo, la deep copy(copia profunda) hace una copia de la instancia del 
objeto original y de los objetos anidados, de forma que si por ejemplo modificas una lista en la copia no lo hace en la original.
"""

# Añadir un elemento a la lista

lista = ["Samu", "Ainhoa", "Jon", "Maria", "Alex"]
lista.append("Jon")
print(f"Lista: {lista}")

# Eliminar un elemento de la lista

lista = ["Samu", "Ainhoa", "Jon", "Maria", "Alex"]
lista.remove("Jon")
print(f"Lista: {lista}")

# Crear una nueva lista con los 4 últimos elementos de una lista.

lista = ["Samu", "Ainhoa", "Jon", "Maria", "Alex", "Jonay", "Javier", "Jonatan"]
lista2 = lista[-4:]
print(f"Lista 2: {lista2}")

# Convertir las palabras de una cadena (separadas por espacios) en una lista.

cadena = "Hola me llamo Samu"
lista = cadena.split()
print(f"Lista: {lista}")

# Como ya estoy haciendo en esta misma línea, los comentarios en línea se ponen con el # al principio de esta

"""

Como estoy haciendo en este mismo comentario, los comentarios multilínea se ponen con tres comillas dobles para abrir y cerrar

"""


#Ejercicio 2

# Reciban 2 números y devuelvan la suma

def suma(numero1, numero2):
    return numero1 + numero2

print(suma(1, 5))

"""
Reciban una lista y modifiquen esa misma lista (referencia) duplicando los valores de todos los elementos. No debe devolver nada. Reciban una lista y devuelvan una 
copia de esa misma lista (referencia) duplicando los valores de todos los elementos. La lista original no debe modificarse.
"""

def shallowCopy():
    lista1 = [[1, 2, 3], [4, 5, 6]]
    lista2 = cp.copy(lista1)

    lista2[0][0] = 10

    return lista1, lista2

print(shallowCopy())

def deepCopy():
    lista1 = [[1, 2, 3], [4, 5, 6]]
    lista2 = cp.deepcopy(lista1)

    lista2[0][0] = 10

    return lista1, lista2

print(deepCopy())

"""
A partir de un contexto donde queremos almacenar un usuario y su contraseña, haz un ejemplo que explique cómo se haría:

Usando una lista. Usando un diccionario. Al llenarse, las contraseñas deben pasarse a un formato Hash (por ejemplo, SHA-512). El ejemplo debe llenar la lista con 
5 usuarios/contraseña y hacer dos consultas.
"""

#Usando una lista

listaUsuarios = ["Samu", "Jose", "María", "Ainhoa", "David"]
listsaContrasenas = ["1234", "0000", "4321", "1111", "5555"]
nuevoUsuario = input("Ingrese un nuevo usuario: ")
nuevaContrasena = input("Ingrese una contraseña: ")
listaUsuarios.append(nuevoUsuario)
listsaContrasenas.append(nuevaContrasena)
print(f"Lista de usuarios: {listaUsuarios}\nLista de contraseñas: {listsaContrasenas}")
usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")
for usuarioActual in listaUsuarios:
    if usuarioActual == usuario:
        posicion = listaUsuarios.index(usuarioActual)
        if listsaContrasenas[posicion] == contrasena:
            print("Bienvenido")
        else:
            print("Contraseña incorrecta")

#  Usando un diccionario

usuarios = [
    {
        "nombre": "Samu",
        "contrasena": "1234"
    },
    {
        "nombre": "Jose",
        "contrasena": "0000"
    },
    {
        "nombre": "María",
        "contrasena": "4321"
    },
    {
        "nombre": "Ainhoa",
        "contrasena": "1111"
    },
    {
        "nombre": "David",
        "contrasena": "5555"
    }
]

nuevoUsuario = input("Ingrese un nuevo usuario: ")
nuevaContrasena = input("Ingrese una nueva contraseña: ")

# Agregar nuevo usuario como un diccionario
usuarios.append({"nombre": nuevoUsuario, "contrasena": nuevaContrasena})
print(f"Lista de usuarios: {usuarios}")

usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")

valido = False

for usuarioActual in usuarios:
    if usuarioActual["nombre"] == usuario and usuarioActual["contrasena"] == contrasena:
        print("Bienvenido")
        valido = True
        break

if not valido:
    print("Usuario o contraseña incorrecta")


# Al llenarse, las contraseñas deben pasarse a un formato Hash (por ejemplo, SHA-512)

contrasena = ["1234", "5678", "Rodrigo123", "contraseñajeje654"]

contrasenaHash = []

for elemento in contrasena:
    contrasenaHash.append(hash(elemento))
print(f"Contraseñas: {contrasena}")
print(f"Contraseñas pasados a Hash: {contrasenaHash}")

# Explica con ejemplos cómo funcionan los operadores “is”, “not”, “in” en Python 3.

variable = True
lista = [variable]

# Si variable es True, entra
if variable is True:
    print("Es True")
else:
    print("No es True")
# Si variable no es True, entra
if variable is not True:
    print("No es True")
else:
    print("Es True")
# Si variable está dentro de la lista, entra
if variable in lista:
    print("Es True")
else:
    print("No es True")
# Si variable no está dentro de la lista, entra
if variable not in lista:
    print("No es True")
else:
    print("Es True")

"""
Pon un ejemplo de cómo pasar varios parámetros desde la consola a un programa Python 3. Pon un ejemplo de cómo hacer “sobrecarga de funciones” 
(funciones que pueden recibir varios números de parámetros), incluyendo el caso en que el número de parámetros no esté definido.
"""

import sys

def main():
  if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
      print(f"Parámetro {i}: {sys.argv[i]}")
  else:
    print("No se pasaron parámetros.")

if __name__ == "__main__":
  main()

"""
Crea una lista en la cual cada elemento de esa lista sea una lista con dos valores: tamaño y peso. Utilizando Key functions, haz que esta lista se ordene por mayor altura y, 
en caso de igualdad, por menor peso. Explica en comentarios qué es realmente la “key function”. Pista: en la ayuda se menciona: 
“El valor del parámetro key debe ser una función (u otro callable) que tome un solo argumento y devuelva una clave para usar con fines de ordenación. 
Esta técnica es rápida porque la función key se llama exactamente una vez por cada registro de entrada.”
https://docs.python.org/3/howto/sorting.html
"""

lista_datos = [
    (1.78, 60),
    (1.89, 77),
    (1.89, 65),
    (1.62, 60),
    (1.57, 55),
    (1.70, 80)
]

lista_numeros = [0,1,23,34,4,4,5,5,3,32,21,1,54,5,2,2,52,9]

# Ordenamos por primer valor y segundo valor de la tupla si hay repetidos del primero, y orden descendente (el reverse False es ascendente)
from operator import itemgetter, attrgetter # attrgetter es para cuando hay objetos (todos del mismo) en la lista
lista_datos_ordenada = sorted(lista_datos, key=itemgetter(0, 1), reverse=True)
print(lista_datos_ordenada)

# Define la clase Car en Python 3. La clase tendrá como atributos “matrícula” (numérica) y “color”. Crea un método imprimir y, además, dos métodos adicionales que elijas.

class Car:
    def __init__(self, matricula, color, velocidad):
        self.matricula = matricula
        self.color = color
        self.velocidad = velocidad

    def imprimir(self):
        print(f"Matrícula: {self.matricula}\nColor: {self.color}\nVelocidad: {self.velocidad} km/h")

    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        if (self.velocidad - 10) >= 0:
            self.velocidad -= 10

car1 = Car(1234, "Rojo", 0)
car1.imprimir()
car1.acelerar()
car1.imprimir()
car1.frenar()
car1.imprimir()

"""
En segundo lugar, haz que el programa pida un número “n” por teclado y se creen “n” instancias de la clase, donde cada instancia: 
Cada “matrícula” tendrá un número consecutivo desde 1 hasta “n”. 
El “color” será para cada instancia un color aleatorio obtenido de esta lista: ["red", "white", "black", "pink", "blue"]. 
Finalmente, el programa deberá imprimir los valores de las 10 primeras instancias. En caso de que “n” sea menor que 10, solo se imprimirán “n” instancias.
"""

listaColores = ["red", "white", "black", "pink", "blue"]

numeroInstancias = int(input("Dame el número de isntancias que quieres crear: "))
for x in range(numeroInstancias + 1):
    matricula = x + 1
    color = random.choice(listaColores)
    velocidad = x + 10
    globals()[f"car{x}"] = Car(matricula, color, velocidad)

if numeroInstancias < 10:
    for coches in range(numeroInstancias):
        globals()[f"car{coches}"].imprimir()
else:
    for coches in range(10):
        globals()[f"car{coches}"].imprimir()

        
"""
Una función lambda en Python es una función pequeña que puede tener cualquier número de parámetros, pero solo puede contener una expresión. 
Se usa cuando para definir una sola línea de código, generalmente para tareas simples y temporales.
"""

suma = lambda x, y: x + y
print(suma(1, 2))

# 

cadena = input("Introduce una cadena de números separados por espacios: ")

# La función map() en Python toma una función y una o más secuencias (como listas, tuplas, etc.)
lista_numeros = list(map(int, cadena.split()))

print("Lista de números enteros:", lista_numeros)

# Usando “filter()”, elimina de la cadena anterior los números menores que 10.

def mayor_igual_10(x):
    return x >= 10

filtro = filter(mayor_igual_10, lista_numeros)

listaResultante = []

for x in filtro:
    listaResultante.append(x)
print(f"Lista resultante: {listaResultante}")

# Con la cadena resultante y usando “reduce()”, devuelve la multiplicación de los elementos de la lista.

print(f"Multiplicación de los elementos de la lista {listaResultante} = {reduce(lambda a, b: a*b, listaResultante)}")

"""
9.- Crea un programa Python 3 que organice los archivos de la carpeta actual. Para cada extensión de archivo, 
el programa moverá todos los archivos con esa extensión a una carpeta con el mismo nombre que la extensión. 
Por ejemplo, una lista con extensiones [“png”, “mp4”, “doc”] moverá los archivos ".png" a una carpeta "png", los ".mp4" a una carpeta "mp4", 
y los ".doc" a una carpeta "doc", si no corresponde la extensión ignorar el archivo. Para distribuir el programa, empaquétalo con PyInstaller.
"""

DIRECTORIO_BASE = os.getcwd()

listaCarpetas = ["mp4", "png", "pdf"]

for carpeta in listaCarpetas:
    existeDirectorio = os.path.exists(os.path.join(DIRECTORIO_BASE, carpeta))
    if not existeDirectorio:
        os.mkdir(carpeta)
        globals()[f"DIRECTORIO_{carpeta}"] = os.path.join(DIRECTORIO_BASE, carpeta)

for archivo in os.listdir(DIRECTORIO_BASE):
    nombre, extension = os.path.splitext(archivo)
    extension = extension[1:]
    for carpeta in listaCarpetas:
        if extension == carpeta:
            posicion = listaCarpetas.index(extension)
            shutil.move(archivo, carpeta)

