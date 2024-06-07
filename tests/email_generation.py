import random
import string

def generate_login():
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    extension = random.choice(['com', 'net', 'org', 'ru'])  # Выбираем случайное расширение почтового ящика
    return f"{username}@{domain}.{extension}"

email = generate_login()
