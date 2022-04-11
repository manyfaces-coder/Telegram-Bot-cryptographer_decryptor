# -*- coding: utf-8 -*-
import telebot

import morse
import a1z26 as az
import binary_code as bi_c
import vigener_cipher as vc
from caesar_cipher import cipher_cipher_using_lookup


bot = telebot.TeleBot('TOKEN')
C_KEY = 1
VC_KEY = [52]
IN_TEXT = ''
SHIFT_DIRECTION = 'right'
CIPHER_KEY = 0
LANGUAGE_CIPHER = 'ru'


@bot.message_handler(commands=["start"])
def start(message):
    check_unic_user(message.from_user.id)
    save_today_user(message.from_user.id)
    bot.send_message(message.from_user.id, "Привет, я помогу тебе зашифровать и рассшифровать твои сообщения!\n"
                                           "Чтобы выбрать шифр введите команду /choose_cipher")


def check_unic_user(user_id):
    unic_file = open('unic_users.csv', 'r+', encoding='utf8')
    new = 0
    for line in unic_file.readlines():
        if str(user_id)[:9] == line[:9]:
            new += 1
    if new == 0:
        unic_file.write('\n' + str(user_id) + '\n')



def save_today_user(user_id):
    today_us = open('today_users.csv', 'w', encoding='utf8')
    today_us.write('\n' + str(user_id))

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.from_user.id, 'Для начала вам необходимо выбрать шифр с помощью функции "choose_cipher" в '
                                           'меню внизу слева(по умолчанию выбран Шифр Цезаря).\n'
                                           'В каждом шифре по умолчанию уже заданы некоторые параметры, но вы можете их '
                                           'поменять используя всплывающую клавиатуру.\n'
                                           'После того как вы зашифровали или расшифровали ваш текст, для повторного '
                                           'действия вам снова необходимо выбрать нужное вам действие на всплывающей '
                                           'клавиатуре.\n'
                                           'В случае возниконовения вопросов писать на почту oas19@tpu.tu в теме указать'
                                           ' "Телеграм - бот"')


@bot.message_handler(commands=["choose_cipher"])
def choose_cipher(message):
    keyboard = telebot.types.InlineKeyboardMarkup()  # наша клавиатура
    key_caesar = telebot.types.InlineKeyboardButton(text='Шифр Цезаря', callback_data='caesar')  # кнопка «Да»
    keyboard.add(key_caesar)  # добавляем кнопку в клавиатуру
    key_vigener = telebot.types.InlineKeyboardButton(text='Шифрование по Виженеру', callback_data='vigener')
    keyboard.add(key_vigener)
    key_binary = telebot.types.InlineKeyboardButton(text='Двоичный код', callback_data='binary')
    keyboard.add(key_binary)
    key_a1z26 = telebot.types.InlineKeyboardButton(text='Шифр A1Z26', callback_data='a1z26')
    keyboard.add(key_a1z26)
    key_morse = telebot.types.InlineKeyboardButton(text='Код Морзе', callback_data='morse')
    keyboard.add(key_morse)
    bot.send_message(message.from_user.id, text="Выберите Шифр", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global SHIFT_DIRECTION, CIPHER_KEY, LANGUAGE_CIPHER
    if call.data == "caesar":
        CIPHER_KEY = 0

        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('О Шифре Цезаря')
        keyboard.row('Задать ключ сдвига', 'Выбрать направление сдвига')
        keyboard.row('Зашифровать текст', 'Расшифровать текст')
        bot.send_message(call.message.chat.id, 'Вы выбрали шифр Цезаря!\n - Ключ сдивга = ' + str(C_KEY) + '\n'
                                                                                                           ' - Направление сдвига: вправо\n\nВыберите действие!👇',
                         reply_markup=keyboard)
    elif call.data == "vigener":
        CIPHER_KEY = 1

        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('О Шифре Виженера', 'Пример шифрования Виженера')
        keyboard.row('Зашифровать текст', 'Расшифровать текст')
        keyboard.row('Задать ключ')
        bot.send_message(call.message.chat.id, 'Вы выбрали шифр Виженера!\n\nВыберите действие!👇',
                         reply_markup=keyboard)

    elif call.data == "morse":
        CIPHER_KEY = 2
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('О коде Морзе')
        keyboard.row('Выбрать язык')
        keyboard.row('Зашифровать текст', 'Расшифровать текст')
        bot.send_message(call.message.chat.id, 'Вы выбрали код Морзе!\n - Язык: Русский\n\nВыберите действие!👇',
                         reply_markup=keyboard)

    elif call.data == "binary":
        CIPHER_KEY = 3
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('О Двоичном Коде')
        keyboard.row('Зашифровать текст', 'Расшифровать текст')
        bot.send_message(call.message.chat.id, 'Вы выбрали шифрование в Довичный код!'
                                               '\n\nВыберите действие!👇', reply_markup=keyboard)


    elif call.data == "a1z26":
        CIPHER_KEY = 4
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('О шифре A1Z26')
        keyboard.row('Зашифровать текст', 'Расшифровать текст')
        keyboard.row('Выбрать язык')
        bot.send_message(call.message.chat.id, 'Вы выбрали Шифр A1Z26!\n - Язык: Русский'
                                               '\n\nВыберите действие!👇', reply_markup=keyboard)

    elif call.data == "right":
        SHIFT_DIRECTION = 'right'
        bot.send_message(call.message.chat.id, 'Выбран сдвиг вправо')

    elif call.data == "left":
        SHIFT_DIRECTION = 'left'
        bot.send_message(call.message.chat.id, 'Выбран сдвиг влево')

    elif call.data == "ru":
        LANGUAGE_CIPHER = call.data
        bot.send_message(call.message.chat.id, 'Выбранный язык: Русский')

    elif call.data == "en":
        LANGUAGE_CIPHER = call.data
        bot.send_message(call.message.chat.id, 'Выбранный язык: Английский')

    bot.answer_callback_query(call.id)


@bot.message_handler(content_types=["text"])
def text_handler(message):
    if message.text == "Задать ключ сдвига":
        bot.send_message(message.chat.id, 'Впишите ключ:')
        bot.register_next_step_handler(message, caesar_key)

    elif message.text == "Задать ключ":
        bot.send_message(message.chat.id, 'Впишите ключ:')
        bot.register_next_step_handler(message, vigener_key)

    elif message.text == "Зашифровать текст":
        if CIPHER_KEY == 0:
            bot.send_message(message.from_user.id, 'Введите текст:')
            bot.register_next_step_handler(message, caesar_crypt)
        elif CIPHER_KEY == 1:
            bot.send_message(message.from_user.id, 'Введите текст:')
            bot.register_next_step_handler(message, vigener_crypt)
        elif CIPHER_KEY == 2:
            bot.send_message(message.from_user.id, 'Введите текст:')
            bot.register_next_step_handler(message, morse_crypt)
        elif CIPHER_KEY == 3:
            bot.send_message(message.from_user.id, 'Введите текст:')
            bot.register_next_step_handler(message, binary_crypt)
        elif CIPHER_KEY == 4:
            bot.send_message(message.from_user.id, 'Введите текст:')
            bot.register_next_step_handler(message, a1z26_crypt)

    elif message.text == "Расшифровать текст":
        if CIPHER_KEY == 0:
            bot.send_message(message.from_user.id, 'Введите текст:')
            bot.register_next_step_handler(message, caesar_decrypt)
        elif CIPHER_KEY == 1:
            bot.send_message(message.from_user.id, 'Введите текст:')
            bot.register_next_step_handler(message, vigener_decrypt)
        elif CIPHER_KEY == 2:
            bot.send_message(message.from_user.id, 'Введите текст:')
            bot.register_next_step_handler(message, morse_decrypt)
        elif CIPHER_KEY == 3:
            bot.send_message(message.from_user.id, 'Введите текст:')
            bot.register_next_step_handler(message, binary_decrypt)
        elif CIPHER_KEY == 4:
            bot.send_message(message.from_user.id, 'Введите текст:')
            bot.register_next_step_handler(message, a1z26_decrypt)

    elif message.text == "Выбрать направление сдвига":
        keyboard = telebot.types.InlineKeyboardMarkup()  # наша клавиатура
        shift_right = telebot.types.InlineKeyboardButton(text='Сдвиг вправо', callback_data='right')
        keyboard.add(shift_right)  # добавляем кнопку в клавиатуру
        shift_left = telebot.types.InlineKeyboardButton(text='Сдвиг влево', callback_data='left')
        keyboard.add(shift_left)
        bot.send_message(message.from_user.id, text="Выберите сторону сдвига", reply_markup=keyboard)

    elif message.text == "Выбрать язык":
        keyboard = telebot.types.InlineKeyboardMarkup()  # наша клавиатура
        ru_lang = telebot.types.InlineKeyboardButton(text='Русский', callback_data='ru')
        keyboard.add(ru_lang)  # добавляем кнопку в клавиатуру
        en_lang = telebot.types.InlineKeyboardButton(text='Английский', callback_data='en')
        keyboard.add(en_lang)
        bot.send_message(message.from_user.id, text="Выберите сторону сдвига", reply_markup=keyboard)

    elif message.text == "О Шифре Цезаря":
        bot.send_message(message.from_user.id, 'Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в '
                                               'открытом тексте заменяется символом, находящимся на некотором постоянном '
                                               'числе позиций левее или правее него в алфавите. Например, в шифре со '
                                               'сдвигом 3 А была бы заменена на Г, Б станет Д, и так далее.'
                                               'По умолчанию ключ сдвига = 1, направление сдвига - вправо')

        img = open('pictures/caesar_info.jpeg', 'rb')
        bot.send_photo(message.chat.id, img)

    elif message.text == "О Шифре Виженера":
        bot.send_message(message.from_user.id, 'Шифр Виженера состоит из последовательности нескольких шифров Цезаря с '
                                               'различными значениями сдвига. Для зашифровывания может использоваться '
                                               'таблица алфавитов, называемая tabula recta или квадрат (таблица) '
                                               'Виженера. Применительно к латинскому алфавиту таблица Виженера '
                                               'составляется из строк по 26 символов, причём каждая следующая строка '
                                               'сдвигается на несколько позиций. Таким образом, в таблице получается 26 '
                                               'различных шифров Цезаря. На каждом этапе шифрования используются '
                                               'различные алфавиты, выбираемые в зависимости от символа ключевого слова.'
                         )

        img = open('pictures/vigenere-cipher-0.png', 'rb')
        bot.send_photo(message.chat.id, img)

    elif message.text == "Пример шифрования Виженера":

        img = open('pictures/example_vigener.png', 'rb')
        bot.send_photo(message.chat.id, img)

    elif message.text == "О коде Морзе":
        bot.send_message(message.from_user.id, 'Азбука Морзе — код Морзе, «Морзянка» — способ кодирования букв '
                                               'алфавита, цифр, знаков препинания и других символов при помощи длинных '
                                               'и коротких сигналов, так называемых «тире» и «точек» (а также пауз, '
                                               'разделяющих буквы). \nЗа единицу времени принимается длительность одной '
                                               'точки. Длительность тире равна трём точкам. Пауза между знаками в '
                                               'букве — одна точка, между буквами в слове — 3 точки, между словами '
                                               '— 7 точек.'
                         )
        img = open('pictures/morse.jpg', 'rb')
        bot.send_photo(message.chat.id, img)

    elif message.text == "О Двоичном Коде":
        bot.send_message(message.from_user.id, 'Текстовые данные вполне можно хранить и передавать в двоичном коде. '
                                               'В этом случае по таблице символов (чаще всего ASCII) каждое простое '
                                               'число из предыдущего шага сопоставляется с буквой: 01100001 = 97 = «a», '
                                               '01100010 = 98 = «b», etc. При этом важно соблюдение регистра.')

        img = open('pictures/binary.jpg', 'rb')
        bot.send_photo(message.chat.id, img)

    elif message.text == "О шифре A1Z26":
        bot.send_message(message.from_user.id, 'Шифр A1Z26 - простой шифр, основан на простой подстановке, где каждая '
                                               'буква заменяется своим порядковым номером в алфавите. '
                                               'Буква Ё не считается буква, Я под номером 32.\n'
                                               'При шифровании текста таким образом, разделение между словами и знаки '
                                               'препинания пропадают')


def vigener_key(message):
    global VC_KEY
    key = message.text
    bot.send_message(message.from_user.id, 'Ваш ключ: ' + key)
    VC_KEY = vc.encode_val(key)


def caesar_key(message):
    global C_KEY
    C_KEY = message.text
    if C_KEY.isdigit():
        bot.send_message(message.from_user.id, 'Ваш ключ: ' + str(C_KEY))
    elif int(C_KEY.isdigit()) == float(C_KEY.isdigit()):
        bot.send_message(message.from_user.id, 'Число дожно быть целым  и положительны')
        bot.register_next_step_handler(message, caesar_key)
    else:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        bot.register_next_step_handler(message, caesar_key)

def a1z26_crypt(message):
    in_text = message.text
    bot.send_message(message.from_user.id, 'Ваш текст: ' + in_text)
    ans = az.a1z26_encrypt(in_text, lang=LANGUAGE_CIPHER)
    bot.send_message(message.from_user.id, 'Шифр:')
    bot.send_message(message.from_user.id, ans)


def a1z26_decrypt(message):
    in_text = message.text
    bot.send_message(message.from_user.id, 'Ваш текст: ' + in_text)
    ans = az.a1z26_decrypt(in_text, lang=LANGUAGE_CIPHER)
    bot.send_message(message.from_user.id, 'Шифр:')
    bot.send_message(message.from_user.id, ans)


def binary_crypt(message):
    in_text = message.text
    bot.send_message(message.from_user.id, 'Ваш текст: ' + in_text)
    ans = bi_c.text_to_bits(in_text)
    bot.send_message(message.from_user.id, 'Шифр:')
    bot.send_message(message.from_user.id, ans)


def binary_decrypt(message):
    in_text = message.text
    bot.send_message(message.from_user.id, 'Ваш шифр: ' + in_text)
    ans = bi_c.text_from_bits(in_text)
    bot.send_message(message.from_user.id, 'Расшифровка:')
    bot.send_message(message.from_user.id, ans)


def morse_crypt(message):
    in_text = message.text
    bot.send_message(message.from_user.id, 'Ваш текст: ' + in_text)
    ans = morse.encrypt(in_text, lang=LANGUAGE_CIPHER)
    bot.send_message(message.from_user.id, 'Шифр:')
    bot.send_message(message.from_user.id, ans)


def morse_decrypt(message):
    in_text = message.text
    bot.send_message(message.from_user.id, 'Ваш шифр: ' + in_text)
    ans = morse.decrypt(in_text, lang=LANGUAGE_CIPHER)
    bot.send_message(message.from_user.id, 'Расшифровка:')
    bot.send_message(message.from_user.id, ans)


def vigener_crypt(message):
    in_text = message.text
    bot.send_message(message.from_user.id, 'Ваш текст: ' + in_text)
    ans_1 = vc.full_encode(value=vc.encode_val(in_text), key=VC_KEY)
    ans = ''.join(vc.decode_val(ans_1))
    bot.send_message(message.from_user.id, 'Шифр: \n' + ans)


def vigener_decrypt(message):
    in_text = message.text
    bot.send_message(message.from_user.id, 'Ваш шифр: ' + in_text)
    ans_1 = vc.full_decode(value=vc.encode_val(in_text), key=VC_KEY)
    ans = ''.join(vc.decode_val(ans_1))
    bot.send_message(message.from_user.id, 'Расшифровка:')
    bot.send_message(message.from_user.id, ans)


def caesar_crypt(message):
    global SHIFT_DIRECTION
    in_text = message.text
    display_shift_direct = 'вправо' if SHIFT_DIRECTION == 'right' else 'влево'
    bot.send_message(message.from_user.id, 'Ваш текст: ' + in_text + '\nНаправление сдвига: ' + display_shift_direct +
                     '\nКлюч сдвига=  ' + str(C_KEY))
    ans = cipher_cipher_using_lookup(text=in_text, key=int(C_KEY), decrypt=False, shift_type=SHIFT_DIRECTION)
    bot.send_message(message.from_user.id, ans)


def caesar_decrypt(message):
    global SHIFT_DIRECTION
    in_text = message.text
    display_shift_direct = 'вправо' if SHIFT_DIRECTION == 'right' else 'влево'
    bot.send_message(message.from_user.id, 'Ваш шифр: ' + in_text + '\nНаправление сдвига: ' + display_shift_direct +
                     '\nКлюч сдвига=  ' + str(C_KEY))
    ans = cipher_cipher_using_lookup(text=in_text, key=int(C_KEY), decrypt=True, shift_type=SHIFT_DIRECTION)
    bot.send_message(message.from_user.id, 'Расшифровка:')
    bot.send_message(message.from_user.id, ans)


bot.polling(none_stop=True, interval=0)
