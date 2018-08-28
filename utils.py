def search_in_array_of_dicts(array, key, value):
  for item in array:
    if item[key] == value:
      return item
