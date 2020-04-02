alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
result = ""
d = {}
counter = 0

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

print()
print("Статистика: ")
for key in sorted(d.keys()):
    print("Символ {} становить {:.1f}% тексту".format(key, 100 / counter * d[key]))

letter = get_key(d, max(d.values()))
for i in message:
    result += decrypt(i, alph.index(letter) - alph.index(" "))
print("В повідомленні символів: " + str(counter))
print("Найбільш повторювана літера: " + str(letter))
print("Крок зсуву: " + str(alph.index(letter) + 1))
print()
print("Розшифроване повідомлення: ")
print(result)