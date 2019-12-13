def decrypt(encrypted_text: str, n: int) -> str:
    """Returns decrypted string - capable of decrypting strings encrypted with encrypt function.
    Encryption is done n times"""
    decrypted = encrypted_text
    decrypt = ''
    for i in range(n):
        for num in range(int(len(decrypted) / 2) + 1):
            a = decrypted[int((len(decrypted) / 2)):]
            b = decrypted[:int((len(decrypted) / 2))]
            try:
                decrypt += a[num] + b[num]
            except IndexError:
                if len(decrypted) % 2:
                    decrypt += a[num]
                    continue
                continue
        decrypted, decrypt = decrypt, ''

    return decrypted


def encrypt(text: str, n: int) -> str:
    """Encrypts and returns a string by concatenating string slices - first slice is every second character from the sting,
     second slice contains remaining characters. Encryption is done n times."""
    encrypted = text
    for i in range(n):
        encrypted = encrypted[1::2] + encrypted[0::2]

    return encrypted
