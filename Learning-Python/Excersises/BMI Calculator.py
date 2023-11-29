# Prompt the user fo their weight in kg and height in m
weight = input("Enter your weight(kg): ")
height = input("Enter your height(m): ")

# calculate the BMI
bmi = int(weight) / (float(height) ** 2)

# print the output
print(f"Your BMI is {round(bmi, 3)}")
