#Name: Wong Fook Weng Matthew Oliver
#Admin No: 220261J
#IT2553-01
#SF2201
class Queue():
    def __init__(self):
        self.items = []
    #Returns the first item in the queue
    def peek(self):
        return self.items[self.size()-1]
    #Returns true if the queue is empty
    def isEmpty(self):
        return self.items == []
    #Adds an item to the queue
    def enqueue(self, item):
        self.items.insert(0,item)
    #Removes an item from the queue
    def dequeue(self):
        return self.items.pop()
    #Returns the size of the queue
    def size(self):
        return len(self.items)
