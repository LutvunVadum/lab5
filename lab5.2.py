import math

A = list(map(float, input("Введіть координати точки A (x, y): ").split()))
B = list(map(float, input("Введіть координати точки B (x, y): ").split()))
C = list(map(float, input("Введіть координати точки C (x, y): ").split()))

p = [('A', A), ('B', B), ('C', C)]

min_sum = float('inf')
best_point_name = ''
best_point = None

for name, point in p:
    distance_sum = abs(point[0]) + abs(point[1])
    if distance_sum < min_sum:
        min_sum = distance_sum
        best_point_name = name
        best_point = point


distance_to_origin = math.sqrt(best_point[0]**2 + best_point[1]**2)

print(f"Точка з найменшою сумою відстаней до осей: {best_point_name}")
print(f"Відстань від цієї точки до початку координат: {distance_to_origin:.2f}")