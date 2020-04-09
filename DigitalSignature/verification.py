def hash(astring, tablesize):
    sum = 0
    for i in astring:
        sum = sum + ord(i) ** (astring.index(i) + 1)
    return sum % tablesize

def verification(hash1, hash2):
    if hash1 == hash2:
        print("\nПовідомлення достовірне")
    else:
        print("\nПовідомлення не достовірне. Хеш суми не співпадають!")

s = input("Введіть повідомлення: ")
sign = int(input("Введіть підпис: "))
e = int(input("Введіть відкритий ключ e: "))
n = int(input("Введіть модуль n: "))

hash = hash(s, 20000)
s_hash = sign ** e % n

print("Розрахований хеш: " + str(hash))
print("Обчислений з підпису хеш: " + str(s_hash))
verification(hash, s_hash)
