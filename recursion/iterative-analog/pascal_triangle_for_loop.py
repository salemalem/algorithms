height = 6
pascal_triangle = []
for row in range(height + 1):
  current_row = []
  for column in range(row + 1):
    if row == 0 or column == 0 or column == row:
      current_row.append(1)
    else:
      result = pascal_triangle[row - 1][column - 1] + pascal_triangle[row - 1][column]
      current_row.append(result)
  pascal_triangle.append(current_row)

for row in pascal_triangle:
  print(row)