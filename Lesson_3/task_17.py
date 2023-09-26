"""Дан список чисел. Определите, сколько в нем
встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]

Output: 6
"""

# numbers = []
# for _ in range(int(input("Количество элементов: "))):
#     numbers.append(int(input("Введите элемент: ")))

numbers = [2, 3, 2, 3, 1, 1, 5, 20, 20, 30]

# Вариант 1
result = []
for num in numbers:
    if num not in result:
        result.append(num)
print(len(result))


# Вариант 2
result = []
for num in numbers:
    if result.count(num) == 0:
        result.append(num)
print(len(result))


# Вариант 3 - Изменяем исходный список
for num in numbers[:]: 
    while numbers.count(num) > 1:
        numbers.remove(num)
print(len(numbers))

