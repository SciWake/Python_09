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
        data_first = file.readlines()
        data_first_version_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_version_second.append(''.join(data_first[j:i + 1]))
                j = i + 1
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

    if number_file == 1:
        # ТУТ НАПИСАТЬ КОД
        # Можно добавить проверку, чтобы человек не выходил за пределы записей
        print("Какую именно запись по счету Вы хотите изменить?")
        for i in range(len(data_first)):
            print(i + 1, data_first[i].replace("\n\n", "").replace("\n", ","))
        number_journal = int(input('Введите номер записи: ')) - 1
        if number_journal in range(len(data_first)): 
            # пришлось городить такую дикую конструкцию потому как input_data не по фэншую написана
            print("Текущее значение: ", "\n\n", data_first[number_journal].replace("\n\n", "").replace("\n", ","))
            print("Введите новые значения (пустая строка сохранит старое): ")
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            address = address_data()
            arr = data_first[number_journal].split('\n')
            if name == '': name = arr[0]
            if surname == '': surname = arr[1]
            if phone == '': phone = arr[2]
            if address == '': address = arr[3]
            str = name + '\n' + surname + '\n' + phone + '\n' + address + '\n\n'
            data_first[number_journal] = str
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                file.writelines(data_first)
            print("Данные изменены")
        else: print("Такой записи в файле нет")
    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        for i in range(0, len(data_second), 2):
            print((int) ((i / 2) + 1), data_second[i].replace("\n", ""))
        number_journal = (int(input('Введите номер записи: ')) - 1) * 2
        if number_journal in range(len(data_second)): 
            # пришлось городить такую дикую конструкцию потому как input_data не по фэншую написана
            print("Текущее значение: ", "\n\n", data_second[number_journal].replace("\n", ""))
            print("Введите новые значения (пустая строка сохранит старое): ")
            name = name_data()
            surname = surname_data()
            phone = phone_data()
            address = address_data()
            arr = data_second[number_journal].replace("\n", "").split(';')
            if name == '': name = arr[0]
            if surname == '': surname = arr[1]
            if phone == '': phone = arr[2]
            if address == '': address = arr[3]
            str = name + ';' + surname + ';' + phone + ';' + address + '\n'
            data_second[number_journal] = str
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.writelines(data_second)
            print("Данные изменены")
        else: print("Такой записи в файле нет")

def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:
        # ТУТ НАПИСАТЬ КОД
        # Можно добавить проверку, чтобы человек не выходил за пределы записей
        print("Какую именно запись по счету Вы хотите удалить?")
        for i in range(len(data_first)):
            print(i + 1, data_first[i].replace("\n\n", "").replace("\n", ","))
        number_journal = int(input('Введите номер записи: ')) - 1
        if number_journal in range(len(data_first)):
            data_first.pop(number_journal)
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                file.writelines(data_first)
            print("Данные изменены")
        else: print("Такой записи в файле нет")
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        for i in range(0, len(data_second), 2):
            print((int) ((i / 2) + 1), data_second[i].replace("\n", ""))
        number_journal = (int(input('Введите номер записи: ')) - 1) * 2
        if number_journal in range(len(data_second)): 
            data_second.pop(number_journal + 1)
            data_second.pop(number_journal )
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                file.writelines(data_second)
            print("Данные изменены")
        else: print("Такой записи в файле нет")