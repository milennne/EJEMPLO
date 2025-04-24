class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.size_count = 0
        self.items = [None] * capacity 

    def is_empty(self):
        return self.size_count == 0

    def is_full(self):
        return self.size_count == self.capacity
    
    def enQueue(self, item):
        if self.is_full():
            data = self.items[self.front]
            self.items[self.front] = item
            self.front = (self.front + 1) % self.capacity 
            self.rear = (self.rear + 1) % self.capacity
            return f"Se reemplazo el elemento {data} por el elemento {self.items[self.front]}"
        

        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity

        self.size_count += 1

    def deQueue(self):
        "Remove and return the front item"
        if self.is_empty():
            return "The queue is empty"
        data = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity

        self.size_count -= 1
        return data
    
    def peek(self):
        if self.is_empty():
            return "The queue is empty"
        return self.items[self.front]
    
    def size(self):
        return self.size_count



    def display(self):
        if self.is_empty():
            return "Queue = []"
        
        result = []
        index = self.front
        for _ in range(self.size_count):
            result.append(str(self.items[index]))
            index = (index + 1) % self.capacity
        
        return f"Queue: [{', '.join(result)}]"
    
def rotate_array(arr, k):
    
    n = len(arr)
    queue = CircularQueue(n)

    

    for i in arr:
        queue.enQueue(i)
    
    k = k % n
    for i in range(n - k):
        val = queue.deQueue() 
        queue.enQueue(val) 


    
    result = []
    index = queue.front
    for i in range(queue.size_count):
        result.append(queue.items[index])
        index = (index+1) % queue.capacity
    return result


print(rotate_array([1, 2, 3, 4], 5))  # -> [4, 1, 2, 3]
print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3)) # -> [5, 6, 7, 1, 2, 3, 4]
print(rotate_array([9, 5, 7, 3], 3)) # -> [5, 7, 3, 9]



1234

4123
3412
2341
1234
4123


1234567
7123456
6712345
5671234

9573
3957
7395
5739