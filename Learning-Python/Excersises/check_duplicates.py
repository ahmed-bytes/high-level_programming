"""check for duplictae in a liss."""
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

result_list = []

for i in some_list:
    if some_list.count(i) > 1:
        if i not in result_list:
            result_list.append(i)
print(result_list)
