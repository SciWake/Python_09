
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def fact(n):
    return 1 if n == 1 else n * fact(n - 1)


print(fact(15))
