class ArrayQueue(object):
    def __init__(self, size):
        self.queue = [None] * size
        self.head = 0
        self.tail = 0
        self.size = size
    def enqueue(self, value): #入队处理
        if self.tail == self.size: 
            if self.head == 0: #队列已满
               return False
            for i in range(self.head, self.tail):
                self.queue[i - self.head] = self.queue[i]
            self.tail -= self.head
            self.head = 0
            
        self.queue[self.tail] = value
        self.tail += 1
        return True

    def dequeue(self):
        if self.tail == self.head:
            return None
        else:
            value = self.queue[self.head]
            self.queue[self.head] = None
            self.head += 1
            return value

    def get(self):
        print(self.queue)
        
queue = ArrayQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.get()
queue.dequeue()
queue.get()
queue.enqueue(3)
queue.enqueue(4)
queue.get()
