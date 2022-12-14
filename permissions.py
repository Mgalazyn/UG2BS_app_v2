from dataclasses import dataclass
from enum import Enum


class Role(Enum):
    ADMIN = "ADMIN"
    USER = "USER"
    NEW_USER = 'NEW_USER'


@dataclass
class User:
    first_name: str
    last_name: str
    login: str
    role: Role

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


@dataclass
class Admin:
    first_name: str
    last_name: str
    login: str
    role: Role


@dataclass
class NewUser:
    first_name: str
    last_name: str
    login: str
    role: Role


def has_role(role):
    def check_user(user):
        return user.role is role

    return check_user

