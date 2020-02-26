alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
print("Start!\nРозмір алфавіту: ", len(alph))
result = ""
step = int(input('Введіть крок зсуву: '))
while step >= len(alph):
    print("Завеликий крок зсуву, повторіть")
    step = int(input('Введіть крок зсуву: '))
message = input("Повідомлення: ").upper()
for i in message:
    if alph.index(i) - step < 0:
        result += alph[len(alph) - step + alph.index(i)]
    else:
        result += alph[alph.index(i) - step]
print("Результат:")
print(result)