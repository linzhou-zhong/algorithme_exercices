class Node(object):
    def __init__(self, value = 0):
        self.value = value
        self.next = None
class QueueLinkedList():
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
    def create_queueLinkedList(self, size):
        if size == 0:
            return None
        tmp_head = self.head
        for i in range(size + 1):
            newNode = Node(i + 1)
            tmp_head.next = newNode
            tmp_head = newNode
            if i == size:
                newNode.next = self.tail
    def add(self, val):
        tmp_head = self.head
        while tmp_head.next != self.tail: #到达末尾
            tmp_head = tmp_head.next 
        newNode = Node(value=val)
        tmp_head.next = newNode
        newNode.next = self.tail
    def remove(self):
        if self.head.next == self.tail:
            return False
        else:
            tmp_head = self.head
            tmp_head.next = tmp_head.next.next
    def get(self):
        tmp_head = self.head.next
        result = []
        while tmp_head.next != self.tail and tmp_head != self.tail:
            result.append(tmp_head.value)
            tmp_head = tmp_head.next
        print(result)
    
queue = QueueLinkedList()
queue.create_queueLinkedList(5)
queue.remove()
queue.get()