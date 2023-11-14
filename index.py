"""
Буквы, цифры и спец.символы из таблицы ascii (1 - 3 import)
Модуль генерации случайного числа (4 import)
"""
from string import ascii_letters
from string import digits as digits_ascii
from string import punctuation
from random import randint

ALPHABET = ascii_letters
DIGITS = digits_ascii
PUNCTUATION = punctuation
PASSWORD_SYMBOLS = ALPHABET + DIGITS + PUNCTUATION
PASSWORD_SYMBOLS_LEN = len(PASSWORD_SYMBOLS)

password_len = int(input("Введите длину пароля: "))
password = ""

for i in range(password_len):
    rand_index = randint(0, PASSWORD_SYMBOLS_LEN)
    rand_symbol = PASSWORD_SYMBOLS[rand_index]

    password += rand_symbol

print(f"Ваш пароль - {password}")
