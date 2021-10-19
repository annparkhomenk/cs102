def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for i in plaintext:
        if i.isalpha():
            o = ord(i)
            if (97 <= o <= 122 - shift) or (65 <= o <= 90 - shift):
                ciphertext += chr(o + shift)
            else:
                ciphertext += chr(o + shift - 26)
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for i in ciphertext:
        if i.isalpha():
            o = ord(i)
            if i.islower():
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
            plaintext += i

    return plaintext
