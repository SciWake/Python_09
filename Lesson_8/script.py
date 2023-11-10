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
    # from other_function import print_data_first
    print('Вывожу данные для Вас из 1-ого файла\n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_version_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i
        data_first = data_first_version_second
        print(''.join(data_first))
        # print(*data_first, sep='')

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
        number_journal = int(input('Введите номер записи: '))
        while number_journal != 1 and number_journal != 2:
            print('Ты дурак?! Даю тебе последний шанс')


        if number_journal == 1:
            print("Какую именно строку Вы хотите изменить?")
            number_str1 = input('Введите имя строки (Имя, Фамилия, Телефон или Адрес): ').lower().strip()
            if number_str1 == 'имя':
                number_str1 = 0
            if number_str1 == 'фамилия':
                number_str1 = 1
            if number_str1 == 'телефон':
                number_str1 = 2
            if number_str1 == 'адрес':
                number_str1 = 3
            else:
                print("Введите корректное название строки!")
            name_str1 = str(input("Введите новые данные: "))
             # ТУТ НАПИСАТЬ КОД
            with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
                data_first = file.readlines()
                data_first_version_second = []
                j = 0
                for i in range(len(data_first)):
                    if number_str1 == i:
                        data_first[i] = name_str1 + "\n"
                    if data_first[i] == '\n' or i == len(data_first) - 1:
                        data_first_version_second.append(''.join(data_first[j:i]))
                        j = i
                data_first = data_first_version_second
                with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                    file.write(''.join(data_first))
            print("Данные изменены. Спасибо, что вы с нами!")


        if number_journal == 2:
            print("Какую именно строку Вы хотите изменить?")
            number_str1 = input('Введите имя строки (Имя, Фамилия, Телефон или Адрес): ').lower().strip()
            if number_str1 == 'имя':
                number_str1 = 5
            if number_str1 == 'фамилия':
                number_str1 = 6
            if number_str1 == 'телефон':
                number_str1 = 7
            if number_str1 == 'адрес':
                number_str1 = 8
            else:
                print("Введите корректное название строки!")
            name_str1 = str(input("Введите новые данные: "))
             # ТУТ НАПИСАТЬ КОД
            with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
                data_first = file.readlines()
                data_first_version_second = []
                j = 0
                for i in range(len(data_first)):
                    if number_str1 == i:
                        data_first[i] = name_str1 + "\n"
                    if data_first[i] == '\n' or i == len(data_first) - 1:
                        data_first_version_second.append(''.join(data_first[j:i]))
                        j = i
                data_first = data_first_version_second
                with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                    file.write(''.join(data_first))
            print("Данные изменены. Спасибо, что вы с нами!")

    if number_file == 2:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        while number_journal != 1 and number_journal != 2:
            print('Ты дурак?! Даю тебе последний шанс')


        if number_journal == 1:
            print("Какую именно строку Вы хотите изменить?")
            number_str2 = input('Введите имя строки (Имя, Фамилия, Телефон или Адрес): ').lower().strip()
            if number_str2 == 'имя':
                number_str2 = 0
            if number_str2 == 'фамилия':
                number_str2 = 1
            if number_str2 == 'телефон':
                number_str2 = 2
            if number_str2 == 'адрес':
                number_str2 = 3
            else:
                print("Введите корректное название строки!")
            name_str2 = str(input("Введите новые данные: "))
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data_second = list(file.readlines())
            all = []
            for i in data_second:
                split_str = i.split(';')
                all.extend(split_str)
            data_second = all
            for i in range(len(data_second)):
                if number_str2 == i:
                    data_second[i] = name_str2
                elif i == 3 and number_str2 == i:
                    data_second[i] = name_str2 + '\n'
            split_res = []        
            for i in range(len(data_second)):
                if data_second[i] == '\n':
                    split_res.append(data_second[i])
                if i == 0 or data_second[i-1] == '\n':
                    split_res.append(data_second[i])
                else:
                    split_res[-1] = split_res[-1] + ';' + data_second[i]
            data_second = split_res
            for i in range(len(data_second)):
                if data_second[i] == '\n;\n':
                    data_second[i] = '\n'
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.write(*data_second)
            print("Данные изменены. Спасибо, что вы с нами!")


        if number_journal == 2:
            print("Какую именно строку Вы хотите изменить?")
            number_str2 = input('Введите имя строки (Имя, Фамилия, Телефон или Адрес): ').lower().strip()
            if number_str2 == 'имя':
                number_str2 = 5
            if number_str2 == 'фамилия':
                number_str2 = 6
            if number_str2 == 'телефон':
                number_str2 = 7
            if number_str2 == 'адрес':
                number_str2 = 8
            else:
                print("Введите корректное название строки!")
            name_str2 = str(input("Введите новые данные: "))
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data_second = list(file.readlines())
            all = []
            for i in data_second:
                split_str = i.split(';')
                all.extend(split_str)
            data_second = all
            for i in range(len(data_second)):
                if number_str2 == i:
                    data_second[i] = name_str2
                elif i == 8 and number_str2 == i:
                    data_second[i] = name_str2 + '\n'
            split_res = []        
            for i in range(len(data_second)):
                if data_second[i] == '\n':
                    split_res.append(data_second[i])
                if i == 0 or data_second[i-1] == '\n':
                    split_res.append(data_second[i])
                else:
                    split_res[-1] = split_res[-1] + ';' + data_second[i]
            data_second = split_res
            for i in range(len(data_second)):
                if data_second[i] == '\n;\n':
                    data_second[i] = '\n'
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.write(*data_second)
            print("Данные изменены. Спасибо, что вы с нами!")
        return data_first, data_second
            # print(*data_first, sep='')
#         # Можно добавить проверку, чтобы человек не выходил за пределы записей
#     else:
#         print("Какую именно запись по счету Вы хотите изменить?")
#         number_journal = int(input('Введите номер записи: '))
#         # ТУТ НАПИСАТЬ КОД
#         # Можно добавить проверку, чтобы человек не выходил за пределы записи


# def delete_data():
#     print('Из какого файла Вы хотите удалить данные?')
#     data_first, data_second = print_data()
#     number_file = int(input('Введите номер файла: '))

#     while number_file != 1 and number_file != 2:
#         print('Ты дурак?! Даю тебе последний шанс')
#         number_file = int(input('Введите номер файла: '))

#     if number_file == 1:  # Можно сделать нумерацию внутри файла
#         print("Какую именно запись по счету Вы хотите удалить?")
#         number_journal = int(input('Введите номер записи: '))
#         # Можно добавить проверку, чтобы человек не выходил за пределы записи
#         # ТУТ НАПИСАТЬ КОД
#     else:
#         print("Какую именно запись по счету Вы хотите удалить?")
#         number_journal = int(input('Введите номер записи: '))
#         # Можно добавить проверку, чтобы человек не выходил за пределы записи
#         # ТУТ НАПИСАТЬ КОД


# print("Какую именно запись по счету Вы хотите изменить?")
# number_journal = int(input('Введите номер записи: '))
# while number_journal != 1 and number_journal != 2:
#     print('Ты дурак?! Даю тебе последний шанс')
# if number_journal == 1:
#     print("Какую именно строку Вы хотите изменить?")
#     number_str2 = input('Введите имя строки (Имя, Фамилия, Телефон или Адрес): ').lower().strip()
#     if number_str2 == 'имя':
#         number_str2 = 0
#     if number_str2 == 'фамилия':
#         number_str2 = 1
#     if number_str2 == 'телефон':
#         number_str2 = 2
#     if number_str2 == 'адрес':
#         number_str2 = 3
#     else:
#         print("Введите корректное название строки!")
#     name_str2 = str(input("Введите новые данные: "))
#     with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
#             data_second = list(file.readlines())
#             all = []
#             for i in data_second:
#                 split_str = i.split(';')
#                 all.extend(split_str)
#             data_second = all
#             for i in range(len(data_second)):
#                 if number_str2 == i:
#                     data_second[i] = name_str2
#                 elif i == 3 and number_str2 == i:
#                     data_second[i] = name_str2 + '\n'
#             split_res = []        
#             for i in range(len(data_second)):
#                 if data_second[i] == '\n':
#                     split_res.append(data_second[i])
#                 if i == 0 or data_second[i-1] == '\n':
#                     split_res.append(data_second[i])
#                 else:
#                     split_res[-1] = split_res[-1] + ';' + data_second[i]
#             data_second = split_res
#             for i in range(len(data_second)):
#                 if data_second[i] == '\n;\n':
#                     data_second[i] = '\n'
#             print(data_second)