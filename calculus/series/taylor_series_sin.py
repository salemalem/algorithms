# incorrect! fix it!
from math import factorial , pi

x = pi/3
# x = 10**-8

approx_sum = x # starting sum, point a

for n in range(1, 51):
  approx_sum += ((-1) ** (n + 1)) * (x ** (2 * n + 1)) / (factorial(2 * n + 1))

approx_sum = round(approx_sum, 5)
print(approx_sum)
