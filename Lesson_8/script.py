from data_create import name_data, surname_data, phone_data, address_data
import os


def get_path(mpath: str) -> os.path:
    return os.path.join(os.getcwd(), mpath)


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = int(
        input(
            f"В каком формате Вы хотите записать данные?\n\n"
            f"1 Вариант:\n\n"
            f"{surname}\n"
            f"{name}\n"
            f"{phone}\n"
            f"{address}\n\n"
            f"2 Вариант:\n\n"
            f"{surname};{name};{phone};{address}\n\n"
            f"Выберите номер варианта: "
        )
    )

    while var != 1 and var != 2:
        print("Попробуйте ещё раз выбрать правильную команду")
        var = int(input("Введите номер варианта: "))

    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf-8") as file:
            file.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    else:
        with open("data_second_variant.csv", "a", encoding="utf-8") as file:
            file.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print("Вывожу данные для Вас из 1-ого файла\n")
    with open("data_first_variant.csv", "r", encoding="utf-8") as file:
        data_first = file.readlines()
        data_first_version_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == "\n" or i == len(data_first) - 1:
                data_first_version_second.append("".join(data_first[j : i + 1]))
                j = i
        data_first = data_first_version_second
        print("".join(data_first))
        # print(*data_first, sep='')

    print("Вывожу данные для Вас из 2-ого файла\n")
    with open("data_second_variant.csv", "r", encoding="utf-8") as file:
        data_second = list(file.readlines())
        print(*data_second)
    return data_first, data_second


def edit_data():
    print("В каком файле Вы хотите изменить данные?")
    data_first, data_second = print_data()
    number_file = int(input("Введите номер файла: "))

    while number_file != 1 and number_file != 2:
        print("Ошибка ввода! Попробуйте, пожалуйста, еще раз.")
        number_file = int(input("Введите номер файла: "))

    if number_file == 1:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input("Введите номер записи: "))
        # ТУТ НАПИСАТЬ КОД
        # следующие четыре строчки запишут новые данные
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        # ниже w - взяла из лекции, я так поняла, что файл должен перезаписаться при использовании этой буквы
        with open("data_first_variant.csv", "w", encoding="utf-8") as file:
            # создала список из имеющихся записей
            data_first = list(file.readlines())
            # человек введет номер записи по порядку, а ее индекс будет меньше на 1, так как индексы начинаются с нуля
            i = number_journal - 1
            # если заданный индекс меньше размера имеющегося списка, то
            if i < len(data_first):
                # присвоила новое значение элементу списка
                data_first[i] = "{name};{surname};{phone};{address}\n\n"
                print("Контакт успешно изменен!")
            else:
                # если человек вышел за пределы имеющихся записей
                print("Контакт не найден!")
    else:  # аналогично как для первого списка в этой функции, только изменено на второй список
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input("Введите номер записи: "))
        # ТУТ НАПИСАТЬ КОД
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        with open("data_second_variant.csv", "w", encoding="utf-8") as file:
            data_second = list(file.readlines())
            i = number_journal - 1
            if i < len(data_second):
                data_second[i] = "{name};{surname};{phone};{address}\n\n"
                print("Контакт успешно изменен!")
            else:
                print("Контакт не найден!")


def delete_data():
    print("Из какого файла Вы хотите удалить данные?")
    data_first, data_second = print_data()
    number_file = int(input("Введите номер файла: "))

    while number_file != 1 and number_file != 2:
        print("Ошибка ввода! Попробуйте, пожалуйста, еще раз.")
        number_file = int(input("Введите номер файла: "))

    if number_file == 1:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input("Введите номер записи: "))
        # ТУТ НАПИСАТЬ КОД
        # w - взяла из лекции, я так поняла, что файл должен перезаписаться при использовании этой буквы
        with open("data_first_variant.csv", "w", encoding="utf-8") as file:
            # создала список из имеющихся записей
            data_first = list(file.readlines())
            # человек введет номер записи по порядку, а ее индекс будет меньше на 1, так как индексы начинаются с нуля
            i = number_journal - 1
            # если заданный индекс меньше размера имеющегося списка, то
            if i < len(data_first):
                # это удалит имеющуюся запись с заданным индексом
                del data_first[i]
                print("Контакт успешно удален!")
            else:
                # если человек вышел за пределы имеющихся записей
                print("Контакт не найден!")
    else:  # аналогично как для первого списка в этой функции, только изменено на второй список
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input("Введите номер записи: "))
        # ТУТ НАПИСАТЬ КОД
        with open("data_second_variant.csv", "w", encoding="utf-8") as file:
            data_second = list(file.readlines())
            i = number_journal - 1
            if i < len(data_second):
                del data_second[i]
                print("Контакт успешно удален!")
            else:
                print("Контакт не найден!")
