plaintext = input("\nEnter the plain text: ")
key = int(input("Enter the key: "))
ciphertext = ""
decryptedtext = ""

for ch in plaintext:
    pos = ord(ch)
    if 65 <= pos <= 90:
        newpos = (pos-65+key) % 26+65
    elif 97 <= pos <= 122:
        newpos = (pos-97+key) % 26+97
    elif pos == 32:
        newpos = pos
    else:
        newpos = pos
    ciphertext += chr(newpos)

print("\nPlain Text: " + plaintext)
print("Cipher Text: " + ciphertext)

for ch in ciphertext:
    pos = ord(ch)
    if 65 <= pos <= 90:
        newpos = (pos-65-key) % 26+65
    elif 97 <= pos <= 122:
        newpos = (pos-97-key) % 26+97
    elif pos == 32:
        newpos = pos
    else:
        newpos = pos
    decryptedtext += chr(newpos)

print("Decrypted Text: " + decryptedtext +"\n")
