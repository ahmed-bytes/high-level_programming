print("Welcome to the Love Calculator")
name1 = input("What is your name? \n").upper()
name2 = input("What is your name? \n").upper()
fullNames = name1 + name2
T = fullNames.count("T")
R = fullNames.count("R")
U = fullNames.count("U")
E = fullNames.count("E")
true = T + R + U + E
L = fullNames.count("L")
O = fullNames.count("O")
V = fullNames.count("V")
E = fullNames.count("E")
love = L + O + V + E
result = int(str(true) + str(love))
print(result)
if result >= 50:
    print(f"{result}% is a match")
else:
    print(f"{result}% is not a match")
