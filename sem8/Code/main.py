
from functions import *
phonebook = read_file()
while True:

    print('''
Выберите команду:
1. Добавить контакт
2. Удалить контакт
3. Редактировать контакт
4. Найти контакт
5. Ввысти телефонную книгу
0. Выйти'''
    )

    user_kod = input("Введите номер команды: ")
    if user_kod == '1':
        add_user(phonebook)
    elif user_kod == '2':
        delete_user(phonebook)
    elif user_kod == '3':
        update_user(phonebook)
    elif user_kod == '4':
        search_user(phonebook)
    elif user_kod == '5':
        print_phonebook(phonebook)
    else:
        write_file(phonebook)
        print("До свидания!")
        break