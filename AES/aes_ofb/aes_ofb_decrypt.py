from Crypto.Cipher import AES

cipher_message = bytearray.fromhex(input("Введіть зашифроване повідомлення: "))
key = bytearray.fromhex(input("Введіть ключ: "))
iv = bytearray.fromhex(input("Введіть значення Iv: "))

try:
    cipher = AES.new(key, AES.MODE_OFB, iv=iv)
    plain_text = cipher.decrypt(cipher_message)
    print("Розшифроване повідомлення:", plain_text.decode('UTF-8'))
except:
    print("Не вдалося розшифрувати повідомлення...")
