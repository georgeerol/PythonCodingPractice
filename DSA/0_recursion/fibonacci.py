def fib(n):
    assert 0 <= n == int(n), 'Fibonacci number cannot be negative number or non integer.'
    if n in [0, 1]:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fib(7))
