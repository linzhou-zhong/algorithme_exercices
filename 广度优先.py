from collections import deque

search_queue = deque()
search_queue += graph['you']
searched = [] #添加已经搜索过的人

while search_queue:
    person = search_queue.popleft()
    if person not in searched: #当这个人没被检查过才检查
        if person_is_seller(person):
            print("Find mango seller")
            return True
        else:
            search_queue += graph[person]
            searched.append(person)#将这个人标记为检查过的
return False

def person_is_seller(name):
    return name[-1] == 'm'
