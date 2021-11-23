from ast import literal_eval as make_tuple
from string import punctuation

# Selection Sorting string with special characters

def swapPositions(list_argument, pos1, pos2):     
    list_argument[pos1], list_argument[pos2] = list_argument[pos2], list_argument[pos1]
    return list_argument

string_with_special_chars = "i@mksw)84*#~\'\"<1xb"
print("Original string:", string_with_special_chars)

alphabets = []
numbers = []
special_chars = []

for char in string_with_special_chars:
    if char.isalpha():
        alphabets.append(char)
    elif char.isdigit():
        numbers.append(int(char))
    elif char in punctuation:
        special_chars.append(char)

print("Unsorted alphabets:", alphabets)
print("Unsorted numbers:", numbers)
print("Unsorted special characters:", special_chars)

# 1. Sorting alphabets
for outer_iterator in range(len(alphabets)):
  outer_element = alphabets[outer_iterator]
  minimum_element = outer_element
  for inner_element in alphabets[outer_iterator:]:
    # inner_iterator_inner_index = inner_iterator0 + outer_iterator
    if minimum_element > inner_element:
      minimum_element = inner_element
  minimum_element_index = alphabets.index(minimum_element)
  swapPositions(alphabets, minimum_element_index, outer_iterator)

print("Sorted alphabets:", alphabets)

# 2. Sorting numbers
for outer_iterator in range(len(numbers)):
  outer_element = numbers[outer_iterator]
  minimum_element = outer_element
  for inner_element in numbers[outer_iterator:]:
    # inner_iterator_inner_index = inner_iterator0 + outer_iterator
    if minimum_element > inner_element:
      minimum_element = inner_element
  minimum_element_index = numbers.index(minimum_element)
  swapPositions(numbers, minimum_element_index, outer_iterator)

print("Sorted numbers:", numbers)


# 3. Sorting special characters
for outer_iterator in range(len(special_chars)):
  outer_element = special_chars[outer_iterator]
  minimum_element = outer_element
  for inner_element in special_chars[outer_iterator:]:
    # inner_iterator_inner_index = inner_iterator0 + outer_iterator
    if minimum_element > inner_element:
      minimum_element = inner_element
  minimum_element_index = special_chars.index(minimum_element)
  swapPositions(special_chars, minimum_element_index, outer_iterator)

print("Sorted special characters:", special_chars)