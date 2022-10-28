from calories_intake import CalculateCaloriesIntake
from build_workout import build_workout
from send_workout_to_email import send_email
from actions import add_exercise_to_accessory
from UserInformation import UserInformation
from exception import WrongUserInfo, CaloriesError, WorkoutError, WrongEmailError, WrongExercise


def save_your_name_to_app():
    try:
        u = UserInformation()
        u.save_info_to_csv_folder()
        # print(u.save_info_to_csv_folder())
    except WrongUserInfo:
        print('Please re-enter your details.. ')


def calculate_your_calories():
    try:
        c = CalculateCaloriesIntake()
        c.daily_calories_intake()
        # print(c.daily_calories_intake())
    except CaloriesError:
        print('Please re-enter your details for calories calculator..')


def build_workout_for_today():
    try:
        print(build_workout())
    except WorkoutError:
        print('Please try again..')


def add_your_exercises_to_the_plan():
    try:
        data = {"Name": "FLOOR PRESS", "Version": "LANDMINE"}
        add_exercise_to_accessory(new_data=data)
    except WrongExercise:
        print('Try adding exercise again')


def send_your_workout_to_email():
    try:
        send_email(message=str(build_workout()))
        print('Sending workout...')
    except WrongEmailError:
        print('Wrong email address..')
