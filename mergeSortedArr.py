def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0

    # Check if either array is empty
    if not arr1:
        return arr2
    if not arr2:
        return arr1
    
    # Merge the two sorted arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    # Append remaining elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

# Example usage:
arr1 = [0, 3, 4, 31]
# arr1 = []
arr2 = [4, 6, 30]
print(merge_sorted_arrays(arr1, arr2))