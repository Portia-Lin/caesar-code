import binascii

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def decrypt_block(c):
    m = modinv(c**d, n)
    if m == None: print("Немає оберненого за модулем числа для: " + str(c) + ".")
    return m

def decrypt_string(s):
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])

def hex2str(h):
    return binascii.unhexlify(h)

result = ""
s = (hex2str(input("Введіть повідомлення для розшифрування: ")).decode('utf-8'))
d = int(input("Введіть закритий ключ d: "))
n = int(input("Введіть модуль n: "))
for i in s:
    result += decrypt_string(str(i))
print("Розшифроване повідомлення: " + result)