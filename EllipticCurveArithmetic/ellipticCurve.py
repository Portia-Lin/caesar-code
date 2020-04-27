a = 1
b = 4
modulo = 13
point_counter = 0
for x in range(modulo):
    z = (x**3 + a*x + b) % modulo
    for y in range(modulo):
        if y*y % modulo == z:
            point_counter += 1
            print("P"+ str(point_counter) + " (" + str(x) + ", "+ str(y) + ")")
print("Знайдено точок на еліптичній кривій:", point_counter)
