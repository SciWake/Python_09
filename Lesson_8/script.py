import os

from data_create import set_data

FIRST_FILENAME = 'data_first_variant.csv'
SECOND_FILENAME = 'data_second_variant.csv'


def get_path(mpath: str) -> os.path:
    return os.path.join(os.getcwd(), mpath)


def input_data():
    name, surname, phone, address = set_data()

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
        var = int(input('Введите номер варианта: '))

    if var == 1:
        with open(FIRST_FILENAME, 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open(SECOND_FILENAME, 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n')


def read_data(number_file):
    exist_first = os.path.exists(FIRST_FILENAME)
    exist_second = os.path.exists(SECOND_FILENAME)
    if not exist_first and not exist_second:
        print('Файлы не существуют')
        return

    if number_file == 1 and exist_first:
        with open(FIRST_FILENAME, 'r', encoding='utf-8') as file:
            data_first = file.readlines()
            data_first_version_second = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_version_second.append(''.join(data_first[j:i + 1]))
                    j = i + 1
            data_first = data_first_version_second
            return data_first

    if number_file == 2 and exist_second:
        with open(SECOND_FILENAME, 'r', encoding='utf-8') as file:
            data_second = list(file.readlines())
            return data_second


def print_data(number_file):
    if number_file == 1 or number_file == 0:
        print('---------------------------------------------')

        data_first = read_data(1)
        if is_list_blank(data_first):
            print('Данные в 1-ом файле отсутствуют\n')
            return

        print('Вывожу данные для Вас из 1-ого файла\n')
        for i in range(len(data_first)):
            index = str(i + 1) + '\n'
            data_first[i] = index + data_first[i]
        print(''.join(data_first))

    if number_file == 2 or number_file == 0:
        print('---------------------------------------------')

        data_second = read_data(2)
        if is_list_blank(data_second):
            print('Данные в 2-ом файле отсутствуют\n')
            return

        print('Вывожу данные для Вас из 2-ого файла\n')
        for i in range(len(data_second)):
            index = str(i + 1) + ' '
            data_second[i] = index + data_second[i].replace(';', ' ')
        print(*data_second, sep='')


def get_number_file():
    number_file = int(input('Введите номер файла: '))
    while number_file != 1 and number_file != 2:
        print('Неправильный выбор, повторите')
        number_file = int(input('Введите номер файла: '))
    return number_file


def is_list_blank(list_data):
    if not list_data or len(list_data) == 0:
        return True
    else:
        return False


def get_number_journal(data, number_file, action):
    print_data(number_file)
    print('Какую именно запись по счету Вы хотите ' + action + '?')
    number_journal = int(input('Введите номер записи: '))
    while 0 <= number_journal > len(data):
        number_journal = int(input('Введите номер записи еще раз: '))
    return number_journal


def write_files(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(data)


def put_data():
    print('В каком файле Вы хотите изменить данные?')
    number_file = get_number_file()

    data = read_data(number_file)
    if is_list_blank(data):
        print('Данные отсутствуют')
        return

    number_journal = get_number_journal(data, number_file, 'изменить')

    print('Заполните новые данные')
    name, surname, phone, address = set_data()

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        data[number_journal - 1] = f'{name}\n{surname}\n{phone}\n{address}\n\n'
        write_files(FIRST_FILENAME, data)
    else:
        data[number_journal - 1] = f'{name};{surname};{phone};{address}\n'
        write_files(SECOND_FILENAME, data)

    print('Запись ' + str(number_journal) + ' изменена успешно')


def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    number_file = get_number_file()

    data = read_data(number_file)
    if is_list_blank(data):
        print('Данные отсутствуют')
        return

    number_journal = get_number_journal(data, number_file, 'удалить')

    del data[number_journal - 1]
    if number_file == 1:
        write_files(FIRST_FILENAME, data)
    else:
        write_files(SECOND_FILENAME, data)

    print('Запись ' + str(number_journal) + ' удалена успешно')


def copy_paste_data():
    print('Из какого файла Вы собираетесь копировать запись?')
    num_copy_file = get_number_file()

    if num_copy_file == 1:
        number_paste_file = 2
    else:
        number_paste_file = 1

    copy_data = read_data(num_copy_file)
    if is_list_blank(copy_data):
        print('Данные отсутствуют')
        return

    number_journal = get_number_journal(copy_data, num_copy_file, 'скопировать')

    element = copy_data[number_journal - 1]
    element = element[:-1]

    if number_paste_file == 1:
        element = element.replace(';', '\n') + '\n'
        with open(FIRST_FILENAME, 'a', encoding='utf-8') as file:
            file.write(element)
    else:
        element = element.replace('\n', ';') + '\n'
        with open(SECOND_FILENAME, 'a', encoding='utf-8') as file:
            file.write(element)

    print('Запись ' + str(number_journal) + ' скопирована успешно')
