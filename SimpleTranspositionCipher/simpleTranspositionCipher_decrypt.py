def decrypt(msg):
    i = 0
    temp = ""
    temp_list = []
    d = {}
    while i < key_length:
        temp_list.append(int(transposition[i]) - 1)
        d[temp_list[i]] = msg[int(transposition[i]) - 1]
        i += 1
    for key in d.values():
        temp += key
    return temp

def slicer(message):
    result = ""
    temp = message.replace(" ", "")
    temp_list = [decrypt(temp[i:i + key_length]) for i in range(0, len(temp), key_length)]
    for i in range(len(temp_list)):
        result += temp_list[i]
    return result

print("Start!")
message = input("Повідомлення: ")
key_length = int(input("Введіть довжину ключа: "))
transposition = input("Введіть ключ: ")
print("Розшифроване повідомлення: ")
print(slicer(message))
