from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

cipher_message = bytearray.fromhex(input("Введіть зашифроване повідомлення: "))
key = bytearray.fromhex(input("Введіть ключ: "))

try:
    cipher = AES.new(key, AES.MODE_ECB)
    plain_text = cipher.decrypt(cipher_message)
    print("Розшифроване повідомлення:", unpad(plain_text, AES.block_size).decode('UTF-8'))
except:
    print("Не вдалося розшифрувати повідомлення...")
