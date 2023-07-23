def postorder(preorder, inorder):
    if len(preorder) == 0:
        return []
    root = preorder[0]
    idx = None
    for i in range(len(inorder)):
        if inorder[i] == root:
            idx = i
    left = inorder[0:idx]
    right = inorder[idx+1:]
    return postorder(preorder[1:len(left)+1], left) + postorder(preorder[len(left)+1:], right) + [root]

T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    print(*postorder(preorder, inorder))
