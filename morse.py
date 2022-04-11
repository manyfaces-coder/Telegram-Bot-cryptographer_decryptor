# -*- coding: utf-8 -*-
import dict_symbs

def encrypt(message, lang='ru'):
    cipher = ''
    message = message.upper()
    if lang == 'ru':
        DICT_MORSE_CODE = dict_symbs.RU_DICT_MORSE_CODE
    else:
        DICT_MORSE_CODE = dict_symbs.EN_DICT_MORSE_CODE
    for symbol in message:
        if symbol == '\n':
            cipher += '\n'
        elif symbol != ' ':
            try:
                cipher += DICT_MORSE_CODE[symbol] + ' '
            except:
                return 'Символ ' + symbol + ' не распознан!\nВозможно вы выбрали не тот язык'
        else:
            cipher += ' '
    return cipher


def decrypt(message, lang='ru'):
    message += ' '
    decipher = ''
    citext = ''

    if lang == 'ru':
        DICT_MORSE_CODE = dict_symbs.RU_DICT_MORSE_CODE
    else:
        DICT_MORSE_CODE = dict_symbs.EN_DICT_MORSE_CODE
    for symbol in message:
        if (symbol != ' '):
            i = 0
            citext += symbol
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                try:
                    decipher += list(DICT_MORSE_CODE.keys())[list(DICT_MORSE_CODE
                                                                  .values()).index(citext)]
                except:
                    return 'Символ ' + symbol + ' не распознан!\nВозможно вы выбрали не тот язык'
                citext = ''
    return decipher


def main():
    message = "Всем привет я из интернет\n"
    result = encrypt(message.upper(), 'ru')
    print(result)

    message = ".-- ... . --  .--. .-. .. .-- . -  .-.-  .. --..  .. -. - . .-. -. . -"
    result = decrypt(message, 'ru')
    print(result)


if __name__ == '__main__':
    main()
