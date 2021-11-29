
def binary_search(sorted_array, search_value):
  for i in range(len(sorted_array) + 1):
    if sorted_array[i] == search_value:
      return i
  return "Not found"
sorted_array = [5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
search_value = 73
print(f"{search_value} found at index {binary_search(sorted_array, search_value)}")