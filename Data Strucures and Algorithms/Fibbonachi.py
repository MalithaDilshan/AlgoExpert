def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, (a + b)


for a in fib():
    print(a)
    if a > 100:
        break
