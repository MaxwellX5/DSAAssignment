#Name: Wong Fook Weng Matthew Oliver
#Admin No: 220261J
#IT2553-01
#SF2201
class Queue():
    def __init__(self):
        self._items = []

    #Returns true if the queue is empty
    def isEmpty(self):
        return self._items == []

    #Adds an item to the queue
    def enqueue(self, item):
        self._items.insert(0,item)

    #Removes an item from the queue
    def dequeue(self):
        if self.isEmpty():
            return "Cannot dequeue when list is empty"

        return self._items.pop()

    #Returns the size of the queue
    def __len__(self):
        return len(self._items)
