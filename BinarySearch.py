def binary_search(key, list2search, head, tail):
    if head > tail:
        return -1
    else:
        mid = head + (head + tail)//2
        if key < list2search[mid]:
            return binary_search(key, list2search, head, mid - 1)
        elif key > list2search[mid]:
            return binary_search(key, binary_search, mid + 1, tail)
        else:
            return mid

print('Position of key: ', binary_search(2, [1,2,3,4,5,6,7,8,9], 0, 8))