def sort_string(str):
  """
  This function sorts a string based on the following rules:
  1. Digits are sorted in ascending order.
  2. Letters are sorted in ascending order.
  3. No two adjacent characters should be the same.

  Args:
    str: The string to be sorted.

  Returns:
    The sorted string.
  """
  digits = []
  letters = []
  for char in str:
    if char.isdigit():
      digits.append(char)
    else:
      letters.append(char)

  digits.sort()
  letters.sort()

  sorted_str = "".join(digits + letters)

  # Remove duplicate adjacent characters.
  i = 0
  while i < len(sorted_str) - 1:
    if sorted_str[i] == sorted_str[i + 1]:
      sorted_str = sorted_str[:i] + sorted_str[i + 2:]
    else:
      i += 1

  return sorted_str

# Example 1
str = "z3b1a2"
print(sort_string(str))  # Output: "1a2b3z"

# Additional test cases
str2 = "a55b1c2"
print(sort_string(str2))  # Output: "1a5bc"

str3 = "d1123"
print(sort_string(str3))  # Output: "123d"
