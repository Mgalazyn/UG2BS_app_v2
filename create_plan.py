class CreatePlan:
    def __init__(self, main_lift, additional_exercises):
        self.main_lift = main_lift
        self.additional_exercises = additional_exercises
        self.training_days = int(input('How many day a week would you like to train?: '))


