def Vigenere_encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    message = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        message += chr(value + 65)
    return message


def Vigenere_decrypt(ciphered, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphered_int = [ord(i) for i in ciphered]
    message = ''
    for i in range(len(ciphered_int)):
        value = (ciphered_int[i] - key_as_int[i % key_length]) % 26
        message += chr(value + 65)
    return message 

def Caesar_encrypt(plaintext, key):
    plaintext_int = [ord(i) for i in plaintext]
    message = ''
    for i in range(len(plaintext_int)):
        val = (plaintext_int[i] - key - 1) % 26;
        message += chr(val + 65)
    return message

def Caesar_decrypt(ciphered, key):
    ciphered_int = [ord(i) for i in ciphered]
    message = ''
    for i in range(len(ciphered_int)):
        val = (ciphered_int[i] + key + 1) % 26;
        message += chr(val + 65)
    return message

def Caesar_break(ciphered):
    ciphered_letters = [i for i in ciphered]
    count = [0 for i in range(26)]
    for i in ciphered_letters:
        count[ord(i) - 65] +=1
    most_common = chr(count.index(max(count)) + 65)
    key1 = ord(most_common) - ord('E') + 2
    key2 = ord(most_common) - ord('A') + 2
    key3 = ord(most_common) - ord('I') + 2
    print(Caesar_decrypt(ciphered, key1))
    print(Caesar_decrypt(ciphered, key2))
    print(Caesar_decrypt(ciphered, key3))
    
def Vernam_encrypt(plaintext, key):
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    message = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i]) % 26
        message += chr(value + 65)
    return message

def Vernam_decrypt(ciphered, key):
    key_as_int = [ord(i) for i in key]
    ciphered_int = [ord(i) for i in ciphered]
    message = ''
    for i in range(len(ciphered_int)):
        value = (ciphered_int[i] - key_as_int[i]) % 26
        message += chr(value + 65)
    return message 
    
print("Choose type:\n")
print("1. Caesar\n")
print("2. Vigenere\n")
print("3. Vernam")

a = int(input())

if a == 1:
    print("Encrypt, Decrypt or Break\n")
    print("1. Encrypt\n")
    print("2. Decrypt\n")
    print("3. Break")
    b = int(input())
    if b == 1:
        print("Enter message")
        adress = str(input())
        print("Enter key")
        key = int(input())
        print(Caesar_encrypt(adress, key))
    if b == 2:
        print("Enter message")
        adress = str(input())
        print("Enter key")
        key = int(input())
        print(Caesar_decrypt(adress, key))
    if b == 3:
        print("Enter message")
        adress = str(input())
        print(Caesar_break(adress, key))
if a == 2:
    print("Encrypt or Decrypt\n")
    print("1. Encrypt\n")
    print("2. Decrypt")
    b = int(input())
    if b == 1:
        print("Enter message")
        adress = str(input())
        print("Enter key")
        key = int(input())
        print(Vigenere_encrypt(adress, key))
    if b == 2:
        print("Enter message")
        adress = str(input())
        print("Enter key")
        key = int(input())
        print(Vigenere_decrypt(adress, key))
if a == 3:
    print("Encrypt or Decrypt\n")
    print("1. Encrypt\n")
    print("2. Decrypt")
    b = int(input())
    if b == 1:
        print("Enter message")
        adress = str(input())
        print("Enter key")
        key = int(input())
        print(Vernam_encrypt(adress, key))
    if b == 2:
        print("Enter message")
        adress = str(input())
        print("Enter key")
        key = int(input())
        print(Vernam_decrypt(adress, key))
    
    
