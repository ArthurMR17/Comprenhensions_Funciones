# [key: vale for vas in iterable]

import random


dict = {}
for i in range(1, 6):
    dict[i] = i * 2
print(dict)

# diccionario comprenhension
dict_v2 = {i: i * 2 for i in range(1, 6)}
print(dict_v2)

countries = ["col", "mex", "bol", "pe"]
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
    # print(population[country])
print(population)


population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

names = ["nico", "zule", "santi"]
ages = [12, 56, 98]

list_dic = zip(names, ages)
list_dic = list(list_dic)
print(list_dic)

new_dic = {name: age for (name, age) in zip(names, ages)}
print(new_dic)
