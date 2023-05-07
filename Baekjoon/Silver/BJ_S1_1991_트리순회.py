import sys;sys.stdin = open('input.txt')

def back(parent):
    global preorder,inorder,postorder
    if parent == -1:
        return
    preorder += chr(parent+65)
    back(tree[parent][0])
    inorder += chr(parent+65)
    back(tree[parent][1])
    postorder += chr(parent+65)

N = int(input())
tree = [[-1,-1] for _ in range(26)]
for _ in range(N):
    p,c1,c2 = map(str,input().split())
    if c1 != '.' :tree[ord(p)-65][0] = (ord(c1)-65)
    if c2 != '.' :tree[ord(p)-65][1] = (ord(c2)-65)
preorder = postorder = inorder = ''
back(0)
print(preorder)
print(inorder)
print(postorder)
