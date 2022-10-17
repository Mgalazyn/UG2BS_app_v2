from tabulate import tabulate


class CreatePlan:
    def __init__(self, main_lift, additional_exercises):
        self.main_lift = main_lift
        self.additional_exercises = additional_exercises
        self.training_days = int(input('How many day a week would you like to train?: '))
        self.traning_plan = [] * self.traning_days

    # def add_main_lift(self):

