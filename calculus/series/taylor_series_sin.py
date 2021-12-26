from math import factorial , pi

# x = pi
x = pi / 4
# x = 10**-8

approx_sum = x # starting sum

# for n in range(1, 51):
#   approx_sum -= ((-1) ** (n + 1)) * (x ** (2 * n + 1)) / (factorial(2 * n + 1))

for n in range(1, 101):
  if n % 2 == 0:
    approx_sum += ((-1) ** (n + 1)) * (x ** (n + 1)) / (factorial(n + 1))


approx_sum = round(approx_sum, 5)
print(approx_sum)
