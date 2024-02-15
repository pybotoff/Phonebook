import csv

def display_records() -> None:
    """
    Функция для отображения всех записей в телефонной книге.
    Если файл не существует, он будет создан.
    """
    try:
        with open('book.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        with open('book.csv', 'w') as file:
            pass
        display_records()

def add_record() -> None:
    """
    Функция для добавления новой записи в телефонную книгу.
    Запрашивает у пользователя данные и записывает их в файл.
    """
    # Запрашиваем у пользователя фамилию
    surname = input("Введите фамилию: ")
    # Запрашиваем у пользователя имя
    name = input("Введите имя: ")
    # Запрашиваем у пользователя отчество
    patronymic = input("Введите отчество: ")
    # Запрашиваем у пользователя название организации
    organization = input("Введите название организации: ")
    # Запрашиваем у пользователя рабочий телефон
    work_phone = input("Введите рабочий телефон: ")
    # Запрашиваем у пользователя личный телефон
    personal_phone = input("Введите личный телефон: ")
    with open('book.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([surname, name, patronymic, organization, work_phone, personal_phone])

def edit_record() -> None:
    """
    Функция для редактирования записи в телефонной книге.
    Запрашивает у пользователя фамилию для поиска записи и новые данные для этой записи.
    """
    surname = input("Введите фамилию записи для редактирования: ")
    records = []
    with open('book.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == surname:
                print("Редактирование записи: ", row)
                name = input("Введите новое имя: ")
                patronymic = input("Введите новое отчество: ")
                organization = input("Введите новое название организации: ")
                work_phone = input("Введите новый рабочий телефон: ")
                personal_phone = input("Введите новый личный телефон: ")
                records.append([surname, name, patronymic, organization, work_phone, personal_phone])
            else:
                records.append(row)
    with open('book.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(records)

def search_records() -> None:
    """
    Функция для поиска записей в телефонной книге.
    Запрашивает у пользователя данные для поиска и выводит все найденные записи.
    """
    search = input("Введите данные для поиска: ")
    with open('book.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if search in row:
                print(row)
            else:
                print('Таких записей не обнаружено!')

while True:
    print("\n1. Вывести записи\n2. Добавить запись\n3. Редактировать запись\n4. Поиск записей\n5. Выход")
    choice = input("Выберите действие: ")
    if choice == '1':
        display_records()
    elif choice == '2':
        add_record()
    elif choice == '3':
        edit_record()
    elif choice == '4':
        search_records()
    elif choice == '5':
        break
