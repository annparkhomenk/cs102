def key_word(text, keyword):
    key_int = [ord(i) - 65 for i in keyword.upper()]
    if len(key_int) < len(text):
        if len(text) % len(key_int) == 0:
            key_int = key_int * (len(text) // len(key_int))
        else:
            key_int = key_int * (len(text) // len(key_int))
            for i in range(len(text) % len(key_int)):
                key_int.append(key_int[i])
    return key_int


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""

    key_int = key_word(plaintext, keyword)

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            o = ord(plaintext[i])
            shift = key_int[i]
            if (97 <= o <= 122 - shift) or (65 <= o <= 90 - shift):
                ciphertext += chr(o + shift)
            else:
                ciphertext += chr(o - 26 + shift)
        else:
            ciphertext += plaintext[i]

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    key_int = key_word(ciphertext, keyword)
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            o = ord(ciphertext[i])
            shift = key_int[i]
            if ciphertext[i].islower():
                if o - shift >= 97:
                    plaintext += chr(o - shift)
                else:
                    plaintext += chr(o - shift + 26)
            else:
                if o - shift >= 65:
                    plaintext += chr(o - shift)
                else:
                    plaintext += chr(o - shift + 26)
        else:
            plaintext += ciphertext[i]

    return plaintext
