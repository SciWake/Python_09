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

def show_data(contacts):
    print("\n№ | ФИО | Телефон | Адрес | Комментарий |")
    for contact in contacts:
        print(f"{contact['id']} | {contact['name']} | {contact['phone']} | {contact['adress']} | {contact['comment']}")
    print("")

def add_contact(contacts):
    fio = input("Введите ФИО: ")
    phone_number = input("Введите номер телефона: ")
    street_name = input('Введите адрес: ')
    comment = input('Введите комментарий: ')
    contact = {'id': len(contacts) + 1, 'name': fio, 'phone': phone_number, 'adress': street_name, 'comment': comment}
    contacts.append(contact)
    print(f"Добавлена запись: {contact['id']} | {contact['name']} | {contact['phone']} | {contact['adress']} | {contact['comment']}\n")

def edit_contact(contacts):
    print("\n№ | ФИО | Телефон | Адрес | Комментарий |")
    for contact in contacts:
        print(f"{contact['id']} | {contact['name']} | {contact['phone']} | {contact['adress']} | {contact['comment']}")
    print("")
    index = int(input("Введите порядковый № контакта для редактирования: ")) - 1
    if index >= 0 and index < len(contacts):
        contact = contacts[index]
        fio = input("Введите измененные данные ФИО: ")
        phone = input("Введите измененный номер телефона: ")
        street_name = input("Введите измененный адрес: ")
        comment = input("Введите измененный комментарий: ")
        if fio:
            contact['name'] = fio
        if phone:
            contact['phone'] = phone
        if street_name:
            contact['adress'] = street_name
        if comment:
            contact['comment'] = comment
        print(f"Изменена запись №{contact['id']} | {contact['name']} | {contact['phone']} | {contact['adress']} | {contact['comment']}\n")
    else:
        print("Неправильный номер контакта\n")

def delete_contact(contacts):
    print("\n№ | ФИО | Телефон | Адрес | Комментарий |")
    for contact in contacts:
        print(f"{contact['id']} | {contact['name']} | {contact['phone']} | {contact['adress']} | {contact['comment']}")
    print("")
    index = int(input("Введите номер контакта для удаления: ")) - 1
    if index >= 0 and index < len(contacts):
        contact = contacts.pop(index)
        print(f"Удалена запись №{contact['id']} | {contact['name']} | {contact['phone']} | {contact['adress']} | {contact['comment']}\n")
    else:
        print("Неправильный номер контакта\n")

def main():
    contacts = []

    while True:
        print("Выберите действие:")
        print("1 - Информации о контакте")
        print("2 - Добавить контакт")
        print("3 - Редактировать контакт")
        print("4 - Удалить контакт")
        print("0 - Выход")
        action = input("Действие: ")
        if action == '1':
            show_data(contacts)
        elif action == '2':
            add_contact(contacts)
        elif action == '3':
            edit_contact(contacts)
        elif action == '4':
            delete_contact(contacts)
        elif action == '0':
            break
        else:
            print("Неправильный выбор\n")

    print("До свидания!")
