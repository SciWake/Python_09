"""25. Напишите программу, которая принимает на вход строку, 
и отслеживает, сколько раз каждый символ уже встречался. 
Количество повторов добавляется к символам с помощью постфикса формата _n."""


# stroka = input("Введиет строку Данных: ")
stroka = 'a a a b c a a d c d d'
stroka = stroka.split()
result = {}

for i in stroka:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
    else:
        print(i, end=' ')
    result[i] = result.get(i, 0) + 1
print()
print(result)


"""
Traceback (most recent call last):
  File "<string>", line 1, in <module>
KeyError: 'b'
"""