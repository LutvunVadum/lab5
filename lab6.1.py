import math

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
h = float(input("Введіть значення h: "))

print("\nТабулювання функції (цикл з параметром):")
x = a
while x <= b:
    f_x = math.exp(x) + math.sqrt(abs(x))
    print(f"f({x:.2f}) = {f_x:.4f}")
    x += h

