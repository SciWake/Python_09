# def print_data_first():
#     with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
#         data_first = file.readlines()
#         data_first_version_second = []
#         j = 0
#         for i in range(len(data_first)):
#             if data_first[i] == '\n' or i == len(data_first) - 1:
#                 data_first_version_second.append(''.join(data_first[j:i + 1]))
#                 j = i
#         data_first = data_first_version_second
#         data_first = print(''.join(data_first))
#         # print(*data_first, sep='')
#         return data_first

# print('Из какого файла Вы хотите изменить данные?')
# number_file = int(input('Введите номер файла: '))
# while number_file != 1 and number_file != 2:
#     print('Ты дурак?! Даю тебе последний шанс')
#     number_file = int(input('Введите номер файла: '))
# if number_file == 1:  # Можно сделать нумерацию внутри файла
#     print("Какую именно запись по счету Вы хотите изменить?")
#     number_journal = int(input('Введите номер записи: '))
#     while number_journal != 1 and number_journal != 2:
#         print('Ты дурак?! Даю тебе последний шанс')
#     if number_journal == 1:
#         print("Какую именно строку Вы хотите изменить?")
#     number_str1 = input('Введите имя строки (Имя, Фамилия, Телефон или Адрес): ')
#     if number_str1 == 'имя'.lower().strip():
#         number_str1 == 0
#     if number_str1 == 'фамилия'.lower().strip():
#         number_str1 == 1
#     if number_str1 == 'телефон'.lower().strip():
#         number_str1 == 2
#     if number_str1 == 'адрес'.lower().strip():
#         number_str1 == 3
#     name_str1 = str(input("Ввведите новые данные: "))
#      # ТУТ НАПИСАТЬ КОД
    
# data_first = ['Максим\n', 'Русанов\n', '76878787575\n', 'Сочи\n', '\n', 'опроап\n', 'апкрр\n', '7654\n', 'рен\n', '\n', '\n', '\n']
# data_first_version_second = []
# j = 0
# for i in range(len(data_first)):
#     if number_str1 == i:
#         data_first[i] = name_str1 + "\n"
#     if data_first[i] == '\n' or i == len(data_first) - 1:
#         data_first_version_second.append(''.join(data_first[j:i + 1]))
#         j = i
# data_first = data_first_version_second
# with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
#     file.write(''.join(data_first))
split_res = [] 
data_second = ['па', 'орповп', '867875', 'ороа\n', '\n', 'максим', 'рус', '785786', 'Варавов\n', '\n', '\n']
for i in range(len(data_second)):
    if data_second[i] == '\n':
        split_res.append(data_second[i])
    if i == 0 or data_second[i-1] == '\n':
        split_res.append(data_second[i])
    else:
        split_res[-1] = split_res[-1] + ';' + data_second[i]
data_second = split_res
for i in range(len(data_second)):
    if data_second[i] == '\n;\n':
        data_second[i] = '\n'


      
print(data_second)