"""Пользователь вводит текст(строка). 
Словом считается последовательность непробельных символов идущих подряд, 
слова разделены одним или большим числом пробелов или символами конца строки. 
Определите, сколько различных слов содержится в этом тексте."""

# Вариант 1 
text = """She sells sea shells on the sea 
shore The shells that she sells are sea 
shells I'm sure So     if she sells sea shells 
on the sea shore I'm sure that the shells are sea shore shells"""
text = text.split()
unique_words = set()
for word in text:
    unique_words.add(word.lower())
print(len(unique_words))


# Вариант 2
text = """She sells sea shells on the sea 
shore The shells that she sells are sea 
shells I'm sure So if she sells sea shells 
on the sea shore I'm sure that the shells are sea shore shells"""

print(len(set(text.lower())))


1, 7, 8, 19, 3, 100, 25, 0, 780, 




a = int(input("Введи любое, кроме 0: "))
max_a = 0
while a != 0:
    a = int(input())
    if a > max_a:
        max_a = a
print(max_a)

В - 2
П - 4