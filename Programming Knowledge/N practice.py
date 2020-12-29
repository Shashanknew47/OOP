from datetime import datetime


def calf(n):
    j = 1
    k = 1
    for _ in range(3, n+1):
        j, k = k, j+k
    return k


print(calf(7))


def recalf(n):
    if n <= 2:
        return 1
    else:
        return recalf(n-1) + recalf(n-2)


print(recalf(7))


def calf(n):
    from functools import reduce
    j = 1
    k = 1
    m = reduce(lambda i, j: j, i+j, range(1, n))
