# https://www.youtube.com/watch?v=-xIZ8uEFDko&ab_channel=CrackingFAANG
def sum_zero(n):
    res = []

    if n % 2:
        res.append(0)
    for i in range(1, n // 2 + 1):  # 1 to get last element
        res.append(i)
        res.append(-i)
    return res


if __name__ == '__main__':
    n = 5
    print(sum_zero(n))
