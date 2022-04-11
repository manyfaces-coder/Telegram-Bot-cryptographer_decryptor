# -*- coding: utf-8 -*-

import string

letters_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяа'

symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits + " " + string.punctuation + letters_ru


def cipher_cipher_using_lookup(text, key, symbols=symbols, decrypt=False, shift_type='right'):
    n = len(symbols)

    if decrypt == True:
        key = n - key

    if shift_type == "left":
        # если требуется сдвиг влево, мы просто инвертируем key
        key = -key

    table = str.maketrans(symbols, symbols[key:] + symbols[:key])

    translated_text = text.translate(table)

    return translated_text
