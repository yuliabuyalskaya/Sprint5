import random
import string

def email_generation():
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    extension = random.choice(['com', 'net', 'org', 'ru'])
    return f"{username}@{domain}.{extension}"

email = email_generation()
