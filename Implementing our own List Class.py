# Implementing our own List Class
# Custom Dynamic Array

# In this exercise, you will implement a custom dynamic array class, similar to Python’s built-in list. Your task is to create a class CustomList that supports dynamic resizing and several list operations.

# Class Definition

# Class Name: CustomList

# Attributes:

# capacity: The current capacity of the internal array.

# size: The number of elements currently stored in the array.

# array: The internal storage for the list elements.

# Methods:

# __init__(self): Initializes an empty CustomList with an initial capacity of 1.

# append(self, item): Adds an item to the end of the list. If the list is full, it should resize the internal storage to accommodate more elements.

# __len__(self): Returns the number of elements in the list.

# __str__(self): Returns a string representation of the list, formatted like a Python list.

# pop(self): Removes and returns the last item in the list. If the list is empty, it should return an appropriate error message.

# __getitem__(self, index): Retrieves the item at the specified index. If the index is out of bounds, it should return an error message.

# clear(self): Clears all items from the list.

# insert(self, position, element): Inserts an element at the specified position. If the list is full, it should resize the internal storage.

# remove(self, element): Removes the first occurrence of the specified element from the list. If the element is not found, it should return an error message.

class CustomList:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = [None] * self.capacity
    
    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
    
    def append(self, item):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.array[self.size] = item
        self.size += 1
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        return "[" + ", ".join(str(self.array[i]) for i in range(self.size)) + "]"
    
    def pop(self):
        if self.size == 0:
            return "Error: list is empty"
        item = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        # Optional: shrink the array if too empty (not required, but nice)
        if 0 < self.size <= self.capacity // 4:
            self._resize(self.capacity // 2)
        return item
    
    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            return "Error: index out of bounds"
        return self.array[index]
    
    def clear(self):
        self.size = 0
        self.capacity = 1
        self.array = [None] * self.capacity
    
    def insert(self, position, element):
        if position < 0 or position > self.size:
            return "Error: index out of bounds"
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        # Shift elements right
        for i in range(self.size, position, -1):
            self.array[i] = self.array[i-1]
        self.array[position] = element
        self.size += 1
    
    def remove(self, element):
        found_index = -1
        for i in range(self.size):
            if self.array[i] == element:
                found_index = i
                break
        if found_index == -1:
            return "Error: element not found"
        # Shift elements left to fill gap
        for i in range(found_index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1
        # Optional shrink
        if 0 < self.size <= self.capacity // 4:
            self._resize(max(1, self.capacity // 2))
