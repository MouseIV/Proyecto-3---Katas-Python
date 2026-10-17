from functools import reduce
import math 
import time # Añadido para poder usar time.sleep() y ver los resultados de cada ejercicio de manera pausada.


print("\nEJERCICIO 1")
# Enunciado: Escribe una funcion que reciba una cadena de texto como parametro
# y devuelva un diccionario con las frecuencias de cada letra en la cadena.
# Los espacios no deben ser considerados.
def frecuencia_letras(cadena):
    frecuencias = {}
    for letra in cadena:
        if letra != " ":
            letra = letra.lower()  # ignorar mayusculas
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias

print(frecuencia_letras("Hola Mundo"))
time.sleep(1)


print("\nEJERCICIO 2")
# Enunciado: Dada una lista de numeros, obten una nueva lista con el doble de
# cada valor. Usa la funcion map().
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)
time.sleep(1)


print("\nEJERCICIO 3")
# Enunciado: Escribe una funcion que tome una lista de palabras y una palabra
# objetivo como parametros. La funcion debe devolver una lista con todas las
# palabras de la lista original que contengan la palabra objetivo.
def palabras_que_contienen(lista_palabras, objetivo):
    return [palabra for palabra in lista_palabras if objetivo in palabra]

print(palabras_que_contienen(["python", "java", "javascript", "c++"], "java"))
time.sleep(1)


print("\nEJERCICIO 4")
# Enunciado: Genera una funcion que calcule la diferencia entre los valores de
# dos listas. Usa la funcion map().
def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

print(diferencia_listas([10, 20, 30], [1, 2, 3]))
time.sleep(1)


print("\nEJERCICIO 5")
# Enunciado: Escribe una funcion que tome una lista de numeros como parametro y
# un valor opcional nota_aprobado (por defecto 5). La funcion debe calcular la
# media de los numeros en la lista y determinar si la media es mayor o igual que
# nota_aprobado. Si es asi, el estado sera "aprobado"; de lo contrario,
# "suspenso". La funcion debe devolver una tupla que contenga la media y el estado.
def media_y_estado(numeros, nota_aprobado=5):
    if not numeros:
        return (0, "suspenso")
    media = sum(numeros) / len(numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

print(media_y_estado([4, 6, 8, 5]))
print(media_y_estado([3, 4, 2], nota_aprobado=6))
time.sleep(1)


print("\nEJERCICIO 6")
# Enunciado: Escribe una funcion que calcule el factorial de un numero de manera
# recursiva.
def factorial(n):
    if n < 0:
        raise ValueError("El factorial no esta definido para numeros negativos")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
time.sleep(1)


print("\nEJERCICIO 7")
# Enunciado: Genera una funcion que convierta una lista de tuplas a una lista de
# strings. Usa la funcion map().
def tuplas_a_strings(lista_tuplas):
    return list(map(lambda t: " ".join(str(x) for x in t), lista_tuplas))

print(tuplas_a_strings([("Hola", "mundo"), (1, 2, 3)]))
time.sleep(1)


print("\nEJERCICIO 8")
# Enunciado: Escribe un programa que pida al usuario dos numeros e intente
# dividirlos. Si el usuario ingresa un valor no numerico o intenta dividir por
# cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando
# si la division fue exitosa o no.
def dividir():
    try:
        a = input("Introduce el primer numero: ")
        b = input("Introduce el segundo numero: ")
        resultado = float(a) / float(b)
        print(f"Division exitosa: {resultado}")
    except ValueError:
        print("Error: Debes introducir valores numericos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

dividir()
time.sleep(1)


print("\nEJERCICIO 9")
# Enunciado: Escribe una funcion que tome una lista de nombres de mascotas como
# parametro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en
# Espana. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Piton",
# "Cocodrilo", "Oso"]. Usa la funcion filter().
def filtrar_mascotas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Piton", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, lista_mascotas))

print(filtrar_mascotas(["Perro", "Gato", "Tigre", "Conejo", "Oso"]))
time.sleep(1)


print("\nEJERCICIO 10")
# Enunciado: Escribe una funcion que reciba una lista de numeros y calcule su
# promedio. Si la lista esta vacia, lanza una excepcion personalizada y maneja
# el error adecuadamente.
class ListaVaciaError(Exception):
    pass

def promedio(lista):
    if not lista:
        raise ListaVaciaError("La lista esta vacia, no se puede calcular el promedio.")
    return sum(lista) / len(lista)

try:
    print(promedio([10, 20, 30]))
    print(promedio([]))
except ListaVaciaError as e:
    print(f"Error: {e}")
time.sleep(1)


print("\nEJERCICIO 11")
# Enunciado: Escribe un programa que pida al usuario que introduzca su edad.
# Si el usuario ingresa un valor no numerico o un valor fuera del rango esperado
# (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")
        print(f"Edad valida: {edad}")
    except ValueError as e:
        print(f"Error: {e}")

pedir_edad()
time.sleep(1)


print("\nEJERCICIO 12")
# Enunciado: Genera una funcion que, al recibir una frase, devuelva una lista
# con la longitud de cada palabra. Usa la funcion map().
def longitudes_palabras(frase):
    return list(map(len, frase.split()))

print(longitudes_palabras("Hola mundo Python"))
time.sleep(1)


print("\nEJERCICIO 13")
# Enunciado: Genera una funcion que, para un conjunto de caracteres, devuelva
# una lista de tuplas con cada letra en mayusculas y minusculas. Las letras no
# pueden estar repetidas. Usa la funcion map().
def mayus_minus(caracteres):
    unicos = sorted(set(caracteres.lower()))  # eliminamos repetidos y ordenamos
    return list(map(lambda c: (c.upper(), c.lower()), unicos))

print(mayus_minus("aAbBcC"))
time.sleep(1)


print("\nEJERCICIO 14")
# Enunciado: Crea una funcion que retorne las palabras de una lista que comiencen
# con una letra en especifico. Usa la funcion filter().
def palabras_que_empiezan(lista, letra):
    return list(filter(lambda p: p.lower().startswith(letra.lower()), lista))

print(palabras_que_empiezan(["Python", "Java", "Javascript", "C++"], "j"))
time.sleep(1)


print("\nEJERCICIO 15")
# Enunciado: Crea una funcion lambda que sume 3 a cada numero de una lista dada.
numeros = [1, 2, 3, 4]
resultado = list(map(lambda x: x + 3, numeros))
print(resultado)
time.sleep(1)


print("\nEJERCICIO 16")
# Enunciado: Escribe una funcion que tome una cadena de texto y un numero entero
# n como parametros y devuelva una lista de todas las palabras que sean mas
# largas que n. Usa la funcion filter().
def palabras_largas(cadena, n):
    return list(filter(lambda p: len(p) > n, cadena.split()))

print(palabras_largas("El gato negro corre rapido", 4))
time.sleep(1)


print("\nEJERCICIO 17")
# Enunciado: Crea una funcion que tome una lista de digitos y devuelva el numero
# correspondiente. Por ejemplo, [5,7,2] corresponde al numero 572.
# Usa la funcion reduce().
def digitos_a_numero(digitos):
    return reduce(lambda acc, d: acc * 10 + d, digitos)

print(digitos_a_numero([5, 7, 2]))
time.sleep(1)


print("\nEJERCICIO 18")
# Enunciado: Escribe un programa en Python que cree una lista de diccionarios
# con informacion de estudiantes (nombre, edad, calificacion) y use filter para
# extraer a los estudiantes con una calificacion mayor o igual a 90.
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 88},
    {"nombre": "Maria", "edad": 21, "calificacion": 92},
    {"nombre": "Pedro", "edad": 19, "calificacion": 75},
]

aprobados = list(filter(lambda e: e["calificacion"] >= 90, estudiantes))
print(aprobados)
time.sleep(1)


print("\nEJERCICIO 19")
# Enunciado: Crea una funcion lambda que filtre los numeros impares de una lista
# dada.
numeros = [1, 2, 3, 4, 5, 6, 7]
impares = list(filter(lambda x: x % 2 != 0, numeros))
print(impares)
time.sleep(1)


print("\nEJERCICIO 20")
# Enunciado: Para una lista con elementos de tipo integer y string, obten una
# nueva lista solo con los valores int. Usa la funcion filter().
mixta = [1, "hola", 3.5, 4, "mundo", 7, True, False]
solo_int = list(filter(lambda x: type(x) is int, mixta))  # evita capturar bool
print(solo_int)
time.sleep(1)


print("\nEJERCICIO 21")
# Enunciado: Crea una funcion que calcule el cubo de un numero dado mediante
# una funcion lambda.
cubo = lambda x: x ** 3
print(cubo(5))
time.sleep(1)


print("\nEJERCICIO 22")
# Enunciado: Dada una lista numerica, obten el producto total de los valores.
# Usa la funcion reduce().
numeros = [1, 2, 3, 4]
producto = reduce(lambda x, y: x * y, numeros)
print(producto)
time.sleep(1)


print("\nEJERCICIO 23")
# Enunciado: Concatena una lista de palabras. Usa la funcion reduce().
palabras = ["Hola", "mundo", "Python"]
resultado = reduce(lambda x, y: x + " " + y, palabras)
print(resultado)
time.sleep(1)


print("\nEJERCICIO 24")
# Enunciado: Calcula la diferencia total en los valores de una lista.
# Usa la funcion reduce().
numeros = [100, 20, 30, 10]
diferencia = reduce(lambda x, y: x - y, numeros)
print(diferencia)  # 100-20-30-10 = 40
time.sleep(1)


print("\nEJERCICIO 25")
# Enunciado: Crea una funcion que cuente el numero de caracteres en una cadena
# de texto dada.
def contar_caracteres(cadena):
    return len(cadena)

print(contar_caracteres("Hola mundo"))
time.sleep(1)


print("\nEJERCICIO 26")
# Enunciado: Crea una funcion lambda que calcule el resto de la division entre
# dos numeros dados.
resto = lambda a, b: a % b
print(resto(17, 5))
time.sleep(1)


print("\nEJERCICIO 27")
# Enunciado: Crea una funcion que calcule el promedio de una lista de numeros.
def calcular_promedio(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

print(calcular_promedio([10, 20, 30]))
time.sleep(1)


print("\nEJERCICIO 28")
# Enunciado: Crea una funcion que busque y devuelva el primer elemento
# duplicado en una lista dada.
def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None  # no hay duplicados

print(primer_duplicado([1, 2, 3, 2, 4, 5]))
time.sleep(1)


print("\nEJERCICIO 29")
# Enunciado: Crea una funcion que convierta una variable en una cadena de texto
# y enmascare todos los caracteres con el caracter '#' excepto los ultimos cuatro.
def enmascarar(valor):
    s = str(valor)
    if len(s) <= 4:
        return s
    return "#" * (len(s) - 4) + s[-4:]

print(enmascarar("1234567890"))
print(enmascarar(987654321))
time.sleep(1)


print("\nEJERCICIO 30")
# Enunciado: Crea una funcion que determine si dos palabras son anagramas, es
# decir, si estan formadas por las mismas letras pero en diferente orden.
def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

print(son_anagramas("amor", "roma"))
print(son_anagramas("hola", "adios"))
time.sleep(1)


print("\nEJERCICIO 31")
# Enunciado: Crea una funcion que solicite al usuario ingresar una lista de
# nombres y luego un nombre para buscar en esa lista. Si el nombre esta en la
# lista, imprime un mensaje indicando que fue encontrado; de lo contrario,
# lanza una excepcion.
def buscar_nombre():
    lista_nombres = input("Introduce una lista de nombres separados por comas: ")
    nombre_buscar = input("Introduce el nombre a buscar: ")
    nombres = [n.strip() for n in lista_nombres.split(",")]
    if nombre_buscar in nombres:
        print(f"!{nombre_buscar} fue encontrado!")
    else:
        raise ValueError(f"El nombre '{nombre_buscar}' no esta en la lista.")

try:
    buscar_nombre()
except ValueError as e:
    print(f"Error: {e}")
time.sleep(1)


print("\nEJERCICIO 32")
# Enunciado: Crea una funcion que tome un nombre completo y una lista de
# empleados, busque el nombre en la lista y devuelva el puesto del empleado si
# se encuentra; de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aqui.
def buscar_puesto(nombre_completo, lista_empleados):
    for empleado in lista_empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    return f"{nombre_completo} no trabaja aqui."

empleados = [
    {"nombre": "Ana Garcia", "puesto": "Desarrolladora"},
    {"nombre": "Luis Perez", "puesto": "Disenador"},
]

print(buscar_puesto("Ana Garcia", empleados))
print(buscar_puesto("Pedro Lopez", empleados))
time.sleep(1)


print("\nEJERCICIO 33")
# Enunciado: Crea una funcion lambda que sume elementos correspondientes de dos
# listas dadas.
suma_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))
print(suma_listas([1, 2, 3], [4, 5, 6]))
time.sleep(1)


print("\nEJERCICIO 34")
# Enunciado: Crea la clase Arbol
# - Define un arbol generico con un tronco y ramas como atributos.
# - Metodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama,
#   info_arbol.
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [r + 1 for r in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posicion invalida")

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

# Caso de uso
arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)
print(arbol.info_arbol())
time.sleep(1)


print("\nEJERCICIO 35")
# Enunciado: Crea la clase UsuarioBanco
# - Representa a un usuario de un banco con su nombre, saldo y si tiene o no
#   cuenta corriente.
# - Metodos: retirar_dinero, transferir_dinero, agregar_dinero.
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente=True):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo.")
        self.saldo -= cantidad
        print(f"{self.nombre} retiro {cantidad}. Saldo actual: {self.saldo}")

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para transferir.")
        self.saldo -= cantidad
        otro_usuario.saldo += cantidad
        print(f"{self.nombre} transfirio {cantidad} a {otro_usuario.nombre}")

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"{self.nombre} agrego {cantidad}. Saldo actual: {self.saldo}")

# Caso de uso
alicia = UsuarioBanco("Alicia", 100)
bob = UsuarioBanco("Bob", 50)

bob.agregar_dinero(20)
bob.agregar_dinero(30)
bob.transferir_dinero(alicia, 80)
alicia.retirar_dinero(50)
time.sleep(1)


print("\nEJERCICIO 36")
# Enunciado: Crea una funcion llamada procesar_texto
# - Procesa un texto segun la opcion especificada: contar_palabras,
#   reemplazar_palabras o eliminar_palabra.
def contar_palabras(texto):
    palabras = texto.lower().split()
    contador = {}
    for p in palabras:
        contador[p] = contador.get(p, 0) + 1
    return contador

def reemplazar_palabras(texto, original, nueva):
    return texto.replace(original, nueva)

def eliminar_palabra(texto, palabra):
    return " ".join(p for p in texto.split() if p != palabra)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        return "Opcion no valida"

texto = "el gato negro y el perro blanco"
print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "gato", "felino"))
print(procesar_texto(texto, "eliminar", "el"))
time.sleep(1)


print("\nEJERCICIO 37")
# Enunciado: Genera un programa que nos indique si es de noche, de dia o de
# tarde segun la hora proporcionada por el usuario.
def momento_del_dia():
    try:
        hora = int(input("Introduce la hora (0-23): "))
        if not 0 <= hora <= 23:
            print("Hora fuera de rango")
            return
        if 6 <= hora < 12:
            print("Es de manana / dia")
        elif 12 <= hora < 20:
            print("Es de tarde")
        else:
            print("Es de noche")
    except ValueError:
        print("Debes introducir un numero entero")

momento_del_dia()
time.sleep(1)


print("\nEJERCICIO 38")
# Enunciado: Escribe un programa que determine que calificacion en texto tiene
# un alumno segun su calificacion numerica.
# Reglas:
#   0 - 69: insuficiente
#   70 - 79: bien
#   80 - 89: muy bien
#   90 - 100: excelente
def calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"
    else:
        return "Nota fuera de rango"

print(calificacion_texto(85))
time.sleep(1)


print("\nEJERCICIO 39")
# Enunciado: Escribe una funcion que tome dos parametros: figura (una cadena
# que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con
# los datos necesarios para calcular el area de la figura).
def calcular_area(figura, datos):
    figura = figura.lower()
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        radio, = datos
        return math.pi * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        return "Figura no reconocida"

print(calcular_area("rectangulo", (5, 3)))
print(calcular_area("circulo", (4,)))
print(calcular_area("triangulo", (6, 4)))
time.sleep(1)


print("\nEJERCICIO 40")
# Enunciado: Escribe un programa en Python que utilice condicionales para
# determinar el monto final de una compra en una tienda en linea, despues de
# aplicar un descuento.
def calcular_precio_final():
    try:
        precio = float(input("Introduce el precio del producto: "))
        tiene_cupon = input("¿Tienes cupon de descuento? (si/no): ").lower()

        if tiene_cupon in ["si", "s"]:
            descuento = float(input("Introduce el valor del descuento: "))
            if descuento > 0:
                precio_final = precio - descuento
                if precio_final < 0:
                    precio_final = 0
                print(f"Precio final con descuento: {precio_final:.2f}")
            else:
                print("El valor del cupon debe ser mayor que cero.")
                print(f"Precio final sin descuento: {precio:.2f}")
        else:
            print(f"Precio final sin descuento: {precio:.2f}")
    except ValueError:
        print("Error: introduce valores numericos validos.")

calcular_precio_final()