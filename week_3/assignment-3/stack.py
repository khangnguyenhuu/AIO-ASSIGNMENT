
class MyStack(object):

    def __init__(self, capacity):
        self.stack_list = []
        self.capacity = capacity

    def initialization(self, capacity):
        self.capacity = capacity

    def is_empty(self):
        if len(self.stack_list) == 0:
            return True
        return False

    def is_full(self):
        if len(self.stack_list) == self.capacity:
            return True
        return False

    def pop(self):
        if self.is_empty():
            print('Empty Stack')
        else:
            a = self.stack_list[-1]
            self.stack_list.pop()
            return a

    def push(self, value):
        self.stack_list.append(value)

    def top(self):
        if self.is_empty():
            print('Empty Stack')
        else:
            return (self.stack_list[-1])
