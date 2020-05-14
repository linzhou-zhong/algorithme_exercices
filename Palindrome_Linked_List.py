class Node(object):
    def __init__(self, value):
        self.next = None
        self.value = value

def create_list(n):
    head = Node(1)
    pred = head
    for i in range(n-1):
        newNode = Node(i)
        pred.next = newNode
        pred = newNode
    pred.next = head
    return head

a = create_list(10)

def isPalindrome(head):
    if head == None or head.next == None:
        return True
    prev = None
    slow = head
    fast = head
    while(fast != None and fast.next != None):
        print("Done")
        fast = fast.next.next
        nextNode = slow.next
        slow.next = prev
        prev = slow
        slow = nextNode

    if (fast != None): #长度是偶数的时候
        slow = slow.next
    while (slow != None):
        if (slow.value != prev.value):
            return False
        slow = slow.next
        prev = prev.next
    return True

print(isPalindrome(a))