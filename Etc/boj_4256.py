import sys
sys.setrecursionlimit(100000)

t = int(input())

def splitTree( preorder, inorder):
    if len(preorder) == 0:
        return
    elif len(preorder) == 1:
        print(preorder[0], end=' ')
        return
    elif len(preorder) == 2:
        print(preorder[1], preorder[0], end=' ')
        return
        
    root = preorder[0]
    root_index = inorder.index(root)
    inleft = inorder[0:root_index]
    inright = inorder[root_index+1:]
    preleft = preorder[1:len(inleft) + 1]
    preright = preorder[1 + len(inleft):]
    
    splitTree(preleft, inleft)  
    splitTree(preright, inright)

    print(root, end=' ')
    

for _ in range(t):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    splitTree(preorder, inorder)
    print()