def get_pairs(arr):
    """
    Returns all unique pairs of elements from the given array.
    Each pair is represented as a tuple (a, b) where a comes before b in the array.
    """
    pairs = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            pairs.append((arr[i], arr[j]))
    return pairs

# Example usage:
arr = [1, 2, 3]
print(get_pairs(arr))  # Output: [(1, 2), (1, 3), (2, 3)]