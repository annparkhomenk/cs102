def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for i in plaintext:
        if i.isalpha():
            if 'A' <= chr(ord(i) + shift) <= 'Z' or 'a' <= chr(ord(i) + shift) <= 'z':
                ciphertext += chr(ord(i) + shift)
            else:
                ciphertext += chr(ord(i) + shift - 26)
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for i in ciphertext:
        if i.isalpha():
            if 'A' <= chr(ord(i) - shift) <= 'Z' or 'a' <= chr(ord(i) - shift) <= 'z':
                plaintext += chr(ord(i) - shift)
            else:
                plaintext += chr(ord(i) - shift + 26)
        else:
            plaintext += i
    return plaintext
