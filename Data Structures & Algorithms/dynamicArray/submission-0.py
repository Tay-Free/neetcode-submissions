class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0 
        self.ints = [0] * capacity

    def get(self, i: int) -> int:
        return self.ints[i]

    def set(self, i: int, n: int) -> None:
        self.ints[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.ints[self.size] = n
        self.size += 1
        

    def popback(self) -> int:
        self.size -= 1
        return self.ints[self.size]
        

    def resize(self) -> None:
        if self.capacity == 0:
            self.capacity = 1
        else:
            self.capacity *= 2

        new_items = [0] * self.capacity

        # Copy old elements over
        for i in range(self.size):
            new_items[i] = self.ints[i]

        # Point to the new list
        self.ints = new_items

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity