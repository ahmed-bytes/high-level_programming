def fib1(n):
    """Print finobacci numbers to n."""
    a, b = 0, 1
    while a < n:
        print(f"{a}", end=" ")
        a, b = b, a + b
        print()
