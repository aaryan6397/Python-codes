def encrypt(message, shift):

    encrypted = ""

    for ch in message:

        if ch.isalpha():

            base = ord('A') if ch.isupper() else ord('a')

            encrypted += chr((ord(ch) - base + shift) % 26 + base)

        else:
            encrypted += ch

    return encrypted


def decrypt(message, shift):

    return encrypt(message, -shift)


text = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted_text = encrypt(text, shift)

print("Encrypted Message:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)

print("Decrypted Message:", decrypted_text)