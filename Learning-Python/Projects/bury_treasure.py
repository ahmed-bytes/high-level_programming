#!/usr/bin/python3
row1 = ["🎌", "🏳️", "⭐️"]
row2 = ["🏁", "🪐", "🎄"]
row3 = ["☠️", "👽", "😸"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}\n")

value = int(input("Where do you want to put the treasure: "))
row = round(value / 10)
column = value % 10
map[row - 1][column - 1] = "X"

print(f"{row1}\n{row2}\n{row3}\n")
