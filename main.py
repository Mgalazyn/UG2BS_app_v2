from UserInformation import UserInformation
from calories_intake import CalculateCaloriesIntake


def run_example():
    s = CalculateCaloriesIntake()
    print(s.daily_calories_intake())


if __name__ == '__main':
    run_example()
