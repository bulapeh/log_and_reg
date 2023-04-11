def start():
    user_choice = int(input('1. Авторизация; 2. Регистрация: '))
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    if user_choice == 2:
        return registration(login, password)
    elif user_choice == 1:
        return authorization(login, password)
    else:
        print('Такой команды нет.')


def length_check(login, password):
    if 3 <= len(login) <= 20 and 4 <= len(password) <= 32:
        return True
    return False


def authorization(login, password):
    if length_check(login, password):
        with open('data.txt', encoding='UTF-8') as file:
            o = file.read().splitlines()
            if (login + ':' + password) in o:
                print('Вы успешно авторизовались!')
                return True
            print('Данные не найдены.')
        return True
    print('Длина логина или пароля некорректна.')


def registration(login, password):
    if length_check(login, password):
        with open('data.txt', 'a+', encoding='UTF-8') as file:
            file.write(login + ':' + password + '\n')
            print('Вы успешно зарегистрировались!')
            return True
    print('Длина логина или пароля некорректна.')


start()
