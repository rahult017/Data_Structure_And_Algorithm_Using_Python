def two_sum(nums, target):
    # Create a dictionary to store the indices of elements
    index_dict = {}

    for index, value in enumerate(nums):
        complement = target - value
        
        if complement in index_dict:
            return [index_dict[complement], index]
        
        # # Store the current number and its index in the dictionary
        index_dict[value] = index

    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)
