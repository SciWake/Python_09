"""Хакер Василий получил доступ к классному журналу 
и хочет заменить все свои минимальные оценки на максимальные."""


# Вариант 1 - max and min
list_of_ratings = [2, 2, 4, 3, 2, 3, 3, 5, 5, 5, 5, 5]
max_number = max(list_of_ratings)
min_number = min(list_of_ratings)
print(f'Минимум - {min_number}, Максимум - {max_number}')

for i in range(len(list_of_ratings)):
    if list_of_ratings[i] == min_number:
        list_of_ratings[i] = max_number
        
print(list_of_ratings)
