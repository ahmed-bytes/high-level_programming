def say_hello():
    print("hello")


def add_num(a, b):
    return int(a) + int(b)


def divide_num(a, b):
    return int(a) / int(b)


say_hello()
add_num(2, 3)
a = input("number: ")
b = input("number: ")

print(divide_num(a, b))
print(add_num(a, b))
