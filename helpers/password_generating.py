import random
import string

def generate_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return password

password = generate_password()