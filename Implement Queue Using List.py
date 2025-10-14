class QueueUsingList:
    def __init__(self):
        self.__queue = []

    def size(self):
        return len(self.__queue)
    
    def is_empty(self):
        return self.size() == 0
    
    def enqueue(self,data):
        self.__queue.append(data)

    def dequeue(self):
        if (self.size()==0):
            print("Queue is empty")
        else:
            return self.__queue.pop(0)
        
    def front(self):
        if (self.size()==0):
            print("Queue is empty")
        else:
            return self.__queue[0]
        
# Create instance
queue1 = QueueUsingList()

# Using the queue
queue1.enqueue(5)
queue1.enqueue(6)
queue1.enqueue(7)
queue1.enqueue(8)


print("Front element:", queue1.front())  # 5
print("Is empty?", queue1.is_empty())    # False

print("Dequeued:", queue1.dequeue())     # 5
print("Dequeued:", queue1.dequeue())     # 6
print("Front now:", queue1.front())      # 7
print("Size now:", queue1.size())        # 2