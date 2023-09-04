# import this Python Zen
# Set son conjuntos, modificables, sin orden, sim duplicados
# usan las {} como los diccionarios
# No tienen el par clave: valor


set_countries = {"col", "mex", "bol"}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)
# Al imprimir no muestra el valor repetido en el set

set_types = {1, "hola", False, 12.12}
print(set_types)
# El set puede ser de varios tipos de datos
# El orden no importa dentro del Set

set_from_string = set("hoooola")
print(set_from_string)
# crear un set desde un String

set_from_tupla = set(("abc", "cbv", "as", "abc"))
print(set_from_tupla)
# crear un set desde una tupla

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers2 = set(numbers)
print(set_numbers2)
# set o conjunto de una lista, elementos unicos

unique_numbers = list(set_numbers2)
print(unique_numbers)
# Transformar un set de numeros unicos a una lista
