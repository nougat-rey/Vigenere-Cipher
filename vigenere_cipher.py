"""Vigenere Cipher Encoder and Decoder

This script allows the user to:

    * encrypt a message using a key
    * decrypt a cipher using the key used to encrypt the original message

This file can also be imported as a module and contains the following
functions:

    * num_to_alpha - converts an integer to an alphabetical letter
    * alpha_to_num - converts an alphabetical letter to an integer
    * generate_cipher_matrix - returns the matrix used for the vigenere cipher
    * encode - encodes a message using the inputted key
    * decode - decodes a cipher with the inputted key
    * manager - handles encoding and decoding
    * test - runs test cases for vigenere cipher implemented in this module
"""

import sys
from collections import deque

def num_to_alpha(num: int) -> str:
    return chr(num+96)

def alpha_to_num(alpha: str) -> int:
    return ord(alpha)-96

def generate_cipher_matrix() -> list:
    cipher_matrix = [deque([x for x in range(1, 27)]) for y in range(1, 27)]
    row = 0
    while row < 26:
        cipher_matrix[row].rotate(-row)
        row+=1
    return cipher_matrix

def get_keystream(key: str, msg_len: int) -> str:
    keystream = ""
    key_len = len(key)
    quotient, remainder = divmod(msg_len, key_len)
    times = 0
    while times < quotient:
        keystream+=key
        times+=1
    keystream+=key[0:remainder]
    return keystream

def encode(msg: list, key: str) -> list:
    matrix = generate_cipher_matrix()
    keystream = get_keystream(key, len(msg))

    cipher = []
    item = 0
    while item < len(msg):
        cipher.append(num_to_alpha(matrix
            [alpha_to_num(keystream[item])-1]
            [alpha_to_num(msg[item])-1]
        ))
        item+=1
    return cipher

def decode(cipher: list, key: str) -> list:
    matrix = generate_cipher_matrix()
    keystream = get_keystream(key, len(cipher))

    msg = []
    item = 0
    while item < len(cipher):
        row = 0
        while row < 26:
            if num_to_alpha(matrix[row][alpha_to_num(keystream[item])-1]) == cipher[item]:
                msg.append(num_to_alpha(row+1))
            row += 1
        item += 1
    return msg

def manager(msg: str, key: str, option: str) -> str:

    #Converting string to list to work with
    msg = list(msg)

    # Handling Capital letters
    capital_letters = [] #index of capital letters
    letter_index = 0
    while letter_index < len(msg):
        if msg[letter_index].isupper():
            capital_letters.append(letter_index)
            msg[letter_index] = msg[letter_index].lower()
        letter_index+=1

    #Handling spaces and other non-alphanumeric input
    original_msg = msg
    alpha_msg = []
    for item in original_msg:
        if item.isalnum():
            alpha_msg.append(item)

    if option == "--encode":
        result = encode(alpha_msg, key)

    if option == "--decode":
        result = decode(alpha_msg, key)

    #Handling Spaces and Symbols
    final_result = []
    for item in original_msg:
        if item.isalpha():
            final_result.append(result.pop(0))
        else:
            final_result.append(item)

    #Handling Capital Letters
    for letter in capital_letters:
        final_result[letter] = final_result[letter].upper()

    return "".join(final_result)

def test():
    """Test function for vigenere cipher. Goes through several test cases."""

    print("\nTest Case #1: Simple Encode")
    try:
        cipher = manager("attackatdawn", "pie", "--encode")
        expected_cipher = "pbxpkopbhper"
        if cipher == expected_cipher:
            print("Result: Pass")
        else:
            print("Result: Fail")
            print("Cipher: "+cipher)
            print("Expected Cipher: "+expected_cipher)
    except Exception as error:
        print("Error - "+ str(error))

    #--------------------------------------------------------------------------#
    print("\nTest Case #2: Simple Decode")
    try:
        msg = manager("pbxpkopbhper", "pie", "--decode")
        expected_msg = "attackatdawn"
        if msg == expected_msg:
            print("Result: Pass")
        else:
            print("Result: Fail")
            print("Message: "+msg)
            print("Expected Message: " +expected_msg)
    except Exception as error:
        print("Error - "+ str(error))

    #--------------------------------------------------------------------------#
    print("\nTest Case #3: Message with Capital Letters")
    try:
        cipher = manager("AttackAtDawn", "pie", "--encode")
        expected_cipher = "PbxpkoPbHper"
        if cipher == expected_cipher:
            print("Result: Pass")
        else:
            print("Result: Fail")
            print("Cipher: "+cipher)
            print("Expected Cipher: "+expected_cipher)
    except Exception as error:
        print("Error - "+ str(error))

    #--------------------------------------------------------------------------#
    print("\nTest Case #4: Cipher with Capital Letters")
    # Test Case 4 (decode with capital letters)
    try:
        msg = manager("PbxpkoPbHper", "pie", "--decode")
        expected_msg = "AttackAtDawn"
        if msg ==expected_msg:
            print("Result: Pass")
        else:
            print("Result: Fail")
            print("Message: "+msg)
            print("Expected Message: " +expected_msg)
    except Exception as error:
        print("Error - "+ str(error))

    #--------------------------------------------------------------------------#
    print("\nTest Case #5: Message with Symbols, Spaces and Special Characters")
    try:
        cipher = manager("Attack At Dawn!", "pie", "--encode")
        expected_cipher = "Pbxpko Pb Hper!"
        if cipher == expected_cipher:
            print("Result: Pass")
        else:
            print("Result: Fail")
            print("Cipher: "+cipher)
            print("Expected Cipher: "+expected_cipher)
    except Exception as error:
        print("Error - "+ str(error))

    #--------------------------------------------------------------------------#
    print("\nTest Case #6: Cipher with Symbols, Spaces and Special Characters")
    try:
        cipher = manager("Pbxpko Pb Hper!", "pie", "--decode")
        expected_msg = "Attack At Dawn!"
        if cipher == expected_msg:
            print("Result: Pass")
        else:
            print("Result: Fail")
            print("Message: "+msg)
            print("Expected Message: " +expected_msg)
    except Exception as error:
        print("Error - "+ str(error))

if __name__ == "__main__":

    if len(sys.argv) <= 3:
        if len(sys.argv) == 2:
            if sys.argv[1] == "--test":
                test()
                sys.exit()
        print("\n   Usage: \n")
        print("     python vigenere_cipher  <message>   <key>   --encode")
        print("     python vigenere_cipher  <cipher>   <key>   --decode")
        print("     python vigenere_cipher  --test\n")
        sys.exit()

    elif len(sys.argv) > 3:
        msg = sys.argv[1]
        key = sys.argv[2]
        option = sys.argv[3]
        if len(key) > len(msg):
            print("Error - key cannot be longer than message or cipher")
            sys.exit()
        print(manager(msg, key, option))
