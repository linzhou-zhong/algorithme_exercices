class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def create_list(n):
    head = Node(0)
    node = head
    for i in range(1, n+1):
        newNode = Node(i)
        node.next = newNode
        node = newNode
        #if i == n:
        #    node.next = head
    return head

def palindrome(head):
    if head.next == None or head == None:
        return True
    slow = head
    quick = head
    prev = None
    while quick != None and quick.next != None:
        quick = quick.next.next
        nextNode = slow.next
        slow.next = prev
        prev = slow
        slow = nextNode
    if quick != None:
        slow = slow.next #判断奇偶性
    while slow != None:
        if (slow.val != prev.val):
            return False
        slow = slow.next
        prev = prev.next
    return True

def reverse_linkedList(head): #链表的反转
    if head.next == None or head == None:
        return head
    slow = head
    quick = head.next
    prev = None
    while quick.next != None:
        slow.next = prev
        prev = slow
        slow = quick
        quick = quick.next
        print(prev.val)
    return(head)

def check_circle_linkedList(head):
    if head.next == None or head == None:
        return False
    slow = head
    fast = head
    while fast.next != None and fast != None:
        fast = fast.next.next
        slow = slow.next
        if fast.next == slow.next:
            return True
    return False

def delete_node_from_linkedList(head, number):
    if head == None or head.next == None and number != 1:
        return None
    slow = head
    fast = head.next
    if number == 1: #删除第一个结点
        return slow
    else:
        for i in range(number-1):
            slow = slow.next
            fast = fast.next
            if fast == None:
                return head
        slow.next = fast.next

    return head

def print_linkedList(head):
    if head == None:
        return None
    while head != None:
        print(head.val)
        head = head.next

def delete_last_node(head, number):
    if head == None or head.next == None:
        return None
    if number == 0:
        return head

    slow = head
    fast = head
    prev = None

    for i in range(number-1):
        fast = fast.next
        if fast.next == None and i != number-2:
            return None
    while fast.next != None:
        fast = fast.next
        prev = slow
        slow = slow.next

    if prev == None:
        head = head.next

    else:
        prev.next = slow.next
    
    return head

head = create_list(10)
head = delete_last_node(head,5)
print_linkedList(head)