from Crypto.Cipher import AES

cipher_message = bytearray.fromhex(input("Введіть зашифроване повідомлення: "))
key = bytearray.fromhex(input("Введіть ключ: "))
nonce = bytearray.fromhex(input("Введіть значення Nonce: "))

try:
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    plain_text = cipher.decrypt(cipher_message)
    print("Розшифроване повідомлення:", plain_text.decode('UTF-8'))
except:
    print("Не вдалося розшифрувати повідомлення...")
