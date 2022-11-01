from exception import UserNotFound
from permissions import User, Role, Admin, NewUser


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
    ),
    NewUser(
        first_name='NEW USER',
        last_name='NEW USER SURNAME',
        login='NEW USER',
        role=Role.NEW_USER
    )
]


def find_user_by_login(login):
    lowered_login = login.lower()
    for user in users:
        if lowered_login == user.login.lower():
            print('Log in successfully')
            return user
    raise UserNotFound
