class MyQueue(object):
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue_list = []
    
    def is_empty(self):
        if len(self.queue_list) == 0:
            return True
        return False
    
    def is_full(self):
        if len(self.queue_list) == self.capacity:
            return True
        return False
    
    def dequeue(self):
        first_ele = self.queue_list[0]
        self.queue_list.pop(0)
        return first_ele
    
    def enqueue(self, value):
        self.queue_list.append(value)
    
    def front(self):
        return self.queue_list[0]
