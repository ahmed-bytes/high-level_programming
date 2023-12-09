def pattern(size):
    for rows in range(1, size + 1):
        print("* " * rows)


def upside_pattern(size):
    for rows in range(size):
        print("* " * (size - rows))


size = int(input("How Many roles?: "))
pattern(size)
upside_pattern(size)
