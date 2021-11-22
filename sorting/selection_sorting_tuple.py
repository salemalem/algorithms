from ast import literal_eval as make_tuple

# Selection Sorting tuple

def swapPositions(list_argument, pos1, pos2):     
    list_argument[pos1], list_argument[pos2] = list_argument[pos2], list_argument[pos1]
    return list_argument
 

tuple_input = input("Enter a tuple like (1, 2, 3): ")
converted_tuple_from_input = make_tuple(tuple_input)
# converted_tuple_from_input = (9, 8, 10, 1, 2, 4, 6, 5, 7, 3)
# converted_tuple_from_input = ('b', 'a', 'c', 'e', 'd')
unsorted_list_from_tuple = list(converted_tuple_from_input)

print("Unsorted list: ", unsorted_list_from_tuple)
for outer_iterator in range(len(unsorted_list_from_tuple)):
  outer_element = unsorted_list_from_tuple[outer_iterator]
  minimum_element = outer_element
  for inner_element in unsorted_list_from_tuple[outer_iterator:]:
    # inner_iterator_inner_index = inner_iterator0 + outer_iterator
    if minimum_element > inner_element:
      minimum_element = inner_element

  print("Minimum element: ", minimum_element)
  # sorted_list.append(minimum_element)
  # unsorted_list_from_tuple.remove(minimum_element)
  minimum_element_index = unsorted_list_from_tuple.index(minimum_element)
  swapPositions(unsorted_list_from_tuple, minimum_element_index, outer_iterator)
  print("Unsorted list: ", unsorted_list_from_tuple)
  
print("Sorted list: ", unsorted_list_from_tuple)