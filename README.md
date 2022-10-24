# UG2BS_app_v2


Console application for gym members, or new gym comers to help them calculate daily calories intake, 
build a free traning plan for each day (pre-programmed training plan by personal trainer with 10 years experience)
program have a possiblity to interact with user, or even send traning plan to him by email.


### Installation
The instalation for UG2BS_app_v2 requires Python 3.9 or greater.

### Installation from GitHub

To Clone the GitHub repository and then install

```bash
  git clone https://github.com/Mgalazyn/UG2BS_app_v2.git
  cd UG2BS_app_v2
  pip install -r requirements.txt
```


## Run Locally

Clone the project from GitHub

```bash
  git clone https://github.com/Mgalazyn/UG2BS_app_v2.git
```

Go to the project directory

```bash
  cd UG2BS_app_v2
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  npm run main.py
```


## Usage/Examples

```python
from build_workout import build_workout
from send_workout_to_email import send_email


def main():
    p = build_workout()
    send_email(p)


if __name__ == '__main__':
    main()


```

