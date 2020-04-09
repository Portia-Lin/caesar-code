def hash(astring, tablesize):
    sum = 0
    for i in astring:
        sum = sum + ord(i) ** (astring.index(i) + 1)
    return sum % tablesize

s = input("Введіть повідомлення для підпису: ")
d = int(input("Введіть закритий ключ d: "))
n = int(input("Введіть модуль n: "))

hash = hash(s, 20000)
sign = hash ** d % n

print("Розрахований хеш: " + str(hash))
print("Підпис: " + str(sign))
