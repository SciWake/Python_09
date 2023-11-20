
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def fact(n):
    return 1 if n == 1 else n * fact(n - 1)


print(fact(1000))
# fact(4) -> 24
#     4 * fact(3) -> 4 * 6
#         3 * fact(2) -> 3 * 2
#             2 * fact(1) -> 2 * 1


# fact = 1
# for i in range(1, 5 + 1):
#     fact *= i
# print(fact)