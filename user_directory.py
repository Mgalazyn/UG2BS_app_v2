from exception import UserNotFound
from permissions import User, Role, Admin

users = [
    Admin(
        first_name='Marcin',
        last_name='Galazyn',
        login="ADMIN",
        role=Role.ADMIN
    ),
    User(
        first_name='Kacper',
        last_name='Kongo',
        login='USER',
        role=Role.USER
    )
]


def add_new_user():
    first_name = input('What\'s your name?: ')
    last_name = input('What\'s your last name?: ')
    login = input('Add your login: ')
    role = f'{login}'
    NewUser = (first_name, last_name, login, role)
    users.append(NewUser)
    return users


def find_user_by_login(login):
    lowered_login = login.lower()
    for user in users:
        if lowered_login == user.login.lower():
            print('Log in successfully')
            return user
    raise UserNotFound

