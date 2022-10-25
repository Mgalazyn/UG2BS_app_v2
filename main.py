from build_workout import build_workout
from send_workout_to_email import send_email


def main():
    p = build_workout()
    send_email(p)


if __name__ == '__main__':
    main()
