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
            file.write(f'{name};{surname};{phone};{address}\n') # \n\n


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
        print("Имя | Фамилия | Телефон | Адрес")
        with open('data_first_variant.csv', "r", encoding="utf-8") as data:
            tel_book = data.read()
        tel_book_lines = tel_book.split("\n")
        len_tel_book_lines = len(tel_book_lines)
        len_rec = (len_tel_book_lines-1)//5

        num_rec = 1 # номер записи в файле.
        for i in range(len_tel_book_lines-1):
            if (i%5 == 0):
                print(f"Запись №{num_rec}:")
                num_rec += 1
            print(tel_book_lines[i])

        print(f"Какую именно запись из {len_rec} по порядку Вы хотите изменить?")
        number_journal = int(input('Введите номер записи, если передумали вносить изменения, введите 0: '))
        
        if number_journal > 0:
            while number_journal > len_rec:
                print('Ты дурак?! Даю тебе последний шанс')
                number_journal = int(input('Введите номер записи: '))

            print("Поля справочника:")
            print("1 - Имя")
            print("2 - Фамилия")
            print("3 - Телефон")
            print("4 - Адрес")
            field = int(input('Введите номер поля, которое хотите изменить. Если передумали вносить изменения, введите 0: '))
            
            if field > 0:
                while field > 4:
                    print('Ты дурак?! Даю тебе последний шанс')
                    number_journal = int(input('Введите номер поля: '))

                num_begin_record = (number_journal-1)*5
                index_line = num_begin_record + field - 1

                # print(f"Вводим инфу в строку с индексом: {index_line}")

                field_data = input(f"Введите информацию для поля {field} записи {number_journal}: ")
                tel_book_lines[index_line] = field_data

                with open('data_first_variant.csv', "w", encoding='utf-8') as data:
                    data.write("\n".join(tel_book_lines))

    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        # ТУТ НАПИСАТЬ КОД
        # Можно добавить проверку, чтобы человек не выходил за пределы записи


def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Имя | Фамилия | Телефон | Адрес")
        with open('data_first_variant.csv', "r", encoding="utf-8") as data:
            tel_book = data.read()
        tel_book_lines = tel_book.split("\n")
        len_tel_book_lines = len(tel_book_lines)
        len_rec = (len_tel_book_lines-1)//5

        num_rec = 1 # номер записи в файле.
        for i in range(len_tel_book_lines-1):
            if (i%5 == 0):
                print(f"Запись №{num_rec}:")
                num_rec += 1
            print(tel_book_lines[i])

        print(f"Какую именно запись из {len_rec} по порядку Вы хотите удалить?")
        number_journal = int(input('Введите номер записи, если передумали удалять, введите 0: '))
        
        if number_journal > 0:
            while number_journal > len_rec:
                print('Ты дурак?! Даю тебе последний шанс')
                number_journal = int(input('Введите номер записи: '))

            num_begin_record = (number_journal-1)*5
            # print(f"Индекс первой строки записи: {num_begin_del_line}")

            del1 = tel_book_lines.pop(num_begin_record)
            del2 = tel_book_lines.pop(num_begin_record)
            del3 = tel_book_lines.pop(num_begin_record)
            del4 = tel_book_lines.pop(num_begin_record)
            tel_book_lines.pop(num_begin_record)

            with open('data_first_variant.csv', "w", encoding='utf-8') as data:
                data.write("\n".join(tel_book_lines))

            print(f"Запись №{number_journal} была удалена со всем своим содержимым:")
            print(del1)
            print(del2)
            print(del3)
            print(del4)

    else:
        print("Имя | Фамилия | Телефон | Адрес")
        with open('data_second_variant.csv', "r", encoding="utf-8") as data:
            tel_book = data.read()
            print(tel_book)
        print("")
        tel_book_lines = tel_book.split("\n")
        len_rec = len(tel_book_lines)-1

        print(f"Какую именно запись из {len_rec} по порядку Вы хотите удалить?")
        number_journal = int(input('Введите номер записи, если передумали удалять, введите 0: '))
        
        if number_journal > 0:
            while number_journal > len_rec:
                print('Ты дурак?! Даю тебе последний шанс')
                number_journal = int(input('Введите номер записи: '))

            del_tel_book_lines = tel_book_lines.pop(number_journal-1)
            print(f"Удалена запись: {del_tel_book_lines}")
            with open('data_second_variant.csv', "w", encoding='utf-8') as data:
                data.write("\n".join(tel_book_lines))