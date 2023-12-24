"""Checks and outputs prime number."""


def prime_checker(number):
    """Check if number is a prime number."""
    counter = 0
    for i in range(2, number):
        if number % i == 0:
            counter += 1
    if counter > 0:
        return False
    else:
        return True


n = int(input("Enter Number: "))
result = prime_checker(number=n)

if result == True:
    print(f"{n} is a prime number")
else:
    print(f"{n} it's not a prime number")
