# Prompt the user for two numbers
first_Number = input("Enter Two Numbers: ")

# separate the numbers
second_Number = first_Number[1]
first_Number = first_Number[0]

# convert to int and add the numbers and print the values
result = int(first_Number) + int(second_Number)
print(f'{first_Number} + {second_Number} = {result}')
