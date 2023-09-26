"""Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.

Input: [1, 2, 3, 4, 5] k = 3
Output: [3, 4, 5, 1, 2]
"""

numbers = [1, ['sdfs', 'dfs'], 3, 4, 5]

data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},] 

k = 3
k = k % len(numbers)  # Убираем лишнии итерации цикла


# Вариант [1] - Modified
list_result = []
len_list = len(numbers)
for i in range(len_list - k, len_list):
    list_result.append(numbers[i])
for i in range(len_list - k):
    list_result.append(numbers[i])
print(list_result)


# Вариант 2 - Убираем два цикла for
list_result = []
for i in range(len(numbers)):
    list_result.append(numbers[-k + i])
print(list_result)


# Вариант 3 - рабобаем с исходным массивом
for _ in range(k):
    numbers.insert(0, numbers.pop())
print(numbers)


# Вариант 4 - так как исходный список поменял, создадим его ещё раз
numbers = [1, 2, 3, 4, 5]
print(numbers[-k:] + numbers[:-k])


# Вариант 5 - обмен значениями [Не успел]
