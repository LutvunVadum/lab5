import math

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
h = float(input("Введіть значення h: "))

values = []

for x in range(int(a), int(b) + 1):
    f_x = math.e**x + math.sqrt(abs(x))
    values.append(f_x)
    print(f"x = {x:.2f}, f(x) = {f_x:.2f}")

print("Список значень функції:", values)

values.sort()
print("4 найменші елементи списку:", values[:4])