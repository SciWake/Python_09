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

def edit (csv_file):
        
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        # ТУТ НАПИСАТЬ КОД
        # Можно добавить проверку, чтобы человек не выходил за пределы записей

        with open (csv_file,  "r", encoding="utf-8") as data:
            lines = data.readlines()

        while number_journal > len(lines):
            print("let's do it again)!")
            number_journal = int(input('Введите номер записи: '))
            

        for i, line in enumerate(lines):
            if i == number_journal -1 :
                if input(f"this one? {line} \nif yes type y: ").lower() == "y":                        
                    new_value = input("What would you wish to write instead: ")
                    lines = "".join(lines).replace(line, new_value)
                else:
                    edit(csv_file)

        with open ("data_first_variant.csv",  "w", encoding="utf-8") as file:
            file.writelines(lines)

        if input("that's it?\nif no type n: ").lower() == "n":
            put_data()

def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        edit("data_first_variant.csv")

    else:
                
        print('Из какого файла Вы хотите изменить данные?')
        print_data()
        number_file = int(input('Введите номер файла: '))

        while number_file != 1 and number_file != 2:
            print('Ты дурак?! Даю тебе последний шанс')
            number_file = int(input('Введите номер файла: '))

        with open ("data_second_variant.csv",  "r", encoding="utf-8") as data:
            lines = data.readlines()
        print(*[(i+1, value) for i, value in enumerate(lines)], end="\n\n")
        print("Какую именно запись по счету Вы хотите изменить?", end="\n\n")
        number_journal = int(input('Введите номер записи: '))

        while number_journal > len(lines):
            print("let's do it again)!")
            number_journal = int(input('Введите номер записи: '))

        for i, line in enumerate(lines):
            if i == number_journal -1:
                print(*[(i+1, value) for i, value in enumerate(line.strip().split(";"))], end="\n\n")
                choose_exactly = int(input("\nЧто именно? "))

                if input(f"this one? {line.split(';')[choose_exactly-1]} \nif yes type y: ").lower() == "y":                        
                    new_value = input("\nWhat would you wish to write instead: ")
                    uptadet_data = ("".join(lines).replace(line.split(';')[choose_exactly-1], new_value))
                else:
                    edit("data_second_variant.csv")

        with open ("data_second_variant.csv",  "w", encoding="utf-8") as file:
            file.writelines(uptadet_data)

        if input("that's it?\nif no type n: ").lower() == "n":
            put_data()
           




def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1: 
        with open("data_first_variant.csv", "r") as input_csv:
            lines = input_csv.readlines()

            # нумерация внутри файла
            print([str(i+1)+ ": " + line for i, line in enumerate(lines)])
            choose_one = input("Какую именно запись по счету Вы хотите удалить? ")

            # ПРОВЕРКА 
            if choose_one.isdigit():
                    choose_one = int(choose_one)
            while isinstance(choose_one, str):
                choose_one = input("Выберите цифрами пжлйста: ")
                if choose_one.isdigit():
                    choose_one = int(choose_one)
            while choose_one > len(lines):
                choose_one = int(input(f"Выберите еще раз пжлйста в районе (от 0 до {len(lines)}): "))

            # DO NOT ADD SELECTED ONE!
            updated_data = []
            for line in lines:
                if [line] != [lines[int(choose_one) - 1]]:
                    updated_data.append(line)
                    with open ("data_first_variant.csv", "w") as output_csv:
                        output_csv.writelines(updated_data)
            print(*updated_data, "DONE!")
        
    else:        
        with open("data_second_variant.csv", "r", encoding="utf-8" ) as data:
            lines = data.readlines()
            count = 0
            for i in lines:
                count +=1
                print(count, i.strip())
            print(".......", end="\n")    
            choose_one = int(input(f"Какую именно запись по счету Вы хотите удалить? Выберите чисто от 1 до {len(lines)} "))
                # ПРОВЕРКА 
            while choose_one > len(lines):
                choose_one = int(input(f"Выберите чисто от 1 до {len(lines)} "))
                
            updated_data = []
            if choose_one <= len(lines):
                        
                for line in lines:
                    if [line] != [lines[choose_one - 1]]:
                        updated_data.append(line)

                    elif [line] == [lines[choose_one - 1]]:
                        print([(i+1,u) for i, u in enumerate(line.split(";")) ])
                        chose_exactly = int(input("Что именно?"))

                        ask_change = input("would you like to renew it?\n type y for yes: ").lower()
                        if ask_change == "y":
                            put_data()
                        
                        updated_data.append(";".join([i for i in line.split(';') if [i] != [line[chose_exactly-1]]]))


                with open ("data_second_variant.csv", "w") as updated_lines:
                    updated_lines.writelines(updated_data)
                    print(updated_data, "DONE!")
            else:
                print("Try to use numbers within the range!")
                delete_data()
    


print('Из какого файла Вы хотите изменить данные?')
print_data()
number_file = int(input('Введите номер файла: '))

while number_file != 1 and number_file != 2:
    print('Ты дурак?! Даю тебе последний шанс')
    number_file = int(input('Введите номер файла: '))
# ТУТ НАПИСАТЬ КОД
# Можно добавить проверку, чтобы человек не выходил за пределы записей

with open ("data_second_variant.csv",  "r", encoding="utf-8") as data:
    lines = data.readlines()
print(*[(i+1, value) for i, value in enumerate(lines)], end="\n\n")
print("Какую именно запись по счету Вы хотите изменить?", end="\n\n")
number_journal = int(input('Введите номер записи: '))

while number_journal > len(lines):
    print("let's do it again)!")
    number_journal = int(input('Введите номер записи: '))

for i, line in enumerate(lines):
    if i == number_journal -1:
        print(*[(i+1, value) for i, value in enumerate(line.strip().split(";"))], end="\n\n")
        choose_exactly = int(input("\nЧто именно? "))

        if input(f"this one? {line.split(';')[choose_exactly-1]} \nif yes type y: ").lower() == "y":                        
            new_value = input("\nWhat would you wish to write instead: ")
            uptadet_data = ("".join(lines).replace(line.split(';')[choose_exactly-1], new_value))
        else:
            edit("data_second_variant.csv")

with open ("data_second_variant.csv",  "w", encoding="utf-8") as file:
    file.writelines(uptadet_data)

if input("that's it?\nif no type n: ").lower() == "n":
    put_data()