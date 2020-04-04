alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
frequency = [' ', 'E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']
result = ""
d = {}
counter = 0
variant = 0

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def decrypt(i, step):
    if alph.index(i) - step < 0:
        char = alph[alph.index(i) - step + len(alph)]
    else:
        char = alph[alph.index(i) - step - len(alph)]
    return char

print("Start!")
message = input("Введіть повідомлення: ")
message = message.upper()

for i in message:
    counter += 1
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

print("\nСтатистика: ")
for key in sorted(d.keys()):
    print("Символ {} становить {:.1f}% тексту".format(key, 100 / counter * d[key]))

letter = get_key(d, max(d.values()))
print("В повідомленні символів: " + str(counter))
print("Найбільш повторювана літера: " + str(letter))
print("\nРозшифроване повідомлення: ")
for i in message:
    result += decrypt(i, alph.index(letter) - alph.index(frequency[variant]))
print(result)
success = input("Повідомлення розшифровано успішно? Введіть 'Y' або 'N': ")
while success == "N":
    if variant == len(frequency) - 1:
        break
    else:
        result = ""
        for i in message:
            result += decrypt(i, alph.index(letter) - alph.index(frequency[variant + 1]))
        variant += 1
        print("\nРозшифроване повідомлення: ")
        print(result)
        success = input("Повідомлення розшифровано успішно? Введіть 'Y' або 'N': ")
print("\nВи успішно, або ні розшифрували повідомлення")