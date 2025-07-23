arr1 = ['a', 'b ', 'c ', 'x']
arr2 = ['z', 'y', 'a']

def containsCommonItem2(arr1, arr2):
    set1 = set(arr1)
    for item in arr2:
        if item in set1:
            return True
    return False


print(containsCommonItem2(arr1, arr2))