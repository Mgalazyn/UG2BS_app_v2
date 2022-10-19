from UserInformation import UserInformation


class CalculateCaloriesIntake(UserInformation):
    def __init__(self):
        super().__init__()
        self.daily_activity = float(input('How much activity you have daily (1.0 to 2.0):? '))
        self.gender = str(input('What\'s your gender(men/women)?:'))

    def __str__(self):
        return (f' Calories calculator for {self.first_name} {self.last_name}: '
                f'{self.calories_intake}')

    def daily_calories_intake(self): #equation by Harris-Benedict
        if self.gender.lower() == 'men':
            daily_calories_m = (66.5 + (13.75 * self.weight) + (5.003 * self.height) - (6.775 * self.age)) \
                               * self.daily_activity
            print(f' Your daily calories intake is {daily_calories_m:.2f} cal')
        elif self.gender.lower() != 'men':
            daily_calories_w = (655.1 + (9.563 * self.weight) + (1.85 * self.height) - (4.676 * self.age)) \
                               * self.daily_activity
            print(f' Your daily calories intake is {daily_calories_w:.2f} cal')
        else:
            print('Incorrect answer, input (men/women)')


