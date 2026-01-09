import random
import string

def _rand(n: int = 8) -> str:
    alphabet = string.ascii_lowercase + string.digits
    return "".join(random.choice(alphabet) for _ in range(n))

def make_user() -> dict:
    r = _rand(10)
    return {
        "email": f"auto_{r}@mail.test",
        "password": f"Pwd_{r}",
        "name": f"User_{r[:6]}",
    }
