from interface import save_your_name_to_app, calculate_your_calories, build_workout_for_today, \
     add_exercise_to_accessory, send_your_workout_to_email


def main():
    while True:
        try:
            print(f' CHOOSE OPTION TO DO: \n'
                  f' [1] BUILD YOUR WORKOUT FOR TODAY \n'
                  f' [2] CALCULATE YOUR CALORIES \n'
                  f' [3] SEND WORKOUT_TO_EMAIL \n'
                  f' [4] ADD YOUR NAME TO APP \n'
                  f' [5] ADD YOURS EXERCISE TO THE PLAN \n'
                  f' [6] QUIT ')
            choose = int(input(f'Choose what you want to do: \n'))
            if choose == 1:
                build_workout_for_today()
            if choose == 2:
                calculate_your_calories()
            elif choose == 3:
                send_your_workout_to_email()
            elif choose == 4:
                save_your_name_to_app()
            elif choose == 5:
                value1 = input(print('Enter name of exercise: '))
                value2 = input(print('Enter version of exercise: '))
                new_data = {"Name": value1, "Version": value2}
                add_exercise_to_accessory(new_data=new_data)
            else:
                print('Closing the app')
                break
        except TypeError:
            print('Try again')


if __name__ == '__main__':
    main()
