class ArrayManipulator:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length
    
    def pop(self):
        if self.length == 0:
            return None
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item
    
    def delete(self, index):
        if index < 0 or index >= self.length:
            return None
        deleted_item = self.data[index]
        self.shift_items(index)
        return deleted_item
    
    def __str__(self):
        return str(self.data)
    
    def shift_items(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1
        return self.data

newArray = ArrayManipulator();
newArray.push('Hi')
newArray.push('You')
newArray.push('There')
newArray.pop()
newArray.push('!')
newArray.push('How are you?')
newArray.push('Goodbye')
newArray.pop()
newArray.delete(1)
print(newArray)