class stack(object):
    def __init__(self, size):
        self.list = []
        self.size = size
        self.count = 0

    def pop(self):
        if self.count == 0:
            return None
        val = self.list[self.count - 1]
        del self.list[self.count - 1]
        self.count -= 1
        return val

    def push(self, value): #入栈操作
        if self.count  == self.size: #栈空间已满
            return False
        self.list.append(value)
        self.count += 1
        return True

    def get(self):
        print(self.list)
            
stack = stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.push(4)
stack.pop()
stack.get()