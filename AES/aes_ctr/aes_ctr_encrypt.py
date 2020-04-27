from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

message = input("Введіть повідомлення для шифрування: ").encode('UTF-8')
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CTR)
cipher_text_bytes = cipher.encrypt(message)
nonce = cipher.nonce

print("Випадково згенерований ключ:", key.hex())
print("Значення Nonce:", nonce.hex())
print("Зашифроване повідомлення:", cipher_text_bytes.hex())
