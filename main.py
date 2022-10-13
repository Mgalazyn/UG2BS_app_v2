from UserInformation import UserInformation
from calories_intake import CalculateCaloriesIntake


def run_example():
    calories = CalculateCaloriesIntake()
    calories.daily_calories_intake()


if __name__ == '__main__':
    run_example()
