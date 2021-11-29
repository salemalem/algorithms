def calc_sum(my_digit):
  print(my_digit)
  if len(my_digit) == 1:
    return int(my_digit[0])
  else:
    return int(my_digit[0]) + int(calc_sum(my_digit[1:]))

print(calc_sum('123'))