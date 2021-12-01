height = 5
def pascal_number(row, column):
    if row <= 0 or column <= 0:
        return "I can't calculate it yet"
    elif row == 1 or row == 2 or column == 1 or column == row:
        return 1
    else:
        return pascal_number(row - 1, column - 1) + pascal_number(row - 1, column)

"""
TO DO: Edit height properly before calling the function
"""

# print(pascal_number(2, 2))
# print(pascal_number(4, 2))
# print(pascal_number(100, 50))
for row in range(1, height + 1):
    for column in range(1, row + 1):
        print(pascal_number(row, column), end=" ")
    print()
    