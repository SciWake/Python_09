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


def edit_data():
    print('Из какого файла Вы хотите изменить данные?')
    print_data()
    number_file = int(input('Введите номер файла: '))
    
    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))


    if number_file == 1:  
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))

        with open ("data_first_variant.csv",  "r", encoding="utf-8") as data:
            lines = data.readlines()

        while number_journal > len(lines):
            print("let's do it again)!")
            number_journal = int(input('Введите номер записи: '))
        
        first_updated_data = []
        for i, line in enumerate(lines):
            if i == number_journal -1 :
                if input(f"this one? {line} \nif yes type y: ").lower() == "y":                        
                    new_value = input("What would you wish to write instead: ")
                    first_updated_data.append("".join(lines).replace(line, f"{new_value}\n"))


        with open ("data_first_variant.csv",  "w", encoding="utf-8") as file:
            file.writelines(first_updated_data)

        if input("that's it?\nif no type n: ").lower() == "n":
            edit_data()


    else:
        with open ("data_second_variant.csv",  "r", encoding="utf-8") as data:
            lines = data.readlines()
        print(*[(i+1, value) for i, value in enumerate(lines)], end="\n\n")
        print("Какую именно запись по счету Вы хотите изменить?", end="\n\n")
        number_journal = int(input('Введите номер записи: '))

        while number_journal > len(lines):
            print("let's do it again)!")
            number_journal = int(input('Введите номер записи: '))
        secnd_updated_data = []
        for i, line in enumerate(lines):
            if i == number_journal -1:
                print(*[(i+1, value) for i, value in enumerate(line.strip().split(";"))], end="\n\n")
                choose_exactly = int(input("\nЧто именно? "))

                if input(f"Вот этот? {line.split(';')[choose_exactly-1]} \n Если да так и напишите да: ").lower() == "да":                        
                    new_value = input("\nЧто написать вместо? ")
                    secnd_updated_data.append("".join(line).replace(line.split(';')[choose_exactly-1], new_value))
            else:
                secnd_updated_data.append(line)

        with open ("data_second_variant.csv",  "w", encoding="utf-8") as file:
            file.writelines(secnd_updated_data)

        if input("That's it?\nIf no type НЕТ: ").lower() == "нет":
            edit_data()
           




def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1: 
        with open("data_first_variant.csv", "r") as input_csv:
            lines = input_csv.readlines()
        count = 1

        print(*[(i+1, line) for i, line in enumerate(lines)])
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

        updated_data = []
        
        for index, line in enumerate(lines):
            print(*line.split("\n\n"))
            if index != int(choose_one) - 1:
                updated_data.append(line)
            
        with open ("data_first_variant.csv", "w") as output_csv:
            output_csv.writelines(updated_data)

        print("DONE!")

        
    else:        
        with open("data_second_variant.csv", "r", encoding="utf-8" ) as data:
            lines = data.readlines()
        count = 0
        for i in lines:
            count +=1
            print(count, i.strip())
        print(".......", end="\n")    
        choose_one = int(input(f"Какую именно запись по счету Вы хотите удалить? Выберите ЧИСЛО от 1 до {len(lines)} "))

            # ПРОВЕРКА 
        while choose_one > len(lines) :
            choose_one = int(input(f"Выберите ЧИСЛО от 1 до {len(lines)} "))
            
        updated_data = []
        if choose_one <= len(lines):
            for index, line in enumerate(lines):
                if index != choose_one - 1:
                    updated_data.append(line)

                elif index == choose_one - 1:
                    print([(i+1,u) for i, u in enumerate(line.split(";"))])
                    chose_exactly = int(input("Что именно?"))

                    ask_change = input("Чем-то заменить?\n Если да так и напишите да : ").lower()
                    if ask_change == "да":
                        edit_data()
                    
                    updated_data.append(";".join([line for i, line in enumerate(line.split(';')) if i != chose_exactly - 1]))


            with open ("data_second_variant.csv", "w") as updated_lines:
                updated_lines.writelines(updated_data)
                print("DONE!")
        else:
            print("Не выходите за пределы!")
            delete_data()
