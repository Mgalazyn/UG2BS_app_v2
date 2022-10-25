from UserInformation import UserInformation


class CalculateCaloriesIntake(UserInformation):
    def __init__(self):
        super().__init__()
        self.daily_activity = float(input('How much activity you have daily (1.0 to 2.0):? '))
        self.gender = str(input('What\'s your gender(men/women)?:'))

    def __str__(self):
        return (f' Calories calculator for {self.first_name} {self.last_name}: '
                )

    def daily_calories_intake(self): #equation by Harris-Benedict
        if self.gender.lower() == 'men':
            daily_calories_m = (66.5 + (13.75 * self.weight) + (5.003 * self.height) - (6.775 * self.age)) \
                               * self.daily_activity
            macro_of_diet_m = f"Protein: {((daily_calories_m * 0.3) / 4):.2f} g " \
                              f"Carbs: {((daily_calories_m * 0.5) / 4):.2f} g " \
                              f"Fats: {((daily_calories_m * 0.2) / 9):.2f} g "
            print(f' Your daily calories intake is {daily_calories_m:.2f} cal \n'
                  f' and your macros are {macro_of_diet_m}')
        elif self.gender.lower() != 'men':
            daily_calories_w = (655.1 + (9.563 * self.weight) + (1.85 * self.height) - (4.676 * self.age)) \
                               * self.daily_activity
            macro_of_diet_w = f"Protein: {((daily_calories_w * 0.3) / 4):.2f} g " \
                              f"Carbs: {((daily_calories_w * 0.5) / 4):.2f} g " \
                              f"Fats: {((daily_calories_w * 0.2) / 9):.2f} g "
            print(f' Your daily calories intake is {daily_calories_w:.2f} cal \n'
                  f' and your macros are {macro_of_diet_w}')
        else:
            print('Incorrect answer, input (men/women)')


p = CalculateCaloriesIntake()
print(p.daily_calories_intake())
