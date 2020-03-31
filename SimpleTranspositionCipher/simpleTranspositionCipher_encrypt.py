import random

def encrypt(msg):
    i = 0
    temp = ""
    temp_list = []
    d = {}
    while len(msg) - key_length < 0:
        msg += chr(random.randrange(ord("А"), ord("Я")))
    while i < key_length:
        temp_list.append(int(permutation[i]) - 1)
        d[temp_list[i]] = msg[i]
        i += 1
    for key in sorted(d.keys()):
        temp += d[key]
    return temp

def slicer(message):
    result = ""
    temp = message.replace(" ", "")
    temp_list = [encrypt(temp[i:i + key_length]) for i in range(0, len(temp), key_length)]
    for i in range(len(temp_list)):
        result += temp_list[i]
    return result

print("Start!")
message = input("Повідомлення: ")
key_length = int(input("Введіть довжину ключа: "))
permutation = input("Введіть ключ: ")
print("Зашифроване повідомлення: ")
print(slicer(message))
