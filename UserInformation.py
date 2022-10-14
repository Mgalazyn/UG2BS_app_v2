class UserInformation:
    def __init__(self):
        self.first_name = str(input('What\'s your name: '))
        self.last_name = str(input('What\'s your last_name: '))
        self.age = int(input('How old are you?: '))
        self.height = int(input('How tall are you(in cm)?:  '))
        self.weight = int(input('What\'s your weight(in kg)?: '))
        self.header = 'USER INFO'

    def __str__(self):
        return (f' User information: First name: {self.first_name}, Last name: {self.last_name}, Age: {self.age}'
              f' Height: {self.height}, Weight: {self.weight}')

    def save_info_to_csv_folder(self):
        with open('User_info.csv', 'a') as f:
            f.write(f" {self.header} \n"
                    f"User's name is {self.first_name} \n"
                    f"User's surname is {self.last_name} \n"
                    f"User's age is {self.age} \n"
                    f"User's height is {self.height} cm \n"
                    f"User's weight is {self.weight}  kg\n "
                    f"\n")

