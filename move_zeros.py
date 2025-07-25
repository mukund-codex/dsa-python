def move_zeros(nums):
    """
    Moves all zeros in the list nums to the end in-place.
    """
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    for i in range(insert_pos, len(nums)):
        nums[i] = 0

# Example usage:
# nums = [0, 1, 0, 3, 12]
# move_zeros(nums)
# print(nums)  # Output: [1, 3, 12, 0, 0]