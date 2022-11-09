import random

def get_random_password() -> str:
    # написать функцию генерации случайных паролей
    litter_1 = 'abcdefghijklmnopqrstuvwxyz'
    litter_2 = litter_1.upper()
    number = '0123456789'

    password_1 = random.sample(litter_1, 4)
    password_1 = ''.join(password_1)

    password_2 = random.sample(litter_2, 2)
    password_2 = ''.join(password_2)

    password_3 = random.sample(number, 2)
    password_3 = ''.join(password_3)

    password = password_1 + password_2 + password_3
    return password
print(get_random_password())
