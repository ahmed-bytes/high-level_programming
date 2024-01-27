def sort_zip(list_num):
    return sorted(list_num)


my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(sort_zip(my_numbers), my_strings)))
