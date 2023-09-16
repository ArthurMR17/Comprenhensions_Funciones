# CRUD => Create, Read, Update, Delete

## Create ##
set_countries = {"col", "mex", "bol"}

size = len(set_countries)
print(size)
# imprimir tamano del set

## Read ##
if "col" in set_countries:
    print(True)

print("col" in set_countries)
# lo mismo que el if linea 7

## Add ##
set_countries.add("pe")
print(set_countries)
# metodo add para agregar datos al set


## Update ##
set_countries.update({"ar", "ecua", "pe"})
print(set_countries)


## Delete ##
set_countries.remove("col")
print(set_countries)
set_countries.discard("colo")
# No crashea si el elemento no existe

set_countries.clear()
print(set_countries)
# borra todo el contenido del Set
print(len(set_countries))
