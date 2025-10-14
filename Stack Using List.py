#Implementing stack using list
class StackUsingList:
    def __init__(self):
        self.__stack = []
    def Push(self,data):
        self.__stack.append(data)
    def Size(self):
        return len(self.__stack)
    def is_empty(self):
        if (len(self.__stack)==0):
            return "stack is empty"
        else:
            return "stack is not empty"
    def top(self):
        if (self.is_empty):
            return None
        return self.__stack[-1]
    def Pop(self):
        if (self.is_empty):
            return None
        return self.__stack.pop

mystack = StackUsingList()
mystack.Push(1)
mystack.Push(2)
mystack.Push(3)
mystack.Push(4)
mystack.is_empty()
mystack.Pop()
mystack.Size()
mystack.top()