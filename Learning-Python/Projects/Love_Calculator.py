print("Welcome to the Love Calculator")
name1 = input("What is your name? \n").upper()
name2 = input("What is your name? \n").upper()

compare_string = ["T", "R", "U", "E", "L", "O", "V", "E"]
combined_name = name1 + name2
result = 0
length1 = len(combined_name)
length2 = len(compare_string)

for i in range(length1):
    for j in range(length2):
        result += combined_name[i].count(compare_string[j])

if result >= 50:
    print(f"{result}% is a match")
else:
    print(f"{result}% is not a match")

print(name1)
