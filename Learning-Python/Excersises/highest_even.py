def highest_even(li):
    """Find the highest even numbers."""
    result = []
    for i in li:
        if i % 2 == 0:
            result.append(i)
    return max(result)


print(highest_even([10, 2, 3, 4, 8, 11]))
