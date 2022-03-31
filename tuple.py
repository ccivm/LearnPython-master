from numpy.random import rand
values = rand(1000000,4)
print(len(values))
tup = tuple(tuple(row) for row in values)