import sys

class Node :
    def __init__(self, data, left, right ):
        self.data = data
        self.left = left
        self.right = right

def tree_order(node) :
    pre_order.append(node.data)
    if node.left != None :
        tree_order(tree_graph[node.left])
    in_order.append(node.data)
    if node.right != None :
        tree_order(tree_graph[node.right])
    post_order.append(node.data)

    return

if __name__ =='__main__' :

    n = int(sys.stdin.readline().strip())

    tree_graph = {}
    pre_order = []
    in_order = []
    post_order = []

    for i in range(n) :
        data, left, right = sys.stdin.readline().strip().split()
        if left == '.' :
            left = None
        if right == '.' :
            right = None
        tree_graph[data] = Node(data, left, right)

    tree_order(tree_graph['A'])
    for i in pre_order :
        print(i, end= '')

    print()
    for i in in_order :
        print(i, end='')

    print()
    for i in  post_order :
        print(i, end ='')

