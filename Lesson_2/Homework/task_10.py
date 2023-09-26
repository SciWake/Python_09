"""На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, 
которые нужно перевернуть, чтобы все монетки были повернуты 
вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
"""

# Вариант 1 
n = int(input("Количество моенток: "))
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input("Сторока монетки: "))
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)


# Вариант 2 
n = int(input("Количество моенток: "))
count_one = 0
for i in range(n):
    x = int(input("Сторока монетки: "))
    if x == 1:
        count_one += 1
count_zero = n - count_one
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)


# Вариант 3
n = int(input("Количество моенток: "))
count_one = sum(int(input("Сторока монетки: ")) for _ in range(n))
count_zero = n - count_one
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)
