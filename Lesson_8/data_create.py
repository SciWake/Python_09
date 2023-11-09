def name_data():
    name = input('Введите "Имя": ')
    print('Очень красивое имя)')
    return name


def surname_data():
    surname = input('Введите "Фамилию": ')
    return surname


def phone_data():
    phone = input('Введите "Телефон": ')
    return phone


def address_data():
    address = input('Введите "Адрес": ')
    return address


def set_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    return name, surname, phone, address
