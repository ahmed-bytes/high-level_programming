#!/usr/bin/python3
def leap_year(num):
    """Check if a year is a leap year."""
    if num % 4 == 0:
        if num % 100 == 0:
            if num % 400 == 0:
                print(f"{num} is a leap year")
            else:
                print(f"{num} is not a leap year")
        else:
            print(f"{num} is a leap year")
    else:
        print(f"{num} is not a leap year")


year = int(input("Which year do you want to check: "))
leap_year(year)

from fibo import fib1 as f

if __name__ == "__main__":
    f(year)
