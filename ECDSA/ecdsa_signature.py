import ecdsa

private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
public_key = private_key.get_verifying_key()

print("Введіть повідомлення для підпису:")
message = input().encode('UTF-8')
signature = private_key.sign(message)

print("Ваш приватний ключ:")
print(private_key.to_string().hex())
print("Ваш публічний ключ:")
print(public_key.to_string().hex())
print("Підпис:")
print(signature.hex())
