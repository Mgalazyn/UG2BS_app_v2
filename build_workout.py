import json
import random


def build_workout():
    with open('data_exercises/main_lifts.json', "r") as f:
        main_lifts = json.load(f)

    with open('data_exercises/accesory_exercises.json', "r") as a:
        accesory_work = json.load(a)

    main_lifts = {k: random.choice(v) for k, v in main_lifts.items()}
    accessory_lifts = {k: random.sample(v, 3) for k, v in accesory_work.items()}
    print(f"Main lift for today is: {main_lifts} \n"
          f"Accessory lifts are: {accessory_lifts}")
    # return main_lifts, accessory_lifts

