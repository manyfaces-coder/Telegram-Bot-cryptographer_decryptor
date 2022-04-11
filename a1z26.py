import os  # Only used to clear command prompt
# -*- coding: utf-8 -*-


def a1z26_encrypt(cistring, lang='ru'):
    # Encrypt string by converting each letter to a number
    string = ""  # Placeholder variable
    cistring = cistring.lower()  # Format to Lowercase
    cistring = "".join(cistring.split())  # Remove spaces from string
    if lang == 'en':
        for x in range(0, len(cistring)):  # Loop through each character of string
            char = ord(cistring[x]) - 96  # Convert character to numeric 1 - 26
            if char > 0 and char <= 26: string += str(char) + " "  # Store value in 'string' variable
    elif lang == 'ru':
        for x in range(0, len(cistring)):  # Loop through each character of string
            char = ord(cistring[x]) - 1071  # Convert character to numeric 1 - 26
            if char > 0 and char <= 33: string += str(char) + " "  # Store value in 'string' variable
    if len(string) == 0:
        return 'Сообщение пустое или вы выбрали не тот язык'
    return string # Return cipher string


def a1z26_decrypt(cistring, lang='ru'):
    # Decrypt string by converting each number to a letter
    string = ""  # Placeholder variable
    data = cistring.split()  # Split string at " "

    if lang == 'en':
        for char in data:  # Loop through each character
            char = chr(int(char) + 96)  # Convert number to letter
            string += char  # Add character to string
    elif lang == 'ru':
        for char in data:  # Loop through each character
            char = chr(int(char) + 1071)  # Convert number to letter
            string += char  # Add character to string
    return (string)  # Return cipher string


if __name__ == '__main__':
    print("A1Z26 Cipher")
    print("-------------------------------")
    cistring = input("Please enter a text string below.  All numbers will be stripped.\n")
    print("\nThe starting string is:")
    print(cistring, "\n")
    print("The A1Z26 encrypted string is:")
    print(a1z26_encrypt(cistring), "\n")
    print("The A1Z26 decrypted string is:")
    print(a1z26_decrypt(a1z26_encrypt(cistring)), "\n")
    input("Press Enter to continue...")


