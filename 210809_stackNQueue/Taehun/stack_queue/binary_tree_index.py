
def dfs(now):
    if tree[now] == 0: return
    preorder.append(tree[now])
    dfs(now * 2) # left
    inorder.append(tree[now])
    dfs(now * 2 + 1) # right
    postorder.append(tree[now])

    return


lst = [1,3,5,2,]
preorder = []
inorder = []
postorder = []
tree = [0 for _ in range(100)]
tree[1] = 1
tree[2] = 3
tree[3] = 5
tree[4] = 2
tree[5] = 6
tree[6] = 7
tree[7] = 8
tree[12] = 9
tree[15] = 4
tree[24] = 10