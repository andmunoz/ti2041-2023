def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def fib2(n):
    fibonacci = fib(n)
    for a in fibonacci:
        print(a, ' ')
    print()
