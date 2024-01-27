def fib(first):
    a = 0
    b = 1
    for i in range(first):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(10000):
    print(x)
