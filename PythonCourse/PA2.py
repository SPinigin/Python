import json
import re

# Файл для хранения данных
FILE_NAME = 'users.json'


# Функция для загрузки данных из файла
def load_users():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# Функция для сохранения данных в файл
def save_users(users):
    with open(FILE_NAME, 'w') as file:
        json.dump(users, file, indent=4)


# Функция для проверки силы пароля
def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[!£$%&]', password):
        score += 1
    return score


# Функция для добавления пользователя
def add_user(users):
    while True:
        username = input("Введите идентификатор пользователя: ")
        if username in users:
            print("Этот идентификатор уже существует, выберите другой.")
        else:
            break

    while True:
        password = input("Введите пароль: ")
        strength = check_password_strength(password)

        if strength < 3:
            print("Пароль слишком слабый. Необходимо использовать другой.")
        elif strength == 3 or strength == 4:
            retry = input("Пароль можно улучшить. Хотите повторить попытку? (да/нет): ")
            if retry.lower() == 'нет':
                users[username] = password
                break
        elif strength == 5:
            print("Пароль является сильным.")
            users[username] = password
            break


# Функция для изменения пароля пользователя
def change_password(users):
    username = input("Введите идентификатор пользователя: ")
    if username not in users:
        print("Пользователь не найден.")
        return

    while True:
        password = input("Введите новый пароль: ")
        strength = check_password_strength(password)

        if strength < 3:
            print("Пароль слишком слабый. Необходимо использовать другой.")
        elif strength == 3 or strength == 4:
            retry = input("Пароль можно улучшить. Хотите повторить попытку? (да/нет): ")
            if retry.lower() == 'нет':
                users[username] = password
                break
        elif strength == 5:
            print("Пароль является сильным.")
            users[username] = password
            break


# Функция для вывода списка пользователей
def list_users(users):
    print("Список пользователей:")
    for username in users:
        print(username)


# Основная функция
def main():
    users = load_users()

    while True:
        print("\nМеню:")
        print("1) Добавить пользователя")
        print("2) Изменить пароль")
        print("3) Вывести пользователей")
        print("4) Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            add_user(users)
        elif choice == '2':
            change_password(users)
        elif choice == '3':
            list_users(users)
        elif choice == '4':
            save_users(users)
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
