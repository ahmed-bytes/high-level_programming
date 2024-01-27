some_list = ["a", "b", "c", "b", "m", "n", "n"]

duplicates = list(set(value for value in some_list if some_list.count(value) > 1))

print(duplicates)
