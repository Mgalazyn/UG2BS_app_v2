class UserInformation:
    def __init__(self, first_name, last_name, age, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return (f' User information: First name: {self.first_name}, Last name: {self.last_name}, Age: {self.age}'
              f' Height: {self.height}, Weight: {self.weight}')


name = str(input('What\'s your name: '))
surname = str(input('What\'s your last_name: '))
age_u = int(input('How old are you?: '))
height_u = int(input('How tall are you(in cm)?:  '))
weight_u = int(input('What\'s your weight(in kg)?: '))


print(UserInformation(name, surname, age_u, height_u, weight_u))
