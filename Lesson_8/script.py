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
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))

        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()

            while number_journal > (len(data_first)//5):
                print('Ты дурак?! Даю тебе последний шанс')
                number_journal = int(input('Введите номер записи: '))

            data_first_version_second = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_version_second.append(''.join(data_first[j:i + 1]))
                    j = i+1
        data_first_version_second.pop(number_journal-1)

        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.writelines(data_first_version_second)

    

    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))

        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data_second = list(file.readlines())

            while number_journal > (len(data_second)//2):
                print('Ты дурак?! Даю тебе последний шанс')
                number_journal = int(input('Введите номер записи: '))
            data_second.pop(2*number_journal - 2)
            data_second.pop(2*number_journal - 2)
            
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.writelines(data_second)
        
    input_data()


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

        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()

            while number_journal > (len(data_first)//5):
                print('Ты дурак?! Даю тебе последний шанс')
                number_journal = int(input('Введите номер записи: '))

            data_first_version_second = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_version_second.append(''.join(data_first[j:i + 1]))
                    j = i+1
        data_first_version_second.pop(number_journal-1)

        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.writelines(data_first_version_second)

    
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))

        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data_second = list(file.readlines())

            while number_journal > (len(data_second)//2):
                print('Ты дурак?! Даю тебе последний шанс')
                number_journal = int(input('Введите номер записи: '))

            data_second.pop(2*number_journal - 2)       #такой индекс нужен для избежания попадания на переносы строки
            data_second.pop(2*number_journal - 2)        # удаляем два раза, так как удаляем запись, а затем перенос после нее
            print(data_second)

        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.writelines(data_second)


def copy_data():
    print('Из какого файла Вы хотите скопировать данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  
        print("Какую именно запись по счету Вы хотите скопировать?")
        number_journal = int(input('Введите номер записи: '))

        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
            while number_journal > (len(data_first)//5):
                print('Ты дурак?! Даю тебе последний шанс')
                number_journal = int(input('Введите номер записи: '))

            data_first_version_second = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_version_second.append(''.join(data_first[j:i + 1]))
                    j = i+1

        data = ';'.join(data_first_version_second[number_journal-1].split('\n'))  #замена переносов строки на точку с запятой
        data = data[:-2] + '\n\n'  #последний два переноса строки, которые нам нужны, переводятся тоже в точку с запятой
        # поэтому мы их срезаем и добавляем нужные переносы
            
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.writelines(data)


    else:
        print("Какую именно запись по счету Вы хотите cкопировать?")
        number_journal = int(input('Введите номер записи: '))

        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data_second = list(file.readlines())

            while number_journal > (len(data_second)//2):
                print('Ты дурак?! Даю тебе последний шанс')
                number_journal = int(input('Введите номер записи: '))

            data = '\n'.join(data_second[number_journal*2 - 2].split(';'))

        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.writelines(data+'\n')
 
