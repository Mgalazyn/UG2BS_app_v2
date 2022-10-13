class UserInformation:
    def __init__(self):
        self.first_name = str(input('What\'s your name: '))
        self.last_name = str(input('What\'s your last_name: '))
        self.age = int(input('How old are you?: '))
        self.height = int(input('How tall are you(in cm)?:  '))
        self.weight = int(input('What\'s your weight(in kg)?: '))

    def __str__(self):
        return (f' User information: First name: {self.first_name}, Last name: {self.last_name}, Age: {self.age}'
              f' Height: {self.height}, Weight: {self.weight}')


