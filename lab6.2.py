import math

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
h = float(input("Введіть значення h: "))

x = a
print("Табулювання функції (цикл з передумовою):")
while x <= b:
    f_x = math.e**x + math.sqrt(abs(x))
    print(f"x = {x:.2f}, f(x) = {f_x:.2f}")
    x += h
