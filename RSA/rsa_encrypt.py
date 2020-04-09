import binascii

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt_block(m):
    c = modinv(m**e, n)
    if c == None: print("Немає оберненого за модулем числа для символу: " + str(chr(m)) + ".")
    return c

def encrypt_string(s):
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])

def str2hex(s):
    return binascii.hexlify(bytes(str.encode(s)))

result = ""
s = input("Введіть повідомлення для шифрування: ")
e = int(input("Введіть відкритий ключ e: "))
n = int(input("Введіть модуль n: "))
print("Зачекайте, йде процес шифрування повідомлення . . .")
for i in s:
    result += encrypt_string(i)
print("Зашифроване повідомлення: " + str(str2hex(result).decode('utf-8')))
