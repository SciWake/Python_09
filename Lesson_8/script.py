from data_create import name_data, surname_data, phone_data, address_data
import os

def get_path(mpath: str) -> os.path:
    return os.path.join(os.getcwd(), mpath)


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = int(input(f"В каком формате Вы хотите записать данные?\n\n"
                    f"1 Вариант:\n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 Вариант:\n\n"
                    f"{surname};{name};{phone};{address}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        print('Попробуйте ещё раз выбрать правильную команду')
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    print('Вывожу данные для Вас из 1-ого файла\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = list(file.readlines())
        # data_first_version_second = []
        # j = 0
        # for i in range(len(data_first)):
        #     if data_first[i] == '\n' or i == len(data_first) - 1:
        #         data_first_version_second.append(''.join(data_first[j:i + 1]))
        #         j = i
        # data_first = data_first_version_second
        # print(''.join(data_first))
        print(*data_first, sep='')

    print('Вывожу данные для Вас из 2-ого файла\n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second


def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: ')) - 1 
        # ТУТ НАПИСАТЬ КОД
        # Можно добавить проверку, чтобы человек не выходил за пределы записей
        result_first = [''.join(data_first[i:i+5]) for i in range(0, len(data_first), 5)] 
        if 0 <= number_journal < len(result_first): # Проверка предела записей
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            address = address_data()
            result_first[number_journal] = f'{name}\n{surname}\n{phone}\n{address}\n\n'
            data_first = ''.join(result_first)
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                file.write(data_first)
        else:
            print ('Вы вышли за границы списка, начните заново')
    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: ')) - 1
        # ТУТ НАПИСАТЬ КОД
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        result_second = [''.join(data_second[i:i+2]) for i in range(0, len(data_second), 2)] 
        if 0 <= number_journal < len(result_second): # Проверка предела записей
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            address = address_data()
            result_second[number_journal] = f'{name};{surname};{phone};{address}\n\n'
            data_second = ''.join(result_second)
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.write(data_second)
        else:
            print ('Вы вышли за границы списка, начните заново')

def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: ')) - 1
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        # ТУТ НАПИСАТЬ КОД
        result_first = [''.join(data_first[i:i+5]) for i in range(0, len(data_first), 5)] 
        if 0 <= number_journal < len(result_first): # Проверка предела записей
            result_first.pop(number_journal)
            data_first = ''.join(result_first)
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                file.write(data_first)
        else:
            print ('Вы вышли за границы списка, начните заново')
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: ')) - 1
        # Можно добавить проверку, чтобы человек не выходил за пределы записи
        # ТУТ НАПИСАТЬ КОД
        result_second = [''.join(data_second[i:i+2]) for i in range(0, len(data_second), 2)] 
        if 0 <= number_journal < len(result_second): # Проверка предела записей
            result_second.pop(number_journal)
            data_second = ''.join(result_second)
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.write(data_second)
        else:
            print ('Вы вышли за границы списка, начните заново')       

