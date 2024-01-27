from functools import reduce


def total(acc, items):
    return acc + items


my_numbers = [5, 4, 3, 2, 1]
scores = [73, 20, 65, 19, 76, 100, 88]

print(reduce(total, (my_numbers + scores), 0))
