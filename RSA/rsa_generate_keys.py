import random

p = int(input('Введіть просте число P: '))
q = int(input('Введіть просте число Q: '))
n = p * q
print("Модуль перетворень N = " + str(n))
phi = (p - 1) * (q - 1)
print("Кількість додатних цілих чисел в інтервалі від 1 до N, що взаємнопрості з N: " + str(phi))
print("Зачекайте, йде процес генерування ключів . . .")

def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x, phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x, phi):
            l.remove(x)
    return l

e = random.choice(coprimes(phi))
d = modinv(e, phi)
print("\nВаш відкритий ключ: (e = " + str(e) + ", n = " + str(n) + ").")
print("Ваш закритий ключ: (d = " + str(d) + ", n = " + str(n) + ").")
