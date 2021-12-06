def dfs(now) :
    if now == 0 :
        return
    preorder.append(now)
    dfs(left[now]) # 왼쪽
    inorder.append(now)
    dfs(right[now]) # 오른쪽
    postorder.append(now)
    return

left = [0 for _ in range(11)]
right = [0 for _ in range(11)]

root = 1
left[1] = 3
right[1] = 5
left[3] = 2
right[3] = 6
left[5] = 7
right[5] = 8
left[7] = 9
left[9] = 10
right[8] = 4

preorder = [] # 저장하기
postorder = []
inorder  = []
dfs(root)

print(*preorder)
print(*postorder)
print(*inorder)