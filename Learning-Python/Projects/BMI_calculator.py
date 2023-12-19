def bmi(w, h):
    """
    Calculate the bmi of a person.

    w: weight of person
    h: height of person.
    """
    result = w / (h * h)
    return round(result)


weight = float(input("Enter your height in kg: "))
height = float(input("Enter your weight in m: "))

BMI = bmi(weight, height)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are Underweight")
elif BMI > 18.5 and BMI < 25.0:
    print(f"Your BMI is {BMI}, you are Normal weight")
elif BMI > 25.0 and BMI < 30.0:
    print(f"Your BMI is {BMI}, you are Overweight")
elif BMI > 30.0 and BMI < 35.0:
    print(f"Your BMI is {BMI}, you are Obese")
else:
    print(f"Your BMI is {BMI}, you are Clinically Obese")
