import json
import random


def build_workout():
    with open('main_lifts.json', "r") as f:
        main_lifts = json.load(f)
        f.close()
    with open('accesory_exercises.json', "r") as a:
        accesory_work = json.load(a)
        a.close()

    main_lifts = {k: random.choice(v) for k, v in main_lifts.items()}
    accessory_lifts = {k: random.sample(v, 3) for k, v in accesory_work.items()}

    return main_lifts, accessory_lifts

