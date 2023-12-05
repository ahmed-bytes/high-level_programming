"""Ascii GUI."""
picture = [
    [0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1],
]

for i in picture:
    for j in i:
        if j == 0:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
