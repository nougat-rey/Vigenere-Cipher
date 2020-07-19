import sys
from collections import deque

def num_to_alpha(num):
    return chr(num+96)

def alpha_to_num(alpha):
    return ord(alpha)-96

def generate_cipher_matrix():
    cipher_matrix = [deque([x for x in range(1, 27)]) for y in range(1, 27)]
    row = 0
    while row < 26:
        cipher_matrix[row].rotate(-row)
        row+=1
    return cipher_matrix

def get_keystream(key, message_len):
    keystream = ""
    key_len = len(key)
    quotient, remainder = divmod(message_len, key_len)
    times = 0
    while times < quotient:
        keystream+=key
        times+=1
    keystream+=key[0:remainder]
    return keystream

def encode(msg, key):
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

def decode(cipher, key):
    matrix = generate_cipher_matrix()
    keystream = get_keystream(key, len(cipher))

    msg = []
    item = 0
    while item < len(cipher):
        #for each letter
        row = 0
        while row < 26:
            if num_to_alpha(matrix[row][alpha_to_num(keystream[item])-1]) == cipher[item]:
                msg.append(num_to_alpha(row+1))
            row += 1
        item += 1
    return msg

def manager(msg, key, option):

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

    # Dealing with spaces and symbols and non-alphanumeric input
    # Create temporary msg without all of the spaces and symbols
    # Add the alphanumeric values back in once done

    if option == "--encode":
        result = encode(msg, key)

    if option == "--decode":
        result = decode(msg, key)

    for letter in capital_letters:
        result[letter] = result[letter].upper()
    return "".join(result)

def test():
    # Test Case 1 (simple encode)
    try:
        cipher = manager("attackatdawn", "pie", "--encode")
        if cipher == "pbxpkopbhper":
            print("Test Case 1: Pass")
        else:
            print("Test Case 1: Fail")
    except Exception as error:
        print("Test Case 1: Fail - "+ str(error))

    # Test Case 2 (simple decode)
    try:
        msg = manager("pbxpkopbhper", "pie", "--decode")
        if msg == "attackatdawn":
            print("Test Case 2: Pass")
        else:
            print("Test Case 2: Fail")
    except Exception as error:
        print("Test Case 2: Fail - "+ str(error))

    # Test Case 3 (encode with capital letters)
    try:
        cipher = manager("AttackAtDawn", "pie", "--encode")
        if cipher == "PbxpkoPbHper":
            print("Test Case 3: Pass")
        else:
            print("Test Case 3: Fail")
    except Exception as error:
        print("Test Case 3: Fail - "+ str(error))

    # Test Case 4 (encode with symbols)

    # Test Case 5 (decode with capital letters)
    try:
        msg = manager("PbxpkoPbHper", "pie", "--decode")
        if msg == "AttackAtDawn":
            print("Test Case 4: Pass")
        else:
            print("Test Case 4: Fail")
    except Exception as error:
        print("Test Case 4: Fail - "+ str(error))


    # Test Case 6 (decode with symbols)

if __name__ == "__main__":

    if len(sys.argv) <= 3:
        if len(sys.argv) == 2:
            if sys.argv[1] == "--test":
                test()
                sys.exit()
        print("Help me!")
        sys.exit()

    elif len(sys.argv) > 3:
        msg = sys.argv[1]
        key = sys.argv[2]
        option = sys.argv[3]
        print(manager(msg, key, option))
