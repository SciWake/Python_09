import os
import csv

def add_user(dictionary: dict):
    name = input('Введите имя: ')
    phone = input('Введите номер: ')
    if name in dictionary:
        print('Абонент уже добавлен: Имя: {} - Номер: {}'.format(name, dictionary[name]))
    else:
        dictionary[name] = phone
        print('Новый абонент "{}" успешно добавлен'.format(name))
    return dictionary


def delete_user(dictionary: dict):
    name = input('Введите имя: ')
    if name in dictionary:
        dictionary.pop(name)
        print('Абонент "{}" удалён'.format(name))
    else:
        print('Данного абонента нет в вашей книге')
    return dictionary


def update_user(dictionary: dict):
    name = input('Введите имя: ')
    phone = input('Введите новый номер номер: ')
    if name in dictionary:
        dictionary[name] = phone
        print('Абонент "{}" удалён'.format(name))
    else:
        print('Данного абонента нет в вашей книге')
    return dictionary


def search_user(dictionary: dict):
    search_value = input('Введите имя или номер абонента: ')
    name_in_dict = False
    for key, value in dictionary.items():
        if key.lower() == search_value.lower() or value == search_value:  
            print('Имя: "{}" - Телефон: "{}"'. format(key, value))
            name_in_dict = True
    if name_in_dict == False:
        print('Данного абонента не существует')


def print_phonebook(dictionary: dict):
    for key, value in dictionary.items():
        print('Все контакты: ' + '\n' + 'Имя: "{}" - Номер: "{}"'. format(key, value))


def read_file():
    check_file = os.path.exists('./phonebook.csv')
    if check_file is True:
        with open('./phonebook.csv') as file:
            phonebook_from_file = csv.reader(file, delimiter = ",")
            phonebook = {}
            for abonent in phonebook_from_file:
                if len(abonent) > 0:
                    phonebook[abonent[0]] = abonent[1]              
        return phonebook
    else:
        return dict()


def write_file(dictionary: dict):
    with open('./phonebook.csv', 'w') as file:
        writing_file = csv.writer(file)
        for name, number in dictionary.items():
            writing_file.writerow([name, number])
        