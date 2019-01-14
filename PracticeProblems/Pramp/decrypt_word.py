def decrypt(word):

    # Edge Case
    if word == "":
        return ""

    # Decrypt first char
    decrypted_word = chr(ord(word[0]) - 1)

    # Decrypt rest of word
    for i in range(1, len(word)):

        ascii_val = ord(word[i]) - ord(word[i-1])

        # Correct the val if it isnt in the a-z range
        corrected_val = correct_val(ascii_val)

        # Add the char to the decrypted word
        decrypted_word += chr(corrected_val)

    return decrypted_word


def correct_val(val):
    while val < ord("a"):
        val += 26
    return val


if __name__ == '__main__':
    word = 'dnotq'
    print(decrypt(word))
