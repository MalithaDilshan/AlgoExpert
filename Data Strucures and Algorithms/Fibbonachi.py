def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, (a + b)


for a in fib():
    # print(a)
    if a > 100:
        break

from functools import lru_cache


@lru_cache(maxsize=1000)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(0, 100):
    print(fib(i))
