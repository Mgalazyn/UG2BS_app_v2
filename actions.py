import json
import user_directory
from exception import UserNotFound
from os import path
from datetime import datetime, timedelta
import config


def add_exercise_to_accessory(new_data, filename='data_exercises/accesory_exercises.json'):
    if path.isfile(filename) is False:
        raise Exception('File not found')
    with open(filename, 'r+') as f:
        file_data = json.load(f)
        file_data["accesory_exercises"].append(new_data)
        f.seek(0)
        json.dump(file_data, f, indent=4)


def login():
    failed_login_attempts = 0
    lock_time = timedelta()
    last_attempt_dt = None
    while True:
        user_login = input("Type in your login: ")
        if last_attempt_dt is not None:
            login_attempts_in = datetime.now() - last_attempt_dt
            last_attempt_dt = datetime.now()
            if login_attempts_in < lock_time:
                failed_login_attempts += 1
                print('Failed authorization')
                continue
        last_attempt_dt = datetime.now()
        try:
            return user_directory.find_user_by_login(user_login)
        except UserNotFound:
            failed_login_attempts += 1
            print('User not in database - please try again: ')
            if failed_login_attempts >= config.AUTH_FAILED_U_LIMIT:
                lock_time = config.AUTH_FAILED_LOCK_TIME * 2
                print(f"Wait {lock_time} s before next attempt")
            elif failed_login_attempts >= config.AUTH_FAILED_LIMIT:
                lock_time = config.AUTH_FAILED_LOCK_TIME
                print(f"Wait {lock_time} s before next attempt")


