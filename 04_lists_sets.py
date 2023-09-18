numbers = []
for element in range(1, 11):
    numbers.append(element * 2)

print(numbers)

# list Comprehensions
numbers_v2 = [element * 2 for element in range(1, 11)]
#            [elemt for element in iterable ]
#            [element for eleent in iterable if condition]
#            [i*2 for i in range(1, 101) if i % 2 ==0]
print(numbers_v2)
print([i * 2 for i in range(1, 101) if i % 2 == 0])
