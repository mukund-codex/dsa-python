strings = ['a', 'b', 'c', 'd', 'e']

print(strings[2])

# push 'f' to the end of the list
strings.append('f') # O(1)
print(strings)

# pop the last element from the list
strings.pop() # O(1)
print(strings)

# insert 'x' at index 1
strings.insert(0, 'x') # O(n)
print(strings)

# splice the list to add 'alien' at index 2
strings[2:2] = ['alien'] # O(n)
print(strings)

# create a static array of size 5 with the elements 1, 2, 3, 4, 5
static_array = [1, 2, 3, 4, 5]
print(static_array)


# create a object with value 10 and a reference to the static array
class StaticArrayObject:
    def __init__(self, value, static_array):
        self.value = value
        self.static_array = static_array

# create an instance of StaticArrayObject
static_array_object = StaticArrayObject(10, static_array)
print(static_array_object.value)
print(static_array_object.static_array)