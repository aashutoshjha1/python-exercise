#!/usr/bin/env python3

def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        yield a
    if n == 1:
        yield b
    else:
        while n > 1:
           r = a + b
           a = b
           b = r
           n  = n - 1
           yield r


def fibonacci_new(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

a = fibonacci(6)


for  i in (fibonacci_new(5)):
    print(i)




           