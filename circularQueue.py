class CircularQueue(object):
    def __init__(self, size):
        self.head = 0
        self.tail = 0
        self.size = size
        self.list = [None] * size
    def add(self, val):
        if (self.tail + 1) % self.size == self.head: # 队列已满
            return False
        else:
            self.list[self.tail] = val
            self.tail = (self.tail + 1) % self.size
    def remove(self):
        if self.head == self.tail: #队列为空
            return False
        else:
            self.list[self.head] = None
            self.head = (self.head + 1) % self.size
            return True
    def get(self):
        tmp_head = self.head
        tmp_tail = self.tail
        result = []
        while tmp_head < tmp_tail:
            val = self.list[tmp_head]
            tmp_head = tmp_head + 1
            result.append(val)
        print(result)


circle = CircularQueue(5)
circle.add(1)
circle.add(2)
circle.add(3)
circle.add(4)
circle.remove()
circle.get()