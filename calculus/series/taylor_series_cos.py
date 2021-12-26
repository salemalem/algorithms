from math import factorial , pi

approx_sum = 1 # starting sum, point a

x = pi/3
for n in range(1, 51):
  approx_sum += ((-1) ** n) * (x ** (2 * n)) / (factorial(2*n))

approx_sum = round(approx_sum, 2)
print(approx_sum)