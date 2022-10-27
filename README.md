# UG2BS_app_v2


Console application for gym members, or new gym comers to help them calculate daily calories intake, 
build a free traning plan for each day (pre-programmed training plan by personal trainer with 10 years experience)
program have a possiblity to interact with user, or even send traning plan to him by email.


### Installation
The instalation for UG2BS_app_v2 requires Python 3.9 or greater.

### Installation from GitHub

To Clone the GitHub repository and then install

```bash
  git clone https://github.com/Mgalazyn/UG2BS_app_v2.git
  cd UG2BS_app_v2
  pip install -r requirements.txt
```


## Run Locally

Clone the project from GitHub

```bash
  git clone https://github.com/Mgalazyn/UG2BS_app_v2.git
```

Go to the project directory

```bash
  cd UG2BS_app_v2
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  npm run main.py
```


## Usage/Examples

```python
from calories_intake import CalculateCaloriesIntake
from build_workout import build_workout
from send_workout_to_email import send_email
from actions import add_exercise_to_accessory
from UserInformation import UserInformation
from exception import WrongUserInfo, CaloriesError, WorkoutError, WrongEmailError, WrongExercise
from interface import save_your_name_to_app, calculate_your_calories, build_workout_for_today, \
     add_exercise_to_accessory, send_your_workout_to_email


def main():
    while True:
        try:
            print(f' CHOOSE OPTION TO DO: \n'
                  f' [1] CALCULATE YOUR CALORIES \n'
                  f' [2] BUILD YOUR WORKOUT FOR TODAY \n'
                  f' [3] SEND WORKOUT_TO_EMAIL \n'
                  f' [4] ADD YOUR NAME TO APP \n'
                  f' [5] ADD YOURS EXERCISE TO THE PLAN \n'
                  f' [6] QUIT ')
            choose = int(input(f'Choose what you want to do: \n'))
            if choose == 1:
                calculate_your_calories()
            elif choose == 2:
                build_workout_for_today()
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
        except TypeError:
            print('Try again')


if __name__ == '__main__':
    main()

```

