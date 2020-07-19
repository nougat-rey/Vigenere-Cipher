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

def manager(msg, key, option):

    #Need checks:

    # Capital letters
    # Dealing with spaces and symbols and non-alphanumeric input

    matrix = generate_cipher_matrix()
    keystream = get_keystream(key, len(msg))

    if option == "--encode":
        cipher = ""
        item = 0
        while item < len(msg):
            cipher+=num_to_alpha(matrix
                [alpha_to_num(keystream[item])-1]
                [alpha_to_num(msg[item])-1]
            )
            item+=1
        return cipher

    if option == "--decode":
        cipher = msg
        msg = ""
        item = 0
        while item < len(cipher):
            #for each letter
            row = 0
            while row < 26:
                if num_to_alpha(matrix[row][alpha_to_num(keystream[item])-1]) == cipher[item]:
                    msg+=num_to_alpha(row+1)
                row += 1
            item += 1
        return msg

def test():
    # Test Case 1 (simple encode)
    try:
        cipher = manager("attackatdawn", "pie", "--encode")
        if cipher == "pbxpkopbhper":
            print("Test Case 1: Pass")
        else:
            print("Test Case 1: Fail")
    except Exception as error:
        print("Test Case 1: Fail - "+ error)

    # Test Case 2 (simple decode)
    try:
        msg = manager("pbxpkopbhper", "pie", "--decode")
        if msg == "attackatdawn":
            print("Test Case 2: Pass")
        else:
            print("Test Case 2: Fail")
    except Exception as error:
        print("Test Case 2: Fail - "+ error)

    # Test Case 3 (encode with capital letters)

    # Test Case 4 (encode with symbols)

    # Test Case 5 (decode with capital letters)

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
