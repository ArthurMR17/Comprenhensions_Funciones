set_a = {"col", "mex", "bol"}
set_b = {"pe", "bol"}

# metodo Union para unir conjuntos
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)  # operador | para sumar conjuntos o unirlos

# conocer elementos en comun
set_d = set_a.intersection(set_b)
print(set_d)
print(set_a & set_b)  # operador & para intersection

# eliminar el elemento comun
# del conjunto B en el conjunto A
set_c = set_a.difference(set_b)
print(set_c)
print(set_b.difference(set_a))
print(set_a - set_b)  # operador para diferencia

# unir los conjuntos sin el elemento en comun
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)
