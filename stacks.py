#python3.10

class Stack:
    def __init__(self,aList):
        self.stack = aList
        
    def push(self,x):
        self.stack.append(x)

    def pop(self):
        self.stack.pop()

    def IsEmpty(self):
        if(self.stack):
            return False
        else:
            return True



myStack = Stack([1,2,3,4]) #initialising the stack

#adding items to the stack
myStack.push(20)
print("Item pushed! Updated stack=",myStack.stack)
myStack.push(30)
print("Item pushed! Updated stack=",myStack.stack)
myStack.push(40)
print("Item pushed! Updated stack=",myStack.stack)
myStack.push(50)
print("Item pushed! Updated stack=",myStack.stack)



#removing items from the stack
myStack.pop()
print("Item popped! Updated stack=",myStack.stack)
myStack.pop()
print("Item popped! Updated stack=",myStack.stack)
myStack.pop()
print("Item popped! Updated stack=",myStack.stack)



#checking is stack is empty
print("Is Stack empty?:",myStack.IsEmpty())
