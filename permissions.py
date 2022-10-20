from dataclasses import dataclass
from enum import Enum
from typing import List


class Role(Enum):
    ADMIN = "ADMIN"
    USER = "USER"


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


def has_role(role):
    def check_user(user):
        return user.role is role

    return check_user


is_admin = has_role(Role.ADMIN)
is_user = has_role(Role.USER)