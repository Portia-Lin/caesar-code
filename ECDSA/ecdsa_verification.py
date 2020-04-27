import ecdsa

print("Введіть повідомлення для перевірки достовірності:")
message = input().encode('UTF-8')
print("Введіть публічний ключ:")
public_key = input()
print("Введіть підпис:")
signature = input()

try:
    pk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)
except:
    print("Неправильний публічний ключ!")

try:
    if pk.verify(bytes.fromhex(signature), message):
        print("Повідомлення достовірне!")
except:
    print("Повідомлення недостовірне!")
