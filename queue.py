#ptyton3.10

#Implementation of Queue using list

class Queue:
    def __init__(self, queue):
        self.queue = queue

    def enqueue(self,x):
        self.queue.insert(0,x)

    def dequeue(self):
        self.queue.pop()

    def IsEmpty(self):
        if(self.queue):
            return False
        else:
            return True


        
myqueue = Queue([1,2,3,4]) #initialising the queue

#adding items to the queue
myqueue.enqueue(20)
print("Item pushed! Updated queue=",myqueue.queue)
myqueue.enqueue(30)
print("Item pushed! Updated queue=",myqueue.queue)
myqueue.enqueue(40)
print("Item pushed! Updated queue=",myqueue.queue)
myqueue.enqueue(50)
print("Item pushed! Updated queue=",myqueue.queue)



#removing items from the queue
myqueue.dequeue()
print("Item popped! Updated queue=",myqueue.queue)
myqueue.dequeue()
print("Item popped! Updated queue=",myqueue.queue)
myqueue.dequeue()
print("Item popped! Updated queue=",myqueue.queue)



#checking is queue is empty
print("Is queue empty?:",myqueue.IsEmpty())
