x = float(input("Введіть значення x:"))
import math
if x >= 3.86:
    y = math.sqrt(2.25 * x + math.pow(x,2) + math.log10(math.fabs(x)))
elif x > 1.54:
    y = math.exp(x) + (12 * math.pow(x,2) - 1) / (x + 9)
else:
    y = math.log(math.fabs(x)) - math.pow(x,x)
print("y=", y)