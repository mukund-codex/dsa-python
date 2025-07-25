def rotate(nums, k):
    n = len(nums)
    k %= n  # In case k > n
    nums[:] = nums[-k:] + nums[:-k]

# Example usage:
if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    rotate(nums, k)
    print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]