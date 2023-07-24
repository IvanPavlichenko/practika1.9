#4. Монетка-2

import math

print("Введите координаты монетки:")
x = float(input("х: "))
y = float(input("у: "))
radius = int(input("Введите радиус: "))

x_1 = 0
y_1 = 0
check_dot = math.sqrt(((x - x_1) ** 2) + ((y - y_1) ** 2))

if check_dot <= radius:
    print("Монетка где-то рядом")
else:
    print("Монетки в области нет")

