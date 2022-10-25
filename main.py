# from calories_intake import CalculateCaloriesIntake
# from build_workout import build_workout
# from send_workout_to_email import send_email
# from actions import add_exercise_to_accessory
# from UserInformation import UserInformation
# from exception import WrongUserInfo, CaloriesError, WorkoutError, WrongEmailError, WrongExercise
from interface import save_your_name_to_app, calculate_your_calories, build_workout_for_today, \
    add_exercise_to_accessory, send_your_workout_to_email


def main():
    try:
        print(f' CHOOSE OPTION TO DO: '
              f' [1] CALCULATE YOUR CALORIES'
              f' [2] BUILD YOUR WORKOUT FOR TODAY'
              f' [3] SEND WORKOUT_TO_EMAIL'
              f' [4] ADD YOUR NAME TO APP'
              f' [5] ADD YOURS EXERCISE TO THE PLAN')
        choose = int(input(f'Choose what you want to do:'))
        if choose == 1:
            calculate_your_calories()
        elif choose == 2:
            build_workout_for_today()
        elif choose == 3:
            send_your_workout_to_email()
        elif choose == 4:
            save_your_name_to_app()
        elif choose == 5:
            new_data = {}
            key = input(print('Enter name of exercise: '))
            value = input(print('Enter version of exercise: '))
            new_data[key] = value
            add_exercise_to_accessory(new_data=new_data)
        else:
            print('Closing the app')
    except TypeError:
        print('Type error try again')


if __name__ == '__main__':
    main()
