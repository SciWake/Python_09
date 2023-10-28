from data_create import *


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
        data_second = file.readlines()
        print(*data_second)
    return data_first, data_second
def edit_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла

        print("Какую именно запись по счету Вы хотите изменить?")
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
            print(*data_first)
        number_journal = int(input('Введите номер записи: '))
        if number_journal == 1:
            data_first_version_second = ''.join(data_first[5:])
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                file.write(f'{name_data()}\n{surname_data()}\n{phone_data()}\n{address_data()}\n\n{data_first_version_second}')
        if number_journal == 2:
            data_first_version_second = ''.join(data_first[:5])
            data2 = ''.join(data_first[9:])
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                file.write(f'{data_first_version_second}{name_data()}\n{surname_data()}\n{phone_data()}\n{address_data()}\n{data2}\n\n')
        if number_journal == 3:
            data_first_version_second = ''.join(data_first[:10])
            data2 = ''.join(data_first[14:])
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                file.write(f'{data_first_version_second}{name_data()}\n{surname_data()}\n{phone_data()}\n{address_data()}\n{data2}\n\n')
        if number_journal == 4:
            data_first_version_second = ''.join(data_first[:15])
            data2 = ''.join(data_first[20:])
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                file.write(f'{data_first_version_second}{name_data()}\n{surname_data()}\n{phone_data()}\n{address_data()}\n{data2}\n\n')
    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data_second = file.readlines()
            print(*data_second)
        number_journal = int(input('Введите номер записи: '))

        if number_journal == 1:
            data_second_version_second = ''.join(data_second[2:])

            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.write(f'{name_data()};{surname_data()};{phone_data()};{address_data()}\n\n {data_second_version_second}')

        if number_journal == 2:
            data_second_version_second = ''.join(data_second[:2])
            data2 = ''.join(data_second[3:])
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.write(f'{data_second_version_second}{name_data()};{surname_data()};{phone_data()};{address_data()}\n{data2}\n\n')
        if number_journal == 3:
            data_second_version_second = ''.join(data_second[:4])
            data2 = ''.join(data_second[5:])
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.write(f'{data_second_version_second}{name_data()};{surname_data()};{phone_data()};{address_data()}\n{data2}\n\n')
        if number_journal == 4:
            data_second_version_second = ''.join(data_second[:6])
            data2 = ''.join(data_second[7:])
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.write(f'{data_second_version_second}{name_data()};{surname_data()};{phone_data()};{address_data()}\n{data2}\n\n')
def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите удалить?")
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
            print(*data_first)
        number_journal = int(input('Введите номер записи: '))
        if number_journal == 1 :
            del_list = ''.join(data_first[5:])
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                file.write(f'{del_list}')
        if number_journal == 2:
            del_list = ''.join(data_first[:5])
            last_list = ''.join(data_first[10:])
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                file.write(f'{del_list}{last_list}')
        if number_journal == 3:
            del_list = ''.join(data_first[:10])
            last_list = ''.join(data_first[15:])
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                file.write(f'{del_list}{last_list}')
        if number_journal == 4:
            del_list = ''.join(data_first[:15])
            last_list = ''.join(data_first[20:])
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                file.write(f'{del_list}{last_list}')

    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data_second = file.readlines()
            print(*data_second)
        number_journal = int(input('Введите номер записи: '))
        if number_journal == 1:
            del_list = ''.join(data_second[2:])
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.write(f'{del_list}')
        if number_journal == 2:
            del_list = ''.join(data_second[:2])
            last_list = ''.join(data_second[4:])
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.write(f'{del_list}{last_list}')
        if number_journal == 3:
            del_list = ''.join(data_second[:4])
            last_list = ''.join(data_second[6:])
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.write(f'{del_list}{last_list}')
        if number_journal == 4:
            del_list = ''.join(data_second[:6])
            last_list = ''.join(data_second[8:])
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.write(f'{del_list}{last_list}')