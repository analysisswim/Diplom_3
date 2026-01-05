# helpers/user_factory.py
import random
import string


def _rand(n=8):
    return "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(n))


def make_user():
    key = _rand(10)
    return {
        "email": f"auto_{key}@mail.test",
        "password": f"Pwd_{key}",
        "name": f"User_{key[:6]}",
    }
