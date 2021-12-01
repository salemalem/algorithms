
def binary_search(sorted_array, search_value):
    if search_value not in sorted_array:
        return None

    low_index = 0
    high_index = len(sorted_array)
    mid_index = (low_index + high_index) // 2

    while True:
        if sorted_array[mid_index] > search_value:
            high_index = mid_index
            mid_index = (low_index + high_index) // 2
        elif sorted_array[mid_index] < search_value:
            low_index = mid_index
            mid_index = (low_index + high_index) // 2
        elif sorted_array[mid_index] == search_value:
            return mid_index
sorted_array = [5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
search_value = 73
print(f"{search_value} found at index {binary_search(sorted_array, search_value)}")