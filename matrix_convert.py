alist = [[1,2],[3,4],[5,6]]

m = len(alist)
n = len(alist[0])

newlist = [[0] * m for i in range(n)]
#newlist = [[0] * m] * n 如果这样声明会造成地址复制，n个自列表同时被修改

for i in range(len(alist)):
    for j in range(len(alist[i])):
        newlist[j][i] = alist[i][j]

print(newlist)

