from math import factorial

approx_sum = 1 # starting sum

x = 16
for n in range(1, 101):
  approx_sum += (x ** n) / (factorial(n))

approx_sum = round(approx_sum, 5)
print(approx_sum)