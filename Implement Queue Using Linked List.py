# Implement Queue Using Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueUsingLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def size(self):
        return self.len

    def isEmpty(self):
        return self.len == 0

    def front(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            return self.head.value

    def enqueue(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.len += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        dataToBeReturned = self.head.value
        self.head = self.head.next
        self.len -= 1
        if self.head is None:
            self.tail = None
        return dataToBeReturned

queue1 = QueueUsingLinkedList()

# Using the queue
queue1.enqueue(5)
queue1.enqueue(6)
queue1.enqueue(7)
queue1.enqueue(8)

print("Front element:", queue1.front())    # 5
print("Is empty?", queue1.isEmpty())       # False

print("Dequeued:", queue1.dequeue())       # 5
print("Dequeued:", queue1.dequeue())       # 6
print("Front now:", queue1.front())        # 7
print("Size now:", queue1.size())          # 2
