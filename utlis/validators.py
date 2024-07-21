import re


def validate_email(email: str):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False
