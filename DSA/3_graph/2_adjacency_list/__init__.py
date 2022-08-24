def rec(n):
    if n <= 1:
        return n
    else:
        return n * rec(n - 1)


if __name__ == "__main__":
    print(rec(-4))
