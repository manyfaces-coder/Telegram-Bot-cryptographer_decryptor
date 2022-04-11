
def cipher_decrypt_lower(ciphertext, key, lang = 'ru'):

    decrypted = ""
    ciphertext.lower()

    if lang == 'ru':
        for c in ciphertext:

            # if c.islower():
            if c.isalpha() == True:

                c_index = ord(c) - ord('а')

                c_og_pos = (c_index - key) % 33 + ord('а')

                c_og = chr(c_og_pos)

                decrypted += c_og

            else:
                c_index = ord(c) - ord('0')

                c_og_pos = (c_index - key) % 10 + ord('0')

                c_og = chr(c_og_pos)

                decrypted += c_og

    # elif lang == 'en':
    #     for c in ciphertext:
    #
    #         # if c.islower():
    #         if c.isalpha() == True:
    #
    #             c_index = ord(c) - ord('а')
    #
    #             c_og_pos = (c_index - key) % 33 + ord('а')
    #
    #             c_og = chr(c_og_pos)
    #
    #             decrypted += c_og
    #
    #         else:
    #             c_index = ord(c) - ord('0')
    #
    #             c_og_pos = (c_index - key) % 10 + ord('0')
    #
    #             c_og = chr(c_og_pos)
    #
    #             decrypted += c_og

            # else:
            #
            #     decrypted += c

    return decrypted
import string
# alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяа' \
#              'бвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#227 символов
#168
# def cipher_cipher_using_lookup(text, key, characters = string.ascii_lowercase + string.ascii_uppercase +
#                                                        string.digits + " "+ string.punctuation + alfavit_RU,
#                                                         decrypt=False, shift_type='right'):
#
#     # if key < 0:
#     #
#     #     print("key cannot be negative")
#     #
#     #     return None
#
#     n = len(characters)
#
#     if decrypt==True:
#
#         key = n - key
#
#     if shift_type=="left":
#
#         # если требуется сдвиг влево, мы просто инвертируем key
#         key = -key
#
#     table = str.maketrans(characters, characters[key:]+characters[:key])
#
#     translated_text = text.translate(table)
#
#     return translated_text

cryptic_text = "ТXгвчъьцуяXцвдвчуXгвюуXёоXвфьёуяXOWWW"

for i in range(0,33):

    plain_text = cipher_decrypt_lower(cryptic_text.lower(), i, lang='ru')

    # plain_text = cipher_cipher_using_lookup(cryptic_text.lower(), i)

    print("For key {}, decrypted text: {}".format(i, plain_text))