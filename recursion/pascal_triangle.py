def pascal_number(row, column, height):
    if row == 1 or row == 2:
        return 1
    elif column == 1 or column == height:
        return 1
    else:
        return pascal_number(row - 1, column - 1) + pascal_number(row - 1, column)

# print(pascal_number(2, 2))
# print(pascal_number(4, 2))
height = 4
for i in range(height + 1):
    