from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

message = input("Введіть повідомлення для шифрування: ").encode('UTF-8')
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_ECB)
cipher_text_bytes = cipher.encrypt(pad(message, AES.block_size))

print("Випадково згенерований ключ:", key.hex())
print("Зашифроване повідомлення:", cipher_text_bytes.hex())
