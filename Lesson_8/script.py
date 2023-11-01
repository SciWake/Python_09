from data_create import name_data, surname_data, phone_data, address_data


def get_data():  # Вводим отдельную функцию, которая возвращает вложенные списки с записями от каждого файла
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = []
        subdata = []
        for i in file.readlines():
            if i == '\n':  # Если дошли до пустой строки, вносим в список одного человека
                data_first.append(subdata)
                subdata = []
            else:
                subdata.append(i.replace('\n', ''))  # Удаляем служебные символы
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = []
        for i in file.readlines():
            if i != '\n':
                data_second.append(i.replace('\n', '').split(';'))
        return data_first, data_second


def rewrite_data(file, data):  # Функция, которая будет перезаписывать файлы
    if file == 'data_first_variant.csv':
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            for i in data:
                for j in i:
                    file.write(j + '\n')
                file.write('\n')
    else:
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            for i in data:
                file.write(';'.join(i) + '\n\n')


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


def print_data():  # Функция, выводящая список записей
    data_first, data_second = get_data()
    print('Вывожу данные для Вас из 1-ого файла\n')
    for i in range(len(data_first)):
        print(f'----- Запись номер {i + 1} -----')
        print('\n'.join(data_first[i]), '\n')
    print('Вывожу данные для Вас из 2-ого файла\n')
    for i in range(len(data_second)):
        print(f'----- Запись номер {i + 1} -----')
        print('\n'.join(data_second[i]), '\n')

    return data_first, data_second  # Возвращаем значения, если необходим вывод + дальнейшая работа со значениями


def change_data():
    print('Из какого файла Вы хотите изменить данные?\n')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))

        while number_journal < 1 or number_journal > len(data_first):  # Проверка на выход за пределы записей
            number_journal = int(input('Нет такой записи. Введите номер записи повторно: '))

        print('Какие данные вы бы хотели изменить?\n')
        for i in range(len(data_first[number_journal - 1])):
            print(f'{i + 1}. {data_first[number_journal - 1][i]}')

        print('0. Отмена\n')

        choice = int(input('Введите номер пункта: '))

        while choice < 0 or choice > len(data_first[number_journal - 1]):  # Проверка на выход за пределы записей
            choice = int(input('Нет такого пункта. Повторите ввод: '))

        if choice == 0:  # Выход из функции при выборе пункта "Отмена"
            print('Отмена')
            return

        else:
            change = input('Введите новое значение: ')
            data_first[number_journal - 1][choice - 1] = change
            rewrite_data('data_first_variant.csv', data_first)

    if number_file == 2:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))

        while number_journal < 1 or number_journal > len(data_second):  # Проверка на выход за пределы записей
            number_journal = int(input('Нет такой записи. Введите номер записи повторно: '))

        print('Какие данные вы бы хотели изменить?\n')
        for i in range(len(data_second[number_journal - 1])):
            print(f'{i + 1}. {data_second[number_journal - 1][i]}')

        print('0. Отмена\n')

        choice = int(input('Введите номер пункта: '))

        while choice < 0 or choice > len(data_second[number_journal - 1]):  # Проверка на выход за пределы записей
            choice = int(input('Нет такого пункта. Повторите ввод: '))

        if choice == 0:  # Выход из функции при выборе пункта "Отмена"
            print('Отмена')
            return

        else:
            change = input('Введите новое значение: ')
            data_second[number_journal - 1][choice - 1] = change
            rewrite_data('data_second_variant.csv', data_second)


def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))

        while number_journal < 1 or number_journal > len(data_first):  # Проверка на выход за пределы записей
            number_journal = int(input('Нет такой записи. Введите номер записи повторно: '))

        del data_first[number_journal - 1]

        rewrite_data('data_first_variant.csv', data_first)

        print('Запись успешно удалена!')

    if number_file == 2:

        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))

        while number_journal < 1 or number_journal > len(data_second):  # Проверка на выход за пределы записей
            number_journal = int(input('Нет такой записи. Введите номер записи повторно: '))

        del data_second[number_journal - 1]

        rewrite_data('data_second_variant.csv', data_second)
