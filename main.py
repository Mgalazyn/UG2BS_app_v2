from UserInformation import UserInformation
from calories_intake import CalculateCaloriesIntake
import pandas as pd


def run_example():
    p = UserInformation()
    p.save_info_to_csv_folder()
    fi = pd.read_csv('User_info.csv')
    print(fi)


if __name__ == '__main__':
    run_example()
