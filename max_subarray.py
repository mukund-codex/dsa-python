def max_subarray_sum(nums):
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
print(max_subarray_sum([1]))  # Output: 1
print(max_subarray_sum([5,4,-1,7,8]))  # Output: 23
print(max_subarray_sum([-1,-2,-3,-4]))  #