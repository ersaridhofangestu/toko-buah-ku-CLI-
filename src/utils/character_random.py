import string
import secrets

def random(length):
    character = string.ascii_letters + string.digits
    return ''.join(secrets.choice(character) for _ in range(length)) 