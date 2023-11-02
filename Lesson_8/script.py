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
        print('\nВаша запись создана!\n')      
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')    
        print('\nВаша запись создана!\n')      


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
        print(''.join(data_second))
    return data_first, data_second


def edit_data():
    print('Из какого файла Вы хотите изменить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))
    list_input_value  = ['имя', 'фамилию', 'номер телефона', 'город']
    if os.stat('data_first_variant.csv').st_size == 0 or os.stat('data_second_variant.csv').st_size == 0:
            print('Файл не содержит данных для изменения\nНаполните файл содержимым')
    else:        
        while number_file != 1 and number_file != 2:
            print('Ты дурак?! Даю тебе последний шанс')
            number_file = int(input('Введите номер файла: '))

        if number_file == 1:  # Можно сделать нумерацию внутри файла
            print("Какую именно запись по счету Вы хотите изменить?")
            number_journal = int(input('Введите номер записи: '))
            # проверяем сколько записей в файле и не выходим ли мы за его пределы
            with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
                lines = file.readlines()
            if  number_journal > lines.count('\n') or number_journal == 0:
                print('\nЗапись с данным номером отсутствует в файле\n')  
                   
                   
            # вносим изменения в запись файла "data_first_variant.csv"
            else:
                with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
                    start_line_record = (4 * (number_journal - 1)) + (number_journal - 1)
                    end_line_record = start_line_record + 4
                    for i in range(start_line_record, end_line_record):
                        user_input = input(f'Введите {list_input_value[i - start_line_record]}:')
                        lines[i] = f'{user_input}\n'
                    file.writelines(lines) 
                print('\nВаши изменения внесены!\n')      
                
                        
        else:
            print("Какую именно запись по счету Вы хотите изменить?")
            number_journal = int(input('Введите номер записи: '))
            # проверяем сколько записей в файле и не выходим ли мы за его пределы
            with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
                lines = file.readlines() 
            lines = '\n'.join(lines).split()    
            if  number_journal > len(lines) or number_journal == 0:
                print('\nЗапись с данным номером отсутствует в файле\n')  
                 
            # вносим изменения в запись файла "data_second_variant.csv"    
            else:    
                with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                    for i in range(len(lines)):
                        if i == number_journal - 1:
                            lines[i] = ''
                            text = ''
                            for j in range(4):
                                user_input = input(f'Введите {list_input_value[j]}: ')
                                text += f'{user_input};' 
                            lines[i] = f'{text}\n\n'
                        else:
                            lines[i] = f'{lines[i]}\n\n'        
                    file.writelines(lines) 
                print('\nВаши изменения внесены!\n')             
            
            
def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Ты дурак?! Даю тебе последний шанс')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  # Можно сделать нумерацию внутри файла
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # проверяем сколько записей в файле и не выходим ли мы за его пределы
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        if  number_journal > lines.count('\n') or number_journal == 0: 
            print('\nЗапись с данным номером отсутствует в файле\n')
        # вносим изменения в запись файла "data_first_variant.csv"       
        else:
            with open('data_first_variant.csv', 'w', encoding='utf-8') as file: 
                start_line_delete = ((number_journal - 1) * 4) + (number_journal - 1)   
                end_line_delete = start_line_delete + 4 
                for  i in range(start_line_delete, end_line_delete + 1):
                    lines[i] = ''
                file.writelines(lines) 
            print('\nВаша запись удалена!\n')
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        # проверяем сколько записей в файле и не выходим ли мы за его пределы
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            lines = file.readlines()
    
        if  number_journal > lines.count('\n') or number_journal == 0: 
            print('\nЗапись с данным номером отсутствует в файле\n')
        # вносим изменения в запись файла "data_first_variant.csv"       
        else:
            with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
                line_delete = (number_journal * 2) - 2
                lines[line_delete] = '\n'
                file.writelines(lines)
            print('\nВаша запись удалена!\n')

    
